"""
I love when you f**k me rough and hard.
"""


import sys
import math
import datetime as dt


__all__ = tuple(["hours_to_meeting"])


def encrypt_file(file) -> 'encrypted_file':
    ...


def decrypt_file(file) -> 'decrypted_file':
    ...


def hours_to_meeting(finish: dt.date, start: dt.date = dt.datetime.now()) -> float:
    """
    Calculate the number of hours to next meeting.
    """
    return abs(finish - start).total_seconds() / 3600.0


def main() -> None:

    match len(sys.argv):
        case 2: # one date
            finish = dt.datetime.fromisoformat(sys.argv[1])
            hours = hours_to_meeting(finish)
            print(f"We will meet after {math.floor(hours)} hours.")
        case 3: # two dates
            print(sys.argv[1], sys.argv[2])
            # TODO
        case _:
            print("Pick a date and time in the future e.g. '2022-03-28T21:30:00'")
            # raise Exception("Bad input.")


if __name__ == "__main__":
    main()