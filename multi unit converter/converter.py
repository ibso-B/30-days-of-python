import sys


# ------------------ Conversion Logic ------------------

# Length: base unit is meters (m)
LENGTH_TO_METERS = {
    "km": 1000.0,
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254,
}

# Weight: base unit is kilograms (kg)
WEIGHT_TO_KG = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 0.000001,
    "lb": 0.45359237,
    "oz": 0.028349523125,
    "ton": 907.18474,  # US Short ton
}


def convert_ratio(val: float, from_unit: str, to_unit: str, ratios: dict) -> float:
    """Generic conversion via base unit."""
    base_val = val * ratios[from_unit]
    return base_val / ratios[to_unit]


def convert_temperature(val: float, from_u: str, to_u: str) -> float:
    """Temperature conversions via Celsius as the intermediary."""
    # Convert to Celsius
    if from_u == "c":
        c = val
    elif from_u == "f":
        c = (val - 32) * 5 / 9
    elif from_u == "k":
        c = val - 273.15
    else:
        raise ValueError(f"Unknown unit: {from_u}")

    # Convert Celsius to target
    if to_u == "c":
        return c
    elif to_u == "f":
        return (c * 9 / 5) + 32
    elif to_u == "k":
        return c + 273.15
    else:
        raise ValueError(f"Unknown unit: {to_u}")


# ------------------ Interactive Handlers ------------------

def handle_linear_conversion(name: str, table: dict):
    print(f"\n--- {name} Converter ---")
    available_units = list(table.keys())
    print(f"Supported units: {', '.join(available_units)}")

    from_u = input("Convert from: ").strip().lower()
    if from_u not in table:
        print(f"Invalid unit '{from_u}'. Returning to menu.")
        return

    to_u = input("Convert to: ").strip().lower()
    if to_u not in table:
        print(f"Invalid unit '{to_u}'. Returning to menu.")
        return

    val_str = input(f"Enter amount in {from_u}: ").strip()
    try:
        val = float(val_str)
    except ValueError:
        print("Invalid number entered.")
        return

    res = convert_ratio(val, from_u, to_u, table)
    print(f"\nResult: {val:g} {from_u} = {res:.6g} {to_u}\n")


def handle_temperature_conversion():
    print("\n--- Temperature Converter ---")
    print("Supported units: C (Celsius), F (Fahrenheit), K (Kelvin)")

    valid = {"c", "f", "k"}
    from_u = input("Convert from: ").strip().lower()
    if from_u not in valid:
        print(f"Invalid unit '{from_u}'.")
        return

    to_u = input("Convert to: ").strip().lower()
    if to_u not in valid:
        print(f"Invalid unit '{to_u}'.")
        return

    val_str = input(f"Enter value in °{from_u.upper()}: ").strip()
    try:
        val = float(val_str)
    except ValueError:
        print("Invalid number entered.")
        return

    res = convert_temperature(val, from_u, to_u)
    print(f"\nResult: {val:g} °{from_u.upper()} = {res:.4f} °{to_u.upper()}\n")


def main():
    while True:
        print("=== Unit Converter ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            handle_linear_conversion("Length", LENGTH_TO_METERS)
        elif choice == "2":
            handle_linear_conversion("Weight", WEIGHT_TO_KG)
        elif choice == "3":
            handle_temperature_conversion()
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select 1 through 4.\n")


if __name__ == "__main__":
    main()