#!/usr/bin/python
import sys
import argparse
import time

# ###############################
# Eyup Can Elma - https://elma.pw
# Dec 22, 2018 - 11:52:05 PM
# ###############################


def is_valid_tc_id_num(tc_id):
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


def guess_tc_id_number(tc_id, print_immediately=False):
    """
    Checks that if the given number is a valid TC ID number or not.
    """

    # We need to be sure that
    # its first digit's greater than zero and
    # total of its digits is as much as eleven digits.
    if int(tc_id[0]) > 0 and len(tc_id) == 9:
        tc_id = str(tc_id) + '00'

        # Calculate the tenth digit...
        # Formula: n10 = ((n1+n3+n5+n7+n9)*7-(n2+n4+n6+n8)) mod 10
        tenth_digit = (sum(map(int, tc_id[:10:2])) * 7-(
                       sum(map(int, tc_id[1:9:2])))) % 10

        new_tc_id = list(tc_id)
        new_tc_id[9] = str(tenth_digit)
        new_tc_id = ''.join(new_tc_id)

        # Now we need to check the eleventh digit
        # Formula: n11 = (n1+n2+..+n10) mod 10
        eleventh_digit = sum(map(int, new_tc_id[0:10])) % 10

        # otherwise, return the number with it's last two digits
        new_tc_id = list(new_tc_id)
        new_tc_id[10] = str(eleventh_digit)
        new_tc_id = ''.join(new_tc_id)

        if is_valid_tc_id_num(new_tc_id):
            if print_immediately:
                print(new_tc_id)
            return new_tc_id

    return False


def generate_valid_tc_ids(limit, start=11111111111, print_immediately=False):
    """
    By starting from the given number {start}, it generates new and valid
    TC ID numbers as much as you specified with the parameter {limit}.
    """
    if is_valid_tc_id_num(start) is False:
        print('Please use a real and valid TC ID number.')
        return 2

    tc_ids = []
    number = start
    while len(tc_ids) < limit:
        if is_valid_tc_id_num(number):
            tc_ids.append(number)

            if print_immediately:
                print('=>', number)

            number += 55
        number += 1
    return tc_ids if print_immediately is False else 0


def find_relatives_tc_ids(
        limit, start=None, relatives=0, print_immediately=False):
    """
    Finds TC ID numbers of the relatives according the given TC ID number.
    It can find the TC ID numbers of both the older relatives and the
    young ones.
    """
    if is_valid_tc_id_num(start) is False:
        print('Please use a real and valid TC ID number.')
        return 2

    tc_ids = []
    number = str(start)

    while len(tc_ids) < limit:
        part1, part2 = number[:9][:5], number[:9][5:]
        # Find younger relatives
        if relatives == 0:
            part1 = str(int(part1) - 3)
            part2 = str(int(part2) + 1)
        # Find older relatives
        else:
            part1 = str(int(part1) + 3)
            part2 = str(int(part2) - 1)

        # Check if it's a valid tc id number
        found_id_number = guess_tc_id_number(part1 + part2)

        # If so
        if found_id_number:
            # Append it to the list of the found ID numbers
            tc_ids.append(found_id_number)

            # Shall we print it right now? If so, do it
            if print_immediately:
                print('=>', found_id_number)

            # Don't forget to register new number so we can find new ones
            # according to it
            number = found_id_number

    # Return the whole list of the found TC ID numbers
    return tc_ids if print_immediately is False else 0


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
        )
    )
    parser.add_argument(
        '-s', '--start-from',
        metavar='12345678901',
        help=(
            "Sample TC ID number to start generating new ones from. "
            "This has to be used with the -g/--generate parameter or the "
            "-r/--relatives parameter."
        ),
        type=int,
    )

    return parser.parse_args()


def main():
    all_args = check_args(sys.argv[1:])
    if all_args.validate:
        TC_ID = all_args.validate
        v = 'a' if is_valid_tc_id_num(TC_ID) else 'NOT'

        print('{tc_id} is {v} valid TC ID number.'.format(tc_id=TC_ID, v=v))
        return 0
    elif all_args.generate:
        if not all_args.start_from:
            print(
                'Please also specify a sample TC ID number as a start point '
                'with the -s or --start-from parameter '
                'so we can generate new ones from.'
                )
            return 2

        return generate_valid_tc_ids(
            all_args.generate, all_args.start_from, True)
    elif all_args.relatives:
        if not all_args.start_from:
            print(
                'Please also specify a sample TC ID number as a start point '
                'with the -s or --start-from parameter '
                'so we can find the relatives from.'
            )
            return 2
        elif not all_args.older and not all_args.younger:
            print(
                'You must specify whether you want to search for the older '
                'relatives or the younger ones by using -o/--older or '
                '-y/--younger parameters.'
            )
            return 2
        return find_relatives_tc_ids(
            limit=all_args.relatives,
            start=all_args.start_from,
            relatives=1 if all_args.older else 0,
            print_immediately=True,
            )
    elif all_args.guess:
        if len(all_args.guess) != 9:
            print('The length of the given number must be exactly 9 digits.')
            return 2

        return guess_tc_id_number(all_args.guess, print_immediately=True)
    else:
        print('Huh. What should I do?')
        return 2


if __name__ == '__main__':
    start_time = time.time()
    m = main()
    end_time = time.time()

    print('Finished in {0:.2f} seconds.'.format(end_time-start_time))
    sys.exit(m)
