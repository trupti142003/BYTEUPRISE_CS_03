import sys

print("\t\t\t🎭 Welcome to Clown Caesar Cipher 🎭\n")

alpha = 'abcdefghijklmnopqrstuvwxyz'

def encryption(plain, shift):
    print("\t🔒 Encrypting message...")
    cipher = ""
    for char in plain:
        if char in alpha:
            pos = alpha.index(char)
            brapos = (pos + shift) % 26
            cipher += alpha[brapos]
        else:
            cipher += char
    print("\t🎉 Encryption successful!\n")
    print(f"\t🔒 Encrypted message: {cipher}\n")

def decryption(cipher, shift):
    print("\t🔓 Decrypting message...")
    plain = ""
    for char in cipher:
        if char in alpha:
            pos = alpha.index(char)
            brapos = (pos - shift) % 26
            plain += alpha[brapos]
        else:
            plain += char
    print("\t🎉 Decryption successful!\n")
    print(f"\t🔓 Decrypted message: {plain}\n")

finish = False
while not finish:
    cryption = input("\tType 'encrypt' for encryption, 'decrypt' for decryption:  \n")
    message = input("\tType your message: \n").lower()
    shift_no = int(input("\tType the shift number: \n"))

    if cryption == "encrypt":
        encryption(plain=message, shift=shift_no)

    elif cryption == "decrypt":
        decryption(cipher=message, shift=shift_no)

    again = input("Type 'yes' to play again, else 'no' to quit: \n")
    if again.lower() == "no":
        finish = True
        print("👋 Bye!\n")
        sys.exit()
