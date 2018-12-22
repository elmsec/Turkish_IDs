#!/usr/bin/python
import sys
import argparse

# ###############################
# Eyup Can Elma - https://elma.pw
# Dec 22, 2018 - 11:52:05 PM
# ###############################


def is_valid_tc_id(tc_id):
    """
    Checks that if the given number is a valid TC ID number or not.
    """
    tc_id = str(tc_id)

    # We need to be sure that
    # its first digit's greater than zero and
    # total of its digits is as much as eleven digits.
    if int(tc_id[0]) > 0 and len(tc_id) == 11:
        # Now we need to check the eleventh digit
        # Formula: n11 = (n1+n2+..+n10) mod 10
        eleventh_digit = sum(map(int, tc_id[0:10])) % 10
        if eleventh_digit == int(tc_id[10]):
            # Calculate the tenth digit...
            # Formula: n10 = ((n1+n3+n5+n7+n9)*7-(n2+n4+n6+n8)) mod 10
            tenth_digit = (sum(map(int, tc_id[:10:2])) * 7-(
                           sum(map(int, tc_id[1:9:2])))) % 10
            # ..and verify that if it's true or not
            return tenth_digit == int(tc_id[9])

    return False


def generate_valid_tc_ids(limit, start=11111111111, print_immediately=False):
    """
    By starting from the given number {start}, it generates new and valid
    TC IDs as much as you specified with the parameter {limit}.
    """
    tc_ids = []
    number = start
    while len(tc_ids) < limit:
        if is_valid_tc_id(number):
            tc_ids.append(number)

            if print_immediately:
                print('=>', number)

        number += 1
    return tc_ids


def check_args(args=None):
    parser = argparse.ArgumentParser(
        description='Turkish ID Number Validator and Generator App',
        prefix_chars='-',
    )
    parser.add_argument(
        '-v', '--validate',
        metavar='12345678901',
        help=(
            "Validate a number to be sure that if it's a valid TC ID "
            "number or not."
        ),
        type=int,
    )
    parser.add_argument(
        '-g', '--generate',
        metavar='[1, ~]',
        help=(
            "Generate valid TC ID numbers up to the limit given with this. "
            "You must specify a sample TC ID number with --start-from "
            "or -s parameter to start generating new TC ID numbers from."
        ),
        type=int
    )
    parser.add_argument(
        '-s', '--start-from',
        metavar='12345678901',
        help=(
            "Sample TC ID number to start generating new ones from. "
            "This has to be used with the -g/--generate parameter."
        ),
        type=int,
    )

    return parser.parse_args()


if __name__ == '__main__':
    all_args = check_args(sys.argv[1:])
    if all_args.validate:
        TC_ID = all_args.validate
        v = 'a' if is_valid_tc_id(TC_ID) else 'NOT'

        print('{tc_id} is {v} valid TC ID number.'.format(tc_id=TC_ID, v=v))
        sys.exit(0)
    elif all_args.generate:
        if not all_args.start_from:
            print(
                'Please also specify a sample TC ID number as a start point '
                'with the -s or --start-from parameter '
                'so we can generate new ones from.'
                )
            sys.exit(2)

        generate_valid_tc_ids(all_args.generate, all_args.start_from, True)
    else:
        print('Huh. What should I do?')
        sys.exit(2)
