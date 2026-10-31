import sys


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    """Explicitly catches division by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a: float, b: float) -> float:
    return a**b


def modulus(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot calculate remainder when divisor is zero.")
    return a % b


def get_valid_number(prompt: str) -> float:
    """Continuously prompts until the user provides a valid real number."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("  [!] Invalid input: Please enter a numeric value (e.g., 5, -2.4, 10).")


def main():
    operations = {
        "+": ("Addition", add),
        "-": ("Subtraction", subtract),
        "*": ("Multiplication", multiply),
        "/": ("Division", divide),
        "^": ("Power", power),
        "%": ("Modulus", modulus),
    }

    print("=" * 40)
    print("      DAY 5: ROBUST CLI CALCULATOR     ")
    print("=" * 40)
    print("Operations: +  -  *  /  ^  %")
    print("Type 'q' or 'exit' anytime to quit.\n")

    while True:
        operator = input("Enter operator (+, -, *, /, ^, %) or 'q' to quit: ").strip().lower()

        if operator in ("q", "exit"):
            print("Exiting calculator. Great job today!")
            sys.exit(0)

        if operator not in operations:
            print(f"  [!] '{operator}' is not a valid operator. Choose from: +, -, *, /, ^, %\n")
            continue

        op_name, func = operations[operator]
        print(f"\n--- {op_name} ---")

        # Safely capture inputs without crashing on letters
        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")

        # Perform the calculation with targeted exception handling
        try:
            result = func(num1, num2)
            # Format: strip trailing .0 for clean whole numbers
            clean_res = f"{result:g}" if isinstance(result, float) else result
            print(f"\n=> Result: {num1:g} {operator} {num2:g} = {clean_res}\n")

        except ZeroDivisionError as err:
            print(f"\n[Math Error]: {err}\n")

        except OverflowError:
            print("\n[Math Error]: Calculation result exceeds memory limits.\n")

        except Exception as e:
            print(f"\n[Unexpected Error]: {e}\n")


if __name__ == "__main__":
    main()