def generate_permuted_alphabet(key2):
    # Create a list of unique characters in key2 while preserving order
    unique_chars = []
    for char in key2:
        if char not in unique_chars:
            unique_chars.append(char)
    
    # Create a permuted alphabet starting with key2's unique characters
    permuted_alphabet = unique_chars.copy()
    
    # Add remaining characters in alphabetical order
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if char not in permuted_alphabet:
            permuted_alphabet.append(char)
    
    return permuted_alphabet

def caesar_permutation_encrypt(message, k1, k2):
    message = message.upper()
    k2 = k2.upper()

    # Generate the permuted alphabet based on key2
    permuted_alphabet = generate_permuted_alphabet(k2)
    standard_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Create the shifted permuted alphabet based on key1
    shifted_permuted_alphabet = permuted_alphabet[k1:] + permuted_alphabet[:k1]
    
    # Create a mapping from the original permuted alphabet to the shifted one
    encryption_map = {standard_alphabet[i]: shifted_permuted_alphabet[i] for i in range(26)}
    
    # Encrypt the message
    encrypted_message = ''.join(encryption_map[char] if char in encryption_map else char for char in message)
    
    return encrypted_message

def caesar_permutation_decrypt(encrypted_message, k1, k2):
    encrypted_message = encrypted_message.upper()
    k2 = k2.upper()
    
    # Generate the permuted alphabet based on key2
    permuted_alphabet = generate_permuted_alphabet(k2)
    standard_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Create the shifted permuted alphabet based on key1
    shifted_permuted_alphabet = permuted_alphabet[k1:] + permuted_alphabet[:k1]
    
    # Create a mapping from the shifted permuted alphabet back to the original permuted one
    decryption_map = {shifted_permuted_alphabet[i]: standard_alphabet[i] for i in range(26)}
    
    # Decrypt the message
    decrypted_message = ''.join(decryption_map[char] if char in decryption_map else char for char in encrypted_message)
    
    return decrypted_message

def main():
    print("Welcome to the Caesar Cipher with Permutation Program!")
    while True:
        # Choose operation
        operation = input("Choose an operation (encrypt/decrypt/exit): ").strip().lower()
        
        if operation == 'encrypt':
            message = input("Enter the message to encrypt: ").strip()
            k1 = int(input("Enter the Caesar shift key (an integer between 0 and 25): ").strip())
            k2 = input("Enter the permutation key (a string of at least 7 unique letters): ").strip()
            
            if len(set(k2)) < 7 or not k2.isalpha():
                print("Invalid permutation key! It must be at least 7 unique letters.")
                continue
            
            encrypted_message = caesar_permutation_encrypt(message, k1, k2)
            print(f"Encrypted Message: {encrypted_message}")
        
        elif operation == 'decrypt':
            encrypted_message = input("Enter the message to decrypt: ").strip()
            k1 = int(input("Enter the Caesar shift key (an integer between 0 and 25): ").strip())
            k2 = input("Enter the permutation key (a string of at least 7 unique letters): ").strip()
            
            if len(set(k2)) < 7 or not k2.isalpha():
                print("Invalid permutation key! It must be at least 7 unique letters.")
                continue
            
            decrypted_message = caesar_permutation_decrypt(encrypted_message, k1, k2)
            print(f"Decrypted Message: {decrypted_message}")
        
        elif operation == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option! Please choose 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()