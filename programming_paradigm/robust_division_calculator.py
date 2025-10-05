def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"te result of the division is {result}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else :
        print(f"The result o the division is {result:.1f}")
    finally :
        print("division complete")
