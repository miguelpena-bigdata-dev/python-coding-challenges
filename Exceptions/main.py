if __name__ == '__main__':
    for _ in range(int(input())):
        args = input().split()
        try:
            print(int(args[0]) // int(args[1]))
        except (ValueError, ZeroDivisionError) as error:
            print("Error Code:", error)
