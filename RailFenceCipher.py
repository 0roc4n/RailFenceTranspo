def encrypt_rail_fence(plain_text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in plain_text:
        fence[rail].append(char)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    cipher_text = ''.join(''.join(rail) for rail in fence)
    return cipher_text

def decrypt_rail_fence(cipher_text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in cipher_text:
        fence[rail].append(None)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for rail in fence:
        for i in range(len(rail)):
            rail[i] = cipher_text[index]
            index += 1

    plain_text = ''
    rail = 0
    direction = 1

    for _ in range(len(cipher_text)):
        plain_text += fence[rail].pop(0)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return plain_text

def main():
    plain_text = input("Enter the plain text: ")
    rails = int(input("Enter the number of rails: "))

    cipher_text = encrypt_rail_fence(plain_text, rails)
    print("Encrypted text:", cipher_text)

    decrypted_text = decrypt_rail_fence(cipher_text, rails)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()