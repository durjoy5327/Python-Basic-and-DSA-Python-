import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("Number1", type=int, help="First Number")
    parser.add_argument("Number2", type=int, help="Second Number")
    parser.add_argument("Operation", choices=['+', '-', '*', '/'], help="Operator")
    args = parser.parse_args()

    n1 = args.Number1
    n2 = args.Number2

    if args.Operation == '+':
        print(n1 + n2)
    elif args.Operation == '-':
        print(n1 - n2)
    elif args.Operation == '*':
        print(n1 * n2)
    elif args.Operation == '/':
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(n1 / n2)
    else:
        print("Invalid operation. Please use one of the following: +, -, *, /")
