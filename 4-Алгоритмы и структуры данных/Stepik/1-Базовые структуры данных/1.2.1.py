def check(input_string: str) -> str:
    bracket_stack: list = []
    for i, char in enumerate(input_string, start=1):
        if char in '])}':
            if len(bracket_stack) == 0:
                return str(i)
            else:
                last_open = bracket_stack.pop()[0]
                if ((last_open == '(' and char != ')')
                        or (last_open == '[' and char != ']')
                        or (last_open == '{' and char != '}')):
                    return str(i)
        if char in '[({':
            bracket_stack.append((char, i))
    if len(bracket_stack) == 0:
        return "Success"
    else:
        return str(bracket_stack.pop()[1])


if __name__ == '__main__':
    print(check(input()))
