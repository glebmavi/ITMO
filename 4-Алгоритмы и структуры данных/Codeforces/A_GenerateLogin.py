def generate_login(first_name, last_name):
    login = first_name[0]
    for i in range(1, len(first_name)):
        if first_name[i] >= last_name[0]:
            break
        else:
            login += first_name[i]
    login += last_name[0]
    return login


if __name__ == "__main__":
    f, l = input().split()
    print(generate_login(f, l))
