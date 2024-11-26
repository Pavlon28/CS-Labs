import random

# Permutarea inițială (IP) conform standardului DES
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

def text_to_bits(text):
    """Convertim un text în biți folosind ASCII."""
    return ''.join(f"{ord(c):08b}" for c in text)

def permute(input_bits, table):
    """Permutăm biții conform unui tabel dat."""
    return ''.join(input_bits[i - 1] for i in table)

def main():
    # Alegerea modului de intrare
    choice = input("Introduceți manual mesajul (M) sau generați aleatoriu (G)? ").strip().upper()
    if choice == "M":
        message = input("Introduceți mesajul (8 caractere): ")
        if len(message) != 8:
            print("Mesajul trebuie să conțină exact 8 caractere!")
            return
    elif choice == "G":
        message = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=8))
        print(f"Mesaj generat aleatoriu: {message}")
    else:
        print("Opțiune invalidă!")
        return

    # Convertim mesajul în biți
    message_bits = text_to_bits(message)
    print(f"Mesaj în biți: {message_bits}")

    # Aplicăm permutarea inițială (IP)
    permuted_bits = permute(message_bits, IP_TABLE)
    print(f"Biți după permutarea inițială (IP): {permuted_bits}")

    # Împărțim în L0 și R0
    L0, R0 = permuted_bits[:32], permuted_bits[32:]
    print(f"L0: {L0}")
    print(f"R0: {R0}")

    # Calculăm L1
    L1 = R0
    print(f"L1 (după prima iterație): {L1}")

if __name__ == "__main__":
    main()