import unittest
from guard import sort_entry


class TestGuard(unittest.TestCase):

    def test_sort_entry(self):
        entry_list = [
            ["1518-11-01 00:05", "falls asleep"],
            ["1518-11-01 00:00", "Guard #10 begins shift"],
            ["1518-11-01 00:30", "falls asleep"],
            ["1518-11-01 00:25", "wakes up"]

        ]
        sorted_entry_list = [
            ["1518-11-01 00:00", "Guard #10 begins shift"],
            ["1518-11-01 00:05", "falls asleep"],
            ["1518-11-01 00:25", "wakes up"],
            ["1518-11-01 00:30", "falls asleep"]
        ]

        self.assertEqual(sort_entry(entry_list), sorted_entry_list)


if __name__ == '__main__':
    unittest.main()
