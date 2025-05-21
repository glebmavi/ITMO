"""
Examples
Rule 30 with a single live cell in the middle:

    python cellular_automata.py 1d --rule 30 --cells 101 --init single

1‑D Rule 110 with a random initial row (50 % density):

    python cellular_automata.py 1d --rule 110 --cells 201 --init random --density 0.5

Game of Life on an 80 × 80 grid with 30 % live cells:

    python cellular_automata.py life --rows 80 --cols 80 --density 0.3

"""

from __future__ import annotations

import argparse
import itertools
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib; matplotlib.use("TkAgg")


def rule_to_bits(rule: int) -> np.ndarray:
    if not 0 <= rule <= 255:
        raise ValueError("Rule must be between 0 and 255 (inclusive).")
    return np.array([(rule >> k) & 1 for k in range(8)], dtype=np.uint8)


def step_1d(state: np.ndarray, bits: np.ndarray) -> np.ndarray:
    left  = np.roll(state,  1)
    right = np.roll(state, -1)
    idx   = (left << 2) | (state << 1) | right
    return bits[idx]


def run_1d_ca(rule: int, n_cells: int, init: str, density: float) -> None:
    """Animate a 1‑D elementary cellular automaton **infinitely**."""
    bits = rule_to_bits(rule)

    if init == "single":
        state               = np.zeros(n_cells, dtype=np.uint8)
        state[n_cells // 2] = 1
    elif init == "random":
        state = (np.random.default_rng().random(n_cells) < density).astype(np.uint8)
    else:
        raise ValueError("init must be 'single' or 'random'.")

    # We keep appending rows so the image grows downward.
    rows = [state.copy()]

    fig, ax = plt.subplots(figsize=(8, 6))
    im      = ax.imshow(np.vstack(rows), aspect="auto", interpolation="nearest")
    title   = ax.set_title("")
    ax.set_xlabel("Cell index")
    ax.yaxis.set_visible(False)

    def update(frame: int):
        nonlocal state
        state = step_1d(state, bits)
        rows.append(state)
        im.set_data(np.vstack(rows))
        title.set_text(f"1‑D CA – Rule {rule} – step {frame + 1}")
        return im, title

    ani = FuncAnimation(fig, update, frames=itertools.count(), interval=40)
    plt.show()


def step_life(grid: np.ndarray) -> np.ndarray:
    """Vectorised Game of Life step with periodic boundaries."""
    nbrs = (
        np.roll(grid,  1, 0) + np.roll(grid, -1, 0) +
        np.roll(grid,  1, 1) + np.roll(grid, -1, 1) +
        np.roll(np.roll(grid, 1, 0),  1, 1) +
        np.roll(np.roll(grid, 1, 0), -1, 1) +
        np.roll(np.roll(grid,-1, 0),  1, 1) +
        np.roll(np.roll(grid,-1, 0), -1, 1)
    )
    birth   = (grid == 0) & (nbrs == 3)
    survive = (grid == 1) & ((nbrs == 2) | (nbrs == 3))
    return (birth | survive).astype(np.uint8)


def run_game_of_life(rows: int, cols: int, density: float) -> None:
    """Animate Conway's Game of Life **infinitely**."""
    rng  = np.random.default_rng()
    grid = (rng.random((rows, cols)) < density).astype(np.uint8)

    fig, ax = plt.subplots(figsize=(6, 6))
    im      = ax.imshow(grid, interpolation="nearest")
    title   = ax.set_title("")
    ax.axis("off")

    def update(frame: int):
        nonlocal grid
        grid = step_life(grid)
        im.set_data(grid)
        title.set_text(f"Game of Life — step {frame + 1}")
        return im, title

    ani = FuncAnimation(fig, update, frames=itertools.count(), interval=40)
    plt.show()



def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Infinite animation of 1‑D CA or Game of Life.")
    sub = parser.add_subparsers(dest="mode", required=True)

    # 1‑D CA
    p1d = sub.add_parser("1d", help="Run a 1‑D elementary cellular automaton")
    p1d.add_argument("--rule", type=int, default=30, help="Wolfram rule number [0–255] (default: 30)")
    p1d.add_argument("--cells", type=int, default=101, help="Number of cells (default: 101)")
    p1d.add_argument("--init", choices=["single", "random"], default="single",
                    help="Initial pattern: single (default) or random")
    p1d.add_argument("--density", type=float, default=0.5,
                    help="Live‑cell density for random init (default: 0.5)")

    # Game of Life
    plife = sub.add_parser("life", help="Run Conway's Game of Life")
    plife.add_argument("--rows", type=int, default=80, help="Grid rows (default: 80)")
    plife.add_argument("--cols", type=int, default=80, help="Grid columns (default: 80)")
    plife.add_argument("--density", type=float, default=0.3,
                      help="Initial live‑cell density (default: 0.3)")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    if args.mode == "1d":
        run_1d_ca(args.rule, args.cells, args.init, args.density)
    elif args.mode == "life":
        run_game_of_life(args.rows, args.cols, args.density)
    else:
        raise RuntimeError("Unexpected mode: " + str(args.mode))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
