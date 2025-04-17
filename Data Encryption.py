def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # shift and wrap around the alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Simple Caesar Cipher")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    if choice not in ('e', 'd'):
        print("Invalid option. Exiting.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift amount (e.g. 3): "))
    except ValueError:
        print("That's not a number. Exiting.")
        return

    if choice == 'e':
        transformed = encrypt(text, shift)
        print("Encrypted message:", transformed)
    else:
        transformed = decrypt(text, shift)
        print("Decrypted message:", transformed)

if __name__ == "__main__":
    main()
