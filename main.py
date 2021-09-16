#!/usr/bin/python
import sys
import argparse
import time

from turkish_ids import TurkishID

# ################################
# Eyup Can Elma - https://elma.dev
# Dec 22, 2018  - 11:52:05 PM
# ################################


def check_args(args=None):
    parser = argparse.ArgumentParser(
        description='Turkish ID Number Validator and Generator App',
        prefix_chars='-',
    )
    parser.add_argument(
        '-f', '--guess',
        metavar='123456789',
        help=(
            "Give a TC ID number without it's two rightmost digits then "
            "I'll guess the exact TC ID number according to the algorithm."
        ),
        type=str,
    )
    parser.add_argument(
        '-v', '--validate',
        metavar='12345678901',
        help=(
            "Validate a number to be sure that if it's a valid TC ID "
            "number or not."
        ),
        type=str,
    )
    parser.add_argument(
        '-g', '--generate',
        metavar='[1, ~]',
        help=(
            "Generate valid TC ID numbers up to the limit given with this. "
            "You must specify a sample TC ID number with --start-from "
            "or -s parameter to start generating new TC ID numbers from."
        ),
        type=int,
    )
    parser.add_argument(
        '-r', '--relatives',
        metavar='[1, ~]',
        help=(
            "Find the relatives' TC ID numbers according to the TC ID number "
            "given by the parameter -s/--start-from."
        ),
        type=int,
    )
    parser.add_argument(
        '-o', '--older',
        action='store_true',
        help=(
            "Tells -r/--relatives argument to search for older relatives."
        ),
    )
    parser.add_argument(
        '-y', '--younger',
        action='store_true',
        help=(
            "Tells -r/--relatives argument to search for younger relatives."
        ),
    )
    parser.add_argument(
        '-s', '--start-from',
        metavar='12345678901',
        help=(
            "Sample TC ID number to start generating new ones from. "
            "This has to be used with the -g/--generate parameter or the "
            "-r/--relatives parameter."
        ),
        type=str,
    )

    return parser.parse_args()


def main():
    turkish_id = TurkishID()
    argument = check_args(sys.argv[1:])
    if argument.validate:
        TC_ID = argument.validate
        v = 'a' if turkish_id.is_valid_tc_id_num(TC_ID) else 'NOT a'

        print('{tc_id} is {v} valid TC ID number.'.format(tc_id=TC_ID, v=v))
        return 0
    elif argument.generate:
        if not argument.start_from:
            print(
                'Please also specify a sample TC ID number as a start point '
                'with the -s or --start-from parameter '
                'so we can generate new ones from.'
                )
            return 2

        values = turkish_id.generate_valid_tc_ids(
            argument.generate, argument.start_from)
        print(*values, sep='\n')
        return 0
    elif argument.relatives:
        if not argument.start_from:
            print(
                'Please also specify a sample TC ID number as a start point '
                'with the -s or --start-from parameter '
                'so we can find the relatives from.'
            )
            return 2
        elif not argument.older and not argument.younger:
            print(
                'You must specify whether you want to search for the older '
                'relatives or the younger ones by using -o/--older or '
                '-y/--younger parameters.'
            )
            return 2
        values = turkish_id.find_relatives_tc_ids(
            limit=argument.relatives,
            start=argument.start_from,
            younger=argument.younger is True,
        )
        print(*values, sep='\n')
    elif argument.guess:
        if len(argument.guess) != 9:
            print('The length of the given number must be exactly 9 digits.')
            return 2

        result = turkish_id.guess_tc_id_number(argument.guess)
        print(result)
        return 0
    else:
        print('Huh. What am I supposed to do?')
        return 2


if __name__ == '__main__':
    start_time = time.time()
    result = main()
    end_time = time.time()

    print('Finished in {0:.2f} seconds.'.format(end_time-start_time))
    sys.exit(result)
