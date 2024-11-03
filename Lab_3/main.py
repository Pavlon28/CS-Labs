# Mapping Romanian alphabet with 31 letters
romanian_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZĂÂÎȘȚ"
alphabet_map = {char: idx for idx, char in enumerate(romanian_alphabet)}
reverse_alphabet_map = {idx: char for char, idx in alphabet_map.items()}
alphabet_length = len(romanian_alphabet)

def prepare_text(text):
    return ''.join(char.upper() for char in text if char.isalpha())

def vigenere_encrypt(plain_text, key):
    plain_text = prepare_text(plain_text)
    key = prepare_text(key)
    encrypted_text = []
    for i, char in enumerate(plain_text):
        plain_idx = alphabet_map[char]
        key_idx = alphabet_map[key[i % len(key)]]
        encrypted_idx = (plain_idx + key_idx) % alphabet_length
        encrypted_text.append(reverse_alphabet_map[encrypted_idx])
    return ''.join(encrypted_text)

def vigenere_decrypt(cipher_text, key):
    cipher_text = prepare_text(cipher_text)
    key = prepare_text(key)
    decrypted_text = []
    for i, char in enumerate(cipher_text):
        cipher_idx = alphabet_map[char]
        key_idx = alphabet_map[key[i % len(key)]]
        decrypted_idx = (cipher_idx - key_idx) % alphabet_length
        decrypted_text.append(reverse_alphabet_map[decrypted_idx])
    return ''.join(decrypted_text)

def main_loop():
    while True:
        print("\nVigenere Cipher Program")
        print("1) Encrypt")
        print("2) Decrypt")
        print("3) Exit")

        choice = input("Select an option (1/2/3): ").strip()

        if choice == "1":
            key = input("Enter the key (minimum 7 characters): ").strip()
            text = input("Enter the text to encrypt: ").strip()

            if len(prepare_text(key)) < 7:
                print("Error: Key must be at least 7 characters.")
            else:
                encrypted_text = vigenere_encrypt(text, key)
                print("Encrypted Text:", encrypted_text)

        elif choice == "2":
            key = input("Enter the key (minimum 7 characters): ").strip()
            text = input("Enter the text to decrypt: ").strip()

            if len(prepare_text(key)) < 7:
                print("Error: Key must be at least 7 characters.")
            else:
                decrypted_text = vigenere_decrypt(text, key)
                print("Decrypted Text:", decrypted_text)

        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the main loop
main_loop()