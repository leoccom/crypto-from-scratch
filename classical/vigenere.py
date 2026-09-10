def encrypt(plaintext: str, key: str) -> str:           # returns ciphertext
    shift_list = []
    key_length = len(key)

    for char1 in key:
        shift = ord(char1.upper()) - ord('A')
        shift_list.append(shift)

    result = []
    key_index = 0
    for char2 in plaintext:
        if char2.isupper():
            new_char = chr((ord(char2) - ord('A') + shift_list[key_index % key_length]) % 26 + ord('A'))
            key_index += 1
        elif char2.islower():
            new_char = chr((ord(char2) - ord('a') + shift_list[key_index % key_length]) % 26 + ord('a'))
            key_index += 1
        else:
            new_char = char2

        result.append(new_char)

    return ''.join(result)

def decrypt(ciphertext: str, key: str) -> str:           # returns plaintext
    shift_list = []
    key_length = len(key)

    for char1 in key:
        shift = ord(char1.upper()) - ord('A')
        shift_list.append(shift)

    result = []
    key_index = 0
    for char2 in ciphertext:
        if char2.isupper():
            new_char = chr((ord(char2) - ord('A') - shift_list[key_index % key_length]) % 26 + ord('A'))
            key_index += 1
        elif char2.islower():
            new_char = chr((ord(char2) - ord('a') - shift_list[key_index % key_length]) % 26 + ord('a'))
            key_index += 1
        else:
            new_char = char2

        result.append(new_char)

    return ''.join(result)


def kasiski_examine(ciphertext: str) -> list[int]:       # returns likely key-length guesses
    def find_repeated_sequence(ciphertext: str, seq_len: int=3) -> dict:
        """Returns {substring: [list of starting indices]} for substrings that repeat."""

        sequences = {}
        for i in range(len(ciphertext) - seq_len + 1):
            seq = ciphertext[i:i + seq_len]
            if seq.isalpha():
                if seq in sequences:
                    sequences[seq].append(i)
                else:
                    sequences[seq] = [i]

        return {seq: positions for (seq, positions) in sequences.items() if len(positions) > 1}


    sequences = find_repeated_sequence(ciphertext)

    def get_distances(sequences: dict) -> list:
        distances = []
        for (seq, positions) in sequences.items():
            for i in range(0, len(positions)-1):
                for j in range(i+1, len(positions)):
                    distances.append(positions[j] - positions[i])
        return distances

    
    def guess_key_length(distances: list, max_factor: int = 20, top_n: int = 5) -> list:
        factor_counts = {}

        for d in distances:
            for factor in [f for f in range(2, max_factor + 1) if d % f == 0]:
                if factor in factor_counts:
                    factor_counts[factor] += 1
                else:
                    factor_counts[factor] = 1

        # most common factors = most likely key lengths
        factor_sorted = sorted(factor_counts, key=factor_counts.get, reverse=True)[:top_n]
        return factor_sorted

    return guess_key_length(get_distances(sequences), max_factor=20, top_n=3)
            


print(kasiski_examine("Qn mje zwakfs’ inamhoko am Gllknhte, Aqrtvih yabvs pkta Dakpakfo tpd Fcrvglews mq qngsmkog c gaqsm vhtv htu tpkcx deyqrx cpigakgd. Mje Zjolv, ig vhx hoko oy vhx namg Kbpg Acmegt hh Dxpmttk, trpxcrl dum yien nhv sigad. Jokctbq dxeiwgs mq txnl aks ygleqw lvuwgnm, Rrbpcx Jafnem, cbhwt mje Zjolv’s trpxcrtpcx."))
