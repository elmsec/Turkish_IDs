#!/usr/bin/python

# ################################
# Eyup Can Elma - https://elma.dev
# Dec 22, 2018  - 11:52:05 PM
# ################################


class TurkishID:
    def is_valid_tc_id_num(self, tc_id: str) -> bool:
        """
        Checks that if the given number is a valid TC ID number or not.
        """
        if int(tc_id[0]) < 1 or len(tc_id) != 11:
            return False

        # Now we need to check the eleventh digit
        # Formula: n11 = (n1+n2+..+n10) mod 10
        eleventh_digit = sum(map(int, tc_id[0:10])) % 10
        if eleventh_digit != int(tc_id[10]):
            return False

        # Calculate the tenth digit...
        # Formula: n10 = ((n1+n3+n5+n7+n9)*7-(n2+n4+n6+n8)) mod 10
        tenth_digit = (sum(map(int, tc_id[:10:2])) * 7-(
                    sum(map(int, tc_id[1:9:2])))) % 10

        return tenth_digit == int(tc_id[9])

    def guess_tc_id_number(self, tc_id: str) -> str:
        """
        Check to see if the given number is a valid TC ID number or not.
        """
        if int(tc_id[0]) < 1 or len(tc_id) != 9:
            raise ValueError(
                'The given TC ID number must be 9 characters long')

        tc_id = tc_id + '00'

        # Calculate the tenth digit...
        # Formula: n10 = ((n1+n3+n5+n7+n9)*7-(n2+n4+n6+n8)) mod 10
        tenth_digit = (sum(map(int, tc_id[:10:2])) * 7-(
                    sum(map(int, tc_id[1:9:2])))) % 10
        new_tc_id = list(tc_id)
        new_tc_id[9] = str(tenth_digit)
        new_tc_id = ''.join(new_tc_id)

        # Check the eleventh digit
        # Formula: n11 = (n1+n2+..+n10) mod 10
        eleventh_digit = sum(map(int, new_tc_id[0:10])) % 10
        new_tc_id = list(new_tc_id)
        new_tc_id[10] = str(eleventh_digit)
        new_tc_id = ''.join(new_tc_id)

        if not self.is_valid_tc_id_num(new_tc_id):
            raise ValueError('The guessed TC ID number seems invalid.')

        return new_tc_id

    def generate_valid_tc_ids(self, limit, start: str) -> list:
        """
        By starting from the given number {start}, it generates new and valid
        TC ID numbers as much as you specified with the parameter {limit}.
        """
        if self.is_valid_tc_id_num(start) is False:
            raise ValueError(
                'Please use a real and valid TC ID number for the parameter '
                '<start>.')

        tc_ids = []
        number = int(start)
        while len(tc_ids) < limit:
            if self.is_valid_tc_id_num(str(number)):
                tc_ids.append(str(number))
                number += 55
            number += 1
        return tc_ids

    def find_relatives_tc_ids(self, limit, start: str, younger=False) -> list:
        """
        Find TC ID numbers of the relatives according to the given TC ID no.
        This can find TC ID numbers of both the older and younger relatives.
        """
        if self.is_valid_tc_id_num(start) is False:
            raise ValueError('Please use a valid TC ID number.')

        tc_ids = []
        number = start

        while len(tc_ids) < limit:
            part1, part2 = number[:9][:5], number[:9][5:]
            # Find younger relatives
            if younger is True:
                part1 = str(int(part1) - 3)
                part2 = str(int(part2) + 1)
            # Find older relatives
            else:
                part1 = str(int(part1) + 3)
                part2 = str(int(part2) - 1)

            possible_relative = self.guess_tc_id_number(part1 + part2)
            if possible_relative:
                tc_ids.append(possible_relative)
                number = possible_relative

        return tc_ids
