import random
import string


def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?")

    remaining = [
        random.choice(
            string.ascii_letters +
            string.digits +
            "!@#$%^&*()-_=+[]{}|;:,.<>?"
        )
        for _ in range(length - 4)
    ]

    password_list = [lowercase, uppercase, digit, special] + remaining
    random.shuffle(password_list)

    return ''.join(password_list)


if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")