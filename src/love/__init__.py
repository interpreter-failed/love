# -*- coding: utf-8 -*-

"""
I love when you f**k me rough and hard.
"""

import sys
import math
import datetime as dt
from typing import IO, TextIO, BinaryIO

from cryptography.fernet import Fernet


__all__ = tuple(["hours_to_meeting"])


# ############################################################################
# Message encryption and decryption with symmetric key.
# ############################################################################

def encrypt_message(key: bytes, message: BinaryIO) -> bytes:
    return Fernet(key).encrypt(message)


def decrypt_message(key: bytes, message: BinaryIO) -> bytes:
    return Fernet(key).decrypt(message)


def demo1():
    with open("./letters/letter-2022-04-01.md", encoding="utf-8") as file:
        key = Fernet.generate_key()

        # Read the key.
        print(f"KEY: {key}")

        # Encrypt the letter.
        encrypted = encrypt_message(key, str.encode(file.read()))
        print(f"ENCRYPTED: {encrypted}")

        # Decrypt the letter.
        decrypted = decrypt_message(key, encrypted).decode()
        print(f"DECRYPTED: {decrypted}")


def demo2(): # AES
    import secrets
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    # Generate a random secret key (AES256 needs 32 bytes)
    key = secrets.token_bytes(32)

    # Encrypt a message
    nonce = secrets.token_bytes(12)  # GCM mode needs 12 fresh bytes every time
    ciphertext = nonce + AESGCM(key).encrypt(nonce, b"Message", b"")

    # Decrypt (raises InvalidTag if using wrong key or corrupted ciphertext)
    msg = AESGCM(key).decrypt(ciphertext[:12], ciphertext[12:], b"")

    print(msg)


def letters_main():
    demo1()
    demo2()


# ############################################################################
# Meeting date/time calculations.
# ############################################################################

def hours_to_meeting(finish: dt.date, start: dt.date = dt.datetime.now()) -> float:
    """
    Calculate the number of hours to next meeting.
    """
    return abs(finish - start).total_seconds() / 3600.0


def meeting_main() -> None:
    match len(sys.argv):
        case 2: # one date
            finish = dt.datetime.fromisoformat(sys.argv[1])
            hours = hours_to_meeting(finish)
            print(f"We will meet in {math.floor(hours)} hours.")
        case 3: # two dates
            print(sys.argv[1], sys.argv[2])
            # TODO
        case _:
            print("Pick a date and time in the future e.g. '2022-03-28T21:30:00'")
            # raise Exception("Bad input.")
