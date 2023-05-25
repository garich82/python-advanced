def operate(operator, *args):
    """Performs the specified operator on multiple numbers and returns the result."""
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
    elif operator == "/":
        result = args[0]
        for num in args[1:]:
            result /= num
    else:
        return "Invalid operator"

    return result

print(operate("*", 3, 4))