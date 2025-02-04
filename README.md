# Password Generator

This program generates random passwords and offers two modes:

- **Grouped Mode (g):**  
  Generates a password divided into several groups (default: 6 characters per group).  
  Example: `ABCdef-GHIjkl-MNOprs`

- **String Mode (s):**  
  Generates a continuous password string with a user-defined length.

After generating the password, it is automatically copied to the clipboard using `pyperclip`.

## Required Libraries

- **Python 3**  
  Make sure Python 3 is installed.

- **pyperclip**  
  Used to copy the password to the clipboard.

  Install via pip:
  ```bash
  pip install pyperclip
