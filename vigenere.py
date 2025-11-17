#!/usr/bin/env python3

import os
import argparse
from methods import encrypt, decrypt

PROG = "python vigenere.py"
DESCRIPTION = "Vigenere cipher command-line tool"
USAGE = f"{PROG} [-e/--encrypt | -d/--decrypt] <PLAINTEXT/CIPHER/FILE> [-k/--key] KEY/FILE"
EPILOG = """
Example of usage:
    python vigenere.py --key KEY/FILE --encrypt PLAINTEXT/FILE
    python vigenere.py --key KEY/FILE--decrypt CIPHER/FILE
    python vigenere.py -k KEY/FILE -e PLAINTEXT/FILE 
    python vigenere.py -k KEY/FILE -d CIPHER/FILE

"""

def _read_file_if_exists(text):
    if os.path.isfile(text):
        try:
            with open(text, "r") as file:
                return file.read().rstrip("\n")
        except Exception:
            return None
    return text


def main():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        prog=PROG,
        formatter_class=argparse.RawTextHelpFormatter,
        usage=USAGE,
        epilog=EPILOG
    )

    parser.add_argument("-k", "--key", type=str, help="Key to be used for encryption/decryption or a file")
    parser.add_argument("-e", "--encrypt", type=str, help="Plaintext to be encrypted or a file")
    parser.add_argument("-d", "--decrypt", type=str, help="Cipher to be decrypted or a file")

    args = parser.parse_args()

    # When encryption and decryption are mentioned at the same time
    if args.encrypt and args.decrypt:
        print("Error: cannot use both -e/--encrypt and -d/--decrypt at the same time.")
        return

    # When key argument is empty
    if not args.key:
        print("Error: Key is required for both encryption/decryption")
        return

    # When key file is empty
    key = _read_file_if_exists(args.key)
    if not key:
        print(f"Error: Key file {args.key} is empty")
        return

    # Process encryption
    if args.encrypt:
        plaintext = _read_file_if_exists(args.encrypt)
        if not plaintext:
            print(f"Error: Plaintext file {args.encrypt} is empty")
            return
        encrypt(plaintext, key)

    # Process decryption
    elif args.decrypt:
        cipher = _read_file_if_exists(args.decrypt)
        if not cipher:
            print(f"Error: Cipher file {args.decrypt} is empty")
            return
        decrypt(cipher, key)


if __name__ == "__main__":
    main()
