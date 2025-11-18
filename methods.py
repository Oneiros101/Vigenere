# Vigenere equation:
# En = (Pn + Kn) * mod26
# Dn = (En - Kn) * mod26

# Pn: decimal number of an nth plaintext char
# Kn: decimal number of an nth key char

# Encryption steps:
# -----------------
# 1. "Plain" char into decimal (Pn)
# 2. "Key" char into decimal (Kn)
# 3.  Pn + Kn = We get "En" in decimal
# 4. "En" decimal into char

# Decryption steps:
# -----------------
# 1. "Cipher" char into decimal (Pn)
# 2. "Key" char into decimal (Kn)
# 3.  Pn - Kn = We get "En" in decimal
# 4. "En" decimal into char

ALPHABET_SIZE = 26

def encrypt(plaintext, key):
    cipher = ""
    REPEATED_KEY = _repeat_key(plaintext, key)

    for plain_char, key_char in zip(plaintext, REPEATED_KEY):
        # In case of any non alphabetical chars
        if not plain_char.isalpha():
            cipher += plain_char
        else:
            if plain_char.isupper():
                base = ord("A")
            else:
                base = ord("a")

            plain_char_num = ord(plain_char) - base
            key_char_num = ord(key_char.upper()) - ord("A")
            enc_num = (plain_char_num + key_char_num) % ALPHABET_SIZE
            encrypted_char = chr(enc_num + base)
            cipher += encrypted_char

    print(f"Plaintext --> {plaintext}")
    print(f"Cipher -----> {cipher}")


def decrypt(cipher, key):
    plaintext = ""
    REPEATED_KEY = _repeat_key(cipher, key)

    for cipher_char, key_char in zip(cipher, REPEATED_KEY):
        if not cipher_char.isalpha():
            plaintext += cipher_char
        else:
            if cipher_char.isupper():
                base = ord("A")
            else:
                base = ord("a")

            cipher_char_num = ord(cipher_char) - base
            key_char_num = ord(key_char.upper()) - ord("A")
            plain_char_num = (cipher_char_num - key_char_num) % ALPHABET_SIZE
            decrypted_char = chr(plain_char_num + base)
            plaintext += decrypted_char

    print(f"Cipher ------> {cipher}")
    print(f"Plaintext ---> {plaintext}")

# Helper method to repeat key along plaintext length
# plaintext ----> "something is about to happen", key = "sun"
# repeated_key -> "sunsunsun su nsuns un sunsun" 
def _repeat_key(text, key):
    repeated_key = ""
    KEY_LENGTH = len(key)
    key_index = 0

    for letter in text:
        if not letter.isalpha():
            repeated_key += letter
        else:
            repeated_key += key[key_index % KEY_LENGTH]
            key_index += 1

    return repeated_key

