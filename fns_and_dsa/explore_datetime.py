from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date):
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if _name_ == "_main_":
    main()

# Got it 👍 Let me explain it very simply, like step by step, with no technical jargon at first:


# ---

# 📝 What this program does

# 1. First, it tells you today’s date and time (like looking at your phone’s clock).
# Example: 2025-09-27 14:30:12


# 2. Then, it asks you:
# 👉 “How many days do you want me to add to today’s date?”

# If you type 10, it will tell you what the date will be 10 days from today.

# If you type 2, it will tell you the date 2 days from today.

# (If you type a negative number, it can even tell you what the date was in the past.)





# ---

# 💡 How it works inside the code

# 1. datetime.now() → Think of it like a camera taking a snapshot of the current date and time.
# Example: it “captures” 2025-09-27 14:30:12.


# 2. strftime("%Y-%m-%d %H:%M:%S") → This just makes the date look nice and readable.

# %Y = Year

# %m = Month

# %d = Day

# %H:%M:%S = Hours:Minutes:Seconds


# So instead of a messy computer format, you see:
# 2025-09-27 14:30:12


# 3. timedelta(days=number) → Think of this as a little box that stores “extra days.”

# If you say 10, the box stores 10 days.

# Then we add that box of days to today’s date.


# Example:
# Today = 2025-09-27
# Box = +10 days
# Result = 2025-10-07


# 4. The program finally shows you the future date.




# ---

# 🖥 Example run

# Current date and time: 2025-09-27 14:30:12
# Enter the number of days to add to the current date: 10
# Future date: 2025-10-07


# ---

# 👉 In short:
# This program is like a calendar helper. You give it today’s date (the computer already knows it), and then you tell it how many days to jump forward. It will then show you the new date.


# ---

# Would you like me to also draw a little diagram (calendar style) to show how the “jumping days” part works?

