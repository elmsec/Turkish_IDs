import unittest
from turkish_ids import TurkishID


class TestTurkishIDMethods(unittest.TestCase):
    def setUp(self):
        self.t = TurkishID()

    def test_is_valid_tc_id_num(self):
        # 36779268334 is a random ID. Its validity guaranteed but
        # don't know whose ID it is.
        self.assertTrue(self.t.is_valid_tc_id_num('36779268334'))

    def test_is_valid_tc_id_num_with_id_not_eleven_character(self):
        self.assertFalse(self.t.is_valid_tc_id_num('3677926833'))

    def test_is_valid_tc_id_num_with_id_starting_with_zero(self):
        self.assertFalse(self.t.is_valid_tc_id_num('06779268334'))

    def test_guess_tc_id_number(self):
        self.assertEqual(self.t.guess_tc_id_number('367792683'), '36779268334')

    def test_guess_tc_id_number_with_complete_id(self):
        with self.assertRaises(ValueError):
            self.t.guess_tc_id_number('36779268334')

    def test_generate_valid_tc_ids(self):
        result = self.t.generate_valid_tc_ids(2, start='36779268334')
        self.assertListEqual(result, ['36779268334', '36779268402'])

    def test_find_relatives_tc_ids(self):
        # older
        result = self.t.find_relatives_tc_ids(2, '36779268334')
        self.assertListEqual(result, ['36782268260', '36785268106'])

        # younger
        result = self.t.find_relatives_tc_ids(2, '36779268334', younger=True)
        self.assertListEqual(result, ['36776268498', '36773268552'])

    def test_find_relatives_tc_ids_with_invalid_start(self):
        with self.assertRaises(ValueError):
            self.t.find_relatives_tc_ids(3, '36779268000')


if __name__ == '__main__':
    unittest.main()
