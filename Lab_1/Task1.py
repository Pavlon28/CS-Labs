def caesar_cipher(text, key, operation):
    # Ensure the key is within the allowed range
    if not (1 <= key <= 25):
        raise ValueError("Key must be between 1 and 25 inclusive.")

    # Prepare the text: convert to uppercase and remove spaces
    text = text.upper().replace(" ", "")

    # Define the alphabet based on Table 1
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alphabet)
    
    # Encrypt or decrypt the message
    result = ""
    for char in text:
        if char not in alphabet:
            raise ValueError("Text contains invalid characters. Use only letters A-Z.")
        
        # Find the original index of the character
        original_index = alphabet.index(char)
        
        if operation.lower() == "encrypt":
            # Apply encryption formula: c = ek(x) = x + k (mod n)
            new_index = (original_index + key) % n
        elif operation.lower() == "decrypt":
            # Apply decryption formula: m = dk(y) = y - k (mod n)
            new_index = (original_index - key) % n
        else:
            raise ValueError("Operation must be either 'encrypt' or 'decrypt'.")
        
        # Append the resulting character to the result
        result += alphabet[new_index]
    
    return result

# User input section
operation = input("Enter operation (encrypt/decrypt): ").strip()
key = int(input("Enter key (1-25): ").strip())
message = input("Enter your message: ").strip()

try:
    result = caesar_cipher(message, key, operation)
    print(f"Result: {result}")
except ValueError as e:
    print(e)
