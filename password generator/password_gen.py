import secrets
import string
import sys


def get_yes_no(prompt: str, default: bool = True) -> bool:
    """Helper to prompt the user for a boolean (y/n) decision."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        resp = input(prompt + suffix).strip().lower()
        if not resp:
            return default
        if resp in ("y", "yes"):
            return True
        if resp in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def generate_password(length: int, use_upper: bool, use_lower: bool, use_digits: bool, use_symbols: bool) -> str:
    categories = []
    if use_upper:
        categories.append(string.ascii_uppercase)
    if use_lower:
        categories.append(string.ascii_lowercase)
    if use_digits:
        categories.append(string.digits)
    if use_symbols:
        # Punctuation set safe for standard web forms and terminal rendering
        categories.append("!@#$%^&*()-_=+[]{}|;:,.<>?")

    if not categories:
        raise ValueError("At least one character set must be selected.")

    if length < len(categories):
        raise ValueError(f"Length must be at least {len(categories)} to satisfy chosen character sets.")

    # Guarantee at least one character from every selected category
    password_chars = [secrets.choice(cat) for cat in categories]

    # Fill the remaining length from the combined character pool
    all_allowed = "".join(categories)
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_allowed))

    # Shuffle cryptographically to avoid predictable character positions
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("=== Secure Password Generator ===")
    
    while True:
        try:
            length_input = input("Enter password length (minimum 4, recommended 12+): ").strip()
            length = int(length_input)
            if length < 4:
                print("Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    print("\nCharacter preferences:")
    use_upper = get_yes_no("Include uppercase letters (A-Z)?", default=True)
    use_lower = get_yes_no("Include lowercase letters (a-z)?", default=True)
    use_digits = get_yes_no("Include numbers (0-9)?", default=True)
    use_symbols = get_yes_no("Include special symbols (!@#$...)?", default=True)

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("\n" + "=" * 40)
        print(f"Generated Password: {password}")
        print("=" * 40)
    except ValueError as err:
        print(f"\nError: {err}")


if __name__ == "__main__":
    main()