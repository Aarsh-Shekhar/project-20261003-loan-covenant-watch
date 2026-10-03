import unittest

from loan_covenant_watch.models import Record
from loan_covenant_watch.scoring import rank_records, score_record, summarize


class ScoringTests(unittest.TestCase):
    def test_score_is_bounded(self):
        record = Record(id="x", exposure=50000, signal=0.7, urgency=6)
        self.assertGreater(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)

    def test_ranking_orders_highest_first(self):
        low = Record(id="low", exposure=1000, signal=0.1, urgency=1)
        high = Record(id="high", exposure=90000, signal=0.9, urgency=9)
        ranked = rank_records([low, high])
        self.assertEqual(ranked[0][0].id, "high")

    def test_summary_reports_count(self):
        records = [Record(id="a", exposure=1000, signal=0.2, urgency=2)]
        self.assertEqual(summarize(records)["count"], 1)


if __name__ == "__main__":
    unittest.main()
