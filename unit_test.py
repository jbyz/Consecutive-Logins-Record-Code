import unittest
from datetime import datetime
import pandas as pd
from functions import (
    string_list_to_filtered_date_list,
    find_logins_start_end_length,
    tabulate_login_data,
)


class TestStringListToFilteredDateList(unittest.TestCase):
    def test_string_list_to_filtered_date_list_valid_list(self):
        # Test valid input
        input_data = ['2023-08-18 13:04:53', '2023-09-18 12:04:53', '2023-09-11 13:04:53']
        result = string_list_to_filtered_date_list(input_data)
        expected = [datetime(2023, 8, 18).date(), datetime(2023, 9, 18).date(), datetime(2023, 9, 11).date()]
        self.assertEqual(result, expected)

    def test_string_list_to_filtered_date_list_invalid_input(self):
        # Test invalid input
        input_data = '2023-08-18 13:04:53'
        with self.assertRaises(ValueError):
            string_list_to_filtered_date_list(input_data)

    def test_string_list_to_filtered_date_list_mixed_list(self):
        # Test list with invalid and valid strings
        input_data = ['2023-09-14 00:04:53', 'asdasd', '2023-09-22 11:04:53', '2023-07-25 02:04:53', 'asdasd']
        result = string_list_to_filtered_date_list(input_data)
        expected = [datetime(2023, 9, 14).date(), datetime(2023, 9, 22).date(), datetime(2023, 7, 25).date()]
        self.assertEqual(result, expected)


class TestFindLoginsStartEndLength(unittest.TestCase):
    def test_find_logins_start_end_length(self):
        # Test with a list of dates
        date_list = [datetime(2023, 7, 21).date(), datetime(2023, 8, 23).date(), datetime(2023, 8, 24).date(),
                     datetime(2023, 8, 25).date(), datetime(2023, 9, 27).date(), datetime(2023, 9, 28).date()]
        start_date, end_date, length_no = find_logins_start_end_length(date_list)
        expected_start_date = [datetime(2023, 7, 21).date(), datetime(2023, 8, 23).date(), datetime(2023, 9, 27).date()]
        expected_end_date = [datetime(2023, 7, 21).date(), datetime(2023, 8, 25).date(), datetime(2023, 9, 28).date()]
        expected_length_no = [1, 3, 2]
        self.assertEqual(start_date, expected_start_date)
        self.assertEqual(end_date, expected_end_date)
        self.assertEqual(length_no, expected_length_no)

    def test_find_logins_start_end_length(self):
        # Test with duplicate dates
        date_list = [datetime(2023, 7, 21).date(), datetime(2023, 8, 23).date(), datetime(2023, 8, 24).date(),
                     datetime(2023, 8, 25).date(), datetime(2023, 9, 27).date(), datetime(2023, 9, 27).date()]
        start_date, end_date, length_no = find_logins_start_end_length(date_list)
        expected_start_date = [datetime(2023, 7, 21).date(), datetime(2023, 8, 23).date(), datetime(2023, 9, 27).date()]
        expected_end_date = [datetime(2023, 7, 21).date(), datetime(2023, 8, 25).date(), datetime(2023, 9, 27).date()]
        expected_length_no = [1, 3, 1]
        self.assertEqual(start_date, expected_start_date)
        self.assertEqual(end_date, expected_end_date)
        self.assertEqual(length_no, expected_length_no)


class TestTabulateLoginData(unittest.TestCase):
    def test_tabulate_login_data(self):
        # Test with lists of start dates, end dates, and lengths to see if table matches
        start_date_list = [datetime(2023, 7, 21).date(), datetime(2023, 7, 25).date()]
        end_date_list = [datetime(2023, 7, 24).date(), datetime(2023, 7, 26).date()]
        length_no_list = [4, 2]
        result = tabulate_login_data(start_date_list, end_date_list, length_no_list)
        expected = pd.DataFrame({
            'START': [datetime(2023, 7, 21).date(), datetime(2023, 7, 25).date()],
            'END': [datetime(2023, 7, 24).date(), datetime(2023, 7, 26).date()],
            'LENGTH': [4, 2]
        })
        self.assertTrue(result.equals(expected))


if __name__ == '__main__':
    unittest.main()
