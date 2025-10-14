print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\bWorld")



# ### 🧵 Python Escape Sequences Table
#
# | Escape Sequence | Meaning                          | Example Code                    | Output                        |
# |-----------------|----------------------------------|----------------------------------|-------------------------------|
# | `\n`           | New line                         | `print("Hello\nWorld")`        | Hello<br>World                |
# | `\t`           | Horizontal tab                   | `print("Hello\tWorld")`        | Hello World                   |
# | `\\`           | Backslash                        | `print("C:\bUsers")`           | C:\Users                      |
# | `\'`           | Single quote                     | `print('It\'s fine')`          | It's fine                     |
# | `\"`           | Double quote                     | `print("She said: \\"Hi\\"")`  | She said: "Hi"                |
# | `\r`           | Carriage return                  | `print("Hello\rWorld")`        | World                         |
# | `\b`           | Backspace                        | `print("Hell\bo")`             | Helo                          |
# | `\f`           | Form feed                        | `print("Hello\fWorld")`        | HelloWorld                   |
# | `\a`           | Bell (alert sound)               | `print("\a")`                  | (May trigger a beep)          |
# | `\v`           | Vertical tab                     | `print("Hello\vWorld")`        | HelloWorld                   |
# | `\N{name}`     | Unicode character by name        | `print("\N{Greek Capital Letter Omega}")` | Ω              |
# | `\uXXXX`       | Unicode character (16-bit hex)   | `print("\u03A9")`              | Ω                             |
# | `\UXXXXXXXX`   | Unicode character (32-bit hex)   | `print("\U0001F600")`          | 😀                            |
# | `\xXX`         | Character with hex value         | `print("\x41")`                | A                             |
