def safe_divide(x, y){
    try:
        result = x/y
    expect ZeroDivisionError:
        print("you cannot divide by zero")
    expect ValueError:
        print("Enter a valid value")
    else :
        print(f"division result is {result}")
    finally :
        print(f"division complete")