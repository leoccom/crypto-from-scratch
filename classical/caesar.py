from curses.ascii import islower, isupper


def encrypt(plaintext: str, shift: int) -> str:        # returns ciphertext
    """Caesar cipher encryption
    """
    result = []

    for char in plaintext:
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = char
        result.append(new_char)

    return ''.join(result)


def decrypt(ciphertext: str, shift: int) -> str:        # returns plaintext
    """Caesar cipher decryption
    """
    result = []

    for char in ciphertext:
        if char.isupper():
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            new_char = char
        result.append(new_char)

    return ''.join(result)


def brute_force(ciphertext: str) -> list[tuple[int, str]]:  # returns all (shift, decoded_text) pairs
    """Caesar cipher brute force
    """

    possible_texts = []

    for i in range(26):
        possible_texts.append((i, decrypt(ciphertext, i)))

    return possible_texts
    
print(brute_force("Uv, zl anzr vf Oevna. Avpr gb zrrg lbh!"))