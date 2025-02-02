import random
import string


def print_logo():
    logo = r"""
                                           _                                     _             
 _ __   __ _ ___ _____      _____  _ __ __| |     __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |    / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |   | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
| .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|____\__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
|_|                                        |_____|___/                                                                                                                                                                                       
    """
    print(logo)


def generate_password(length=12, grouped=False, group_size=6, group_count=3):
    """
    Generates a random password.

    Parameters:
      - length: The length of the password if not grouped.
      - grouped: If True, the password is generated in groups.
      - group_size: Number of characters per group (only when grouped=True).
      - group_count: Number of groups (only when grouped=True).

    Returns:
      - The generated password as a string.
    """
    if grouped:
        # Use only letters for grouped passwords
        letters = string.ascii_letters
        total_length = group_size * group_count
        password_chars = [random.choice(letters) for _ in range(total_length)]
        groups = [''.join(password_chars[i * group_size:(i + 1) * group_size]) for i in range(group_count)]
        password = '-'.join(groups)
    else:
        # Use letters, digits and normal special characters for non-grouped passwords.
        normal_specials = "$%&"
        characters = string.ascii_letters + string.digits + normal_specials
        password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    print_logo()  # Logo ausgeben

    option = input("Soll das Passwort gruppiert werden (Format: xxxxxx-xxxxxx-xxxxxx)? (j/n): ").lower()
    if option == "j":
        print("Dein Passwort lautet:", generate_password(grouped=True))
    else:
        try:
            length = int(input("Gib die Passwortlänge ein: "))
            print("Dein Passwort lautet:", generate_password(length=length))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
