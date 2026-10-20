alphabet = [' ', '.', ',', ':', ';', '!','?', '@', '$', '%', '^','&', '*','(',')','-','_', '+', '=', '/', '\\', '\'', '\"',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']
repeat = "y"

def cipher(text, shift, direction):
    text_list = []
    for char in text:
        if char in alphabet:
            if direction == 'encode':
                #len(alphabet) is used to flexibly add more characters to the alphabet
                # Modulo is used to describe the bring index back to cycle, when the letters would have either negative
                # shift, or would exceed len(alphabet).
                text_list.append(alphabet[(alphabet.index(char) + shift) % len(alphabet)])
            elif direction == 'decode':
                text_list.append(alphabet[(alphabet.index(char) - shift) % len(alphabet)])
        else:
            print("The input is not supported")
            return  # Exits the whole cipher function in case of unsupported characters.
    text_list = "".join(text_list)
    print(text_list)

while repeat == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    # Call the cipher function.
    cipher(text, shift, direction)
    # Ask to try again or close the program.
    repeat = input("Would you like to try again (y/n)?>")

