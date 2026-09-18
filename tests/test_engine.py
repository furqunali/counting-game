import unittest
from random import Random
from counting_game_core.engine import CountingGameEngine

class CountingGameEngineTests(unittest.TestCase):
    def test_round_is_deterministic_with_seed(self):
        game = CountingGameEngine(1, 10, Random(7))
        target = game.new_round()
        result = game.guess(target)
        self.assertTrue(result.correct)
        self.assertTrue(game.is_finished())
        self.assertEqual(game.score(), 1000)

    def test_hints_and_attempt_count(self):
        game = CountingGameEngine(1, 10, Random(1))
        target = game.new_round()
        low = game.guess(target - 1)
        self.assertEqual(low.hint, "higher")
        self.assertEqual(low.attempts, 1)
        high = game.guess(target + 1)
        self.assertEqual(high.hint, "lower")

    def test_finished_round_rejects_more_guesses(self):
        game = CountingGameEngine(1, 2, Random(2))
        target = game.new_round()
        game.guess(target)
        with self.assertRaises(RuntimeError):
            game.guess(target)

if __name__ == "__main__":
    unittest.main()
