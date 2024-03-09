def reader():
    str = ''
    first_line = input()
    n = int(first_line.split()[1])
    for i in range(n):
        str += input() + '\n'

    return first_line + '\n' + str


def parser(str: str):
    packets = str.split('\n')
    size = int(packets[0].split()[0])
    n = int(packets[0].split()[1])
    packets = packets[1:n+1]
    return size, n, packets


def packet_process(size: int, n: int, packets: list):
    buffer = []
    result = []
    for packet in packets:
        arrival, duration = packet.split()
        arrival = int(arrival)
        duration = int(duration)
        if len(buffer) == size:
            while buffer:
                if buffer[0][0] <= arrival:
                    buffer.pop(0)
                else:
                    break
        if len(buffer) < size:
            if not buffer:
                buffer.append((arrival + duration, arrival))
                result.append(arrival)
            else:
                if buffer[-1][0] <= arrival:
                    buffer.append((arrival + duration, arrival))
                    result.append(arrival)
                else:
                    buffer.append((buffer[-1][0] + duration, arrival))
                    result.append(buffer[-2][0])
        else:
            result.append(-1)
    return result


if __name__ == '__main__':
    size, n, packets = parser(reader())
    for i in packet_process(size, n, packets):
        print(i)
