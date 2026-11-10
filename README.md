# Resistor Combination Calculator

## What it does
This program asks how many resistors you have and the value of each one in ohms. It then calculates and prints the **total resistance** when they are connected in **series** and in **parallel**. It rejects letters, zero and negative numbers, and asks again until the input is valid.

## How to run it
Install Python 3, then run: `python resistor_calculator.py`

## Sample output
```
=== Resistor Combination Calculator ===
How many resistors do you have? 3
Enter value of resistor 1 (in ohms): 100
Enter value of resistor 2 (in ohms): 200
Enter value of resistor 3 (in ohms): 300

--- Results ---
Resistors entered: [100.0, 200.0, 300.0]
Series total:   600.00 ohms
Parallel total: 54.55 ohms

Enter the supply voltage (in volts): 12

At 12.0 V:
Series:   current = 0.0200 A, power = 0.2400 W
Parallel: current = 0.2200 A, power = 2.6400 W

Calculate another circuit? (y/n): n
Goodbye!
```

## My own twist
After the resistance totals, the program asks for a **supply voltage** and uses **Ohm's law** (I = V / R and P = V x I) to calculate the **current and power** for both the series and parallel circuits. This shows how the same resistors behave very differently depending on how they are connected.

## What I learned
- Programs must **check input before using it**, otherwise a typed letter crashes everything. I solved this with a function that keeps asking until the number is valid.
- Splitting the work into **small functions that return values** makes the code easier to test and explain.

## Author
Mfon Joy, ND2 Mechatronics Engineering, YabaTech.
