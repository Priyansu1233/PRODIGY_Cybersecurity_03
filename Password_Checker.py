import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    print("\n Password Analysis:")
    print("✔ Length:", length)
    print("✔ Contains uppercase:", has_upper)
    print("✔ Contains lowercase:", has_lower)
    print("✔ Contains number:", has_digit)
    print("✔ Contains special character:", has_special)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if score < 2:
        return "❌ Weak"
    elif score >= 3:
        if length >= 8:
            return "✅ Strong" if score == 4 else "⚠️ Moderate"
        elif length >= 6:
            return "⚠️ Moderate"
        else:
            return "❌ Weak"
    else:
        return "❌ Weak"

def main():
    print("=== Password Complexity Checker ===")
    password = input("Enter a password to test: ")
    result = check_password_strength(password)
    print("\nPassword Strength:", result)

if __name__ == "__main__":
    main()
