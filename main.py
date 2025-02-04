import random
import string
import pyperclip


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
    Generiert ein zufälliges Passwort.

    Parameter:
      - length: Länge des Passworts im String-Modus.
      - grouped: Wenn True, wird ein gruppiertes Passwort erstellt.
      - group_size: Anzahl der Zeichen pro Gruppe (nur im gruppierten Modus).
      - group_count: Anzahl der Gruppen (nur im gruppierten Modus).

    Rückgabe:
      - Das generierte Passwort als Zeichenkette.
    """
    if grouped:
        # Im gruppierten Modus werden ausschließlich Buchstaben verwendet.
        letters = string.ascii_letters
        total_length = group_size * group_count
        password_chars = [random.choice(letters) for _ in range(total_length)]
        groups = [''.join(password_chars[i * group_size:(i + 1) * group_size]) for i in range(group_count)]
        password = '-'.join(groups)
    else:
        # Im String-Modus werden Buchstaben, Ziffern und ausgewählte Sonderzeichen verwendet.
        normal_specials = "$%&"
        characters = string.ascii_letters + string.digits + normal_specials
        password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print_logo()  # Logo ausgeben

    while True:
        mode = input("Wähle den Modus: (g) gruppiert oder (s) string: ").lower()

        if mode == "g":
            try:
                group_count = int(input("Wie viele Gruppen soll das Passwort enthalten? "))
            except ValueError:
                print("Ungültige Eingabe. Es wird der Standardwert 3 verwendet.")
                group_count = 3

            # Im gruppierten Modus verwenden wir fest definierte 6 Zeichen pro Gruppe.
            password = generate_password(grouped=True, group_size=6, group_count=group_count)
            print("Dein Passwort lautet:\n\n", password, "\n")
            pyperclip.copy(password)
            print("Das Passwort wurde in die Zwischenablage kopiert.")

        elif mode == "s":
            try:
                length = int(input("Wie viele Zeichen soll das Passwort haben? "))
            except ValueError:
                print("Ungültige Eingabe. Es wird der Standardwert 12 verwendet.")
                length = 12

            password = generate_password(length=length, grouped=False)
            print("Dein Passwort lautet:\n\n", password, "\n")
            pyperclip.copy(password)
            print("Das Passwort wurde in die Zwischenablage kopiert.")

        else:
            print("Ungültige Eingabe. Bitte wähle 'g' für gruppiert oder 's' für string.")
            continue

        # Abfrage, ob ein weiteres Passwort generiert werden soll.
        another = input("Möchtest du ein weiteres Passwort generieren? (j/n): ").lower()
        if another != "j":
            print("Programm wird beendet.")
            break
