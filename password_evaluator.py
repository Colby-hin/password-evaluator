print("Welcome to Colbys Password Strength Evaluator!")

# Here we define a list of example passwords to evaluate.

passwords = [
    "123456",
    "admin",
    "password123!",
    "qwerty",
    "Str0ngP@ssw0rd!",
    "hunter2",
    "letmein123",
    "gu3st$ecure"
]

# This function checks if the password has at least 8 characters.
# It takes one argument (pwd), and returns True if it's long enough.

def is_min_length(pwd):
    if len(pwd) >= 8:
        return True
    else:
        return False

# We are calling the function with "admin" to check its length.
# The result will be False, since "admin" has fewer than 8 characters.

print('"admin" is long enough?', is_min_length("admin"))

# This function evaluates whether a password is "strong" based on common security criteria.
# A strong password must:
# - Be at least 8 characters long
# - Contain at least one uppercase letter (A-Z)
# - Contain at least one lowercase letter (a-z)
# - Contain at least one digit (0-9)
# - Contain at least one special character (from a selected set: !@#$%^&*()_+-=)

def is_strong_password(pwd):
    if len(pwd) < 8:
        return False
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in "!@#$%^&*()_+-=" for c in pwd)
    return has_upper and has_lower and has_digit and has_special


print("\nEvaluating passwords:\n")
# Loop through each password in the list
for pwd in passwords:
    if is_strong_password(pwd):
        # Strong password meets all criteria
        print(f"{pwd:<15} is STRONG")
    elif is_min_length(pwd):
        # Long enough but missing complexity
        print(f"{pwd:<15} is WEAK (long enough, but missing character types)")
    else:
        # Too short to be considered secure
        print(f"{pwd:<15} is VERY WEAK (too short)")

# This function counts how many passwords are strong, weak, or very weak
def summary(passwords):
    # Initialize counters
    strong = weak = very_weak = 0

    # Loop through each password and categorize
    for pwd in passwords:
        if is_strong_password(pwd):
            strong += 1
        elif is_min_length(pwd):
            weak += 1
        else:
            very_weak += 1

    # Print out the results
    print(f"\n Summary:")
    print(f"Strong passwords    : {strong}")
    print(f"Weak passwords      : {weak}")
    print(f"Very weak passwords: {very_weak}")

# This line executes the summary function using the list of passwords

summary(passwords)
