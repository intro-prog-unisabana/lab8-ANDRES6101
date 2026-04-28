"""Laboratorio 8 - Problema 1.


Implementa una CLI que calcule carga por punto de soporte.
"""

import sys

try:
    
    if len(sys.argv) != 3:
        print("Error: Invalid input! Enter numeric values only.")
    else:
        total_load = float(sys.argv[1])
        num_supports = float(sys.argv[2])

        if num_supports == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
        else:
            load_per_support = total_load / num_supports
            print(f"Load per support point: {load_per_support:.2f} N")

except ValueError:
    print("Error: Invalid input! Enter numeric values only.")