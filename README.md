# Vigenère Cipher Command-Line Tool

This project provides a simple command-line interface for encrypting and
decrypting text using the classic **Vigenère cipher**. 
It supports direct text input as well as reading plaintext, ciphertext,
or keys from files.

------------------------------------------------------------------------

## Files in This Project

### **vigenere.py**

The main CLI wrapper that: 
- Parses command-line arguments.
- Reads plaintext/ciphertext/key from arguments or files.
- Calls `encrypt()` or `decrypt()` from `methods.py`.
- Performs error handling for incorrect usage.

### **methods.py**

Contains the core Vigenère cipher logic:
- `encrypt(plaintext, key)`: to encrypt plaintext message(s).
- `decrypt(cipher, key)`: to decrypt cipher message(s).
- `_repeat_key(text, key)`: helper method to match key length with plaintext/cipher.

------------------------------------------------------------------------

## Usage

You can encrypt or decrypt text by providing the appropriate flags:

### **Basic Commands**

``` bash
python vigenere.py --key KEY/FILE --encrypt PLAINTEXT/FILE
python vigenere.py --key KEY/FILE --decrypt CIPHERTEXT/FILE
```

### **Using Files as Inputs**

``` bash
python vigenere.py --key key.txt --encrypt message.txt
python vigenere.py --key key.txt --decrypt cipher.txt
```

### **Short Flags**

``` bash
python vigenere.py -k KEY/FILE -e PLAINTEXT/FILE
python vigenere.py -k KEY/FILE -d CIPHERTEXT/FILE
```

------------------------------------------------------------------------

## Examples

### Encrypting:

``` bash
python vigenere.py -k "SECRET" -e "HELLO WORLD"
```

### Decrypting:

``` bash
python vigenere.py -k "SECRET" -d "RIJVS UYVJN"
```

------------------------------------------------------------------------

## Vigenère Cipher Logic

-   Encryption:
    `En = (Pn + Kn) mod 26`
-   Decryption:
    `Pn = (En - Kn) mod 26`

Non‑alphabetical characters are preserved.

------------------------------------------------------------------------

## Notes

-   Keys can be uppercase or lowercase.
-   Key repeats automatically to match the length of the text.
-   Files are read if the input path exists.
-   Outputs are printed directly to the terminal.
