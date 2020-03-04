def input_positive_integer(prompt):
    while True:
        try:
            value=int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value < 0:
            print("Number must be positive.")
            continue
        else:
            break
    return value

def input_positive_float(prompt):
    while True:
        try:
            value=float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value < 0:
            print("Number must be positive.")
            continue
        else:
            break
    return value