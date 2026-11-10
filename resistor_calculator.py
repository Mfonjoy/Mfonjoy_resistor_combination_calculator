# Resistor Combination Calculator
# Calculates total resistance in series and in parallel.
# My twist: it also asks for a supply voltage and works out the
# current and power for each circuit using Ohm's law.


def get_positive_number(prompt, whole_number=False):
    """Keep asking until the user types a valid number greater than 0.
    If whole_number is True, the input is converted with int(),
    otherwise it is converted with float()."""
    while True:
        text = input(prompt)
        try:
            if whole_number:
                value = int(text)
            else:
                value = float(text)
        except ValueError:
            # The user typed letters or symbols instead of a number
            print("Please type a number, not letters or symbols.")
            continue
        if value <= 0:
            print("The number must be greater than 0.")
        else:
            return value


def series_resistance(values):
    """Series: just add all the resistors. Returns the total in ohms."""
    return sum(values)


def parallel_resistance(values):
    """Parallel: 1/Rt = 1/R1 + 1/R2 + ... Returns the total in ohms."""
    total_conductance = 0
    for r in values:
        total_conductance += 1 / r
    return 1 / total_conductance


def current_and_power(voltage, resistance):
    """Ohm's law: I = V / R and P = V * I. Returns current (A) and power (W)."""
    current = voltage / resistance
    power = voltage * current
    return current, power


def main():
    print("=== Resistor Combination Calculator ===")

    while True:
        # Step 1: find out how many resistors there are
        count = get_positive_number("How many resistors do you have? ", whole_number=True)

        # Step 2: store each resistor value in a list
        resistors = []
        for i in range(1, count + 1):
            value = get_positive_number(f"Enter value of resistor {i} (in ohms): ")
            resistors.append(value)

        # Step 3: calculate the totals
        total_series = series_resistance(resistors)
        total_parallel = parallel_resistance(resistors)

        print("\n--- Results ---")
        print(f"Resistors entered: {resistors}")
        print(f"Series total:   {total_series:.2f} ohms")
        print(f"Parallel total: {total_parallel:.2f} ohms")

        # Step 4 (my twist): current and power from a supply voltage
        voltage = get_positive_number("\nEnter the supply voltage (in volts): ")
        i_series, p_series = current_and_power(voltage, total_series)
        i_parallel, p_parallel = current_and_power(voltage, total_parallel)

        print(f"\nAt {voltage} V:")
        print(f"Series:   current = {i_series:.4f} A, power = {p_series:.4f} W")
        print(f"Parallel: current = {i_parallel:.4f} A, power = {p_parallel:.4f} W")

        # Step 5: ask if the user wants to go again
        again = input("\nCalculate another circuit? (y/n): ").strip().lower()
        if again == "y":
            print()
        elif again == "n":
            print("Goodbye!")
            break
        else:
            print("I did not understand that, so I will stop here. Goodbye!")
            break


# This makes the program start when the file is run
main()
