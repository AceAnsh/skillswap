import unittest

from app.credits import InsufficientCredits, Ledger
from app.matching import User, find_matches


class MatchingTests(unittest.TestCase):
    def test_mutual_match_ranks_first(self):
        a = User("a", "A", {"Python"}, {"C"})
        b = User("b", "B", {"C"}, {"Python"})
        c = User("c", "C", {"C"}, {"Java"})
        res = find_matches(a, [a, b, c])
        self.assertEqual([m.user.id for m in res], ["b", "c"])
        self.assertEqual(res[0].kind, "mutual")
        self.assertEqual(res[1].kind, "credit")

    def test_no_match(self):
        a = User("a", "A", {"Python"}, {"C"})
        d = User("d", "D", {"Go"}, {"Rust"})
        self.assertEqual(find_matches(a, [a, d]), [])


class LedgerTests(unittest.TestCase):
    def test_session_moves_credits(self):
        l = Ledger()
        l.register("t"); l.register("s")
        l.complete_session("t", "s", 30)
        self.assertEqual(l.balance("t"), 60)
        self.assertEqual(l.balance("s"), 0)

    def test_insufficient_credits(self):
        l = Ledger()
        l.register("t"); l.register("s")
        with self.assertRaises(InsufficientCredits):
            l.complete_session("t", "s", 45)


if __name__ == "__main__":
    unittest.main()
