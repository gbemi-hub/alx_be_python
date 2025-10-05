def safe_divide(numerator, denominator){
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator/denominator
    expect ZeroDivisionError:
        print("you cannot divide by zero")
    expect ValueError:
        print("Enter a valid value")
    else :
        print(f"division result is {result}")
    finally :
        print(f"division complete")