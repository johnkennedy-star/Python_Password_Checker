import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase and lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1

    # Digit check
    if re.search(r'\d', password):
        strength += 1

    # Special character check
    if re.search(r'[@$!%*?&]', password):
        strength += 1

    # Final evaluation
    if strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    else:
        return "Weak"

# Repetitive input loop
while True:
    pwd = input("Enter your password (or type 'exit' to quit): ")
    if pwd.lower() == 'exit':
        break
    result = check_password_strength(pwd)
    print(f"Password Strength: {result}")
