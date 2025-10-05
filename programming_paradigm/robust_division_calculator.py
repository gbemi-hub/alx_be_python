def safe_divide(numerator, denominator){
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator/denominator
    expect ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    expect ValueError:
        print("Error:The value is not valid")
    else :
        print(f"division result is {result}")
    finally :
        print(f"division complete")