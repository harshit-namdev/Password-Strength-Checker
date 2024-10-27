import re
import random
import string

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    strength = check_password_strength(user_password)
    print(f"Password Strength: {strength}")

    if strength != "Strong":
        print("Consider using a stronger password. Here's a suggestion:")
        print(generate_password(12))
    else:
        print("Your Password is strong enough...")
