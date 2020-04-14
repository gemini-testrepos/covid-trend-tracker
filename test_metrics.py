import unittest
from metrics import DailyRecord, doubling_time_days, rolling_average


class TestMetrics(unittest.TestCase):
    def test_rolling_average(self):
        recs = [DailyRecord(f"2020-03-0{i}", i * 10) for i in range(1, 5)]
        self.assertEqual(rolling_average(recs, window=2), [10.0, 15.0, 25.0, 35.0])

    def test_doubling_time(self):
        self.assertAlmostEqual(doubling_time_days(10, 40, 6), 3.0)
