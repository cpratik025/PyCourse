import unittest
import new_random_game
import script

class Test_rand(unittest.TestCase):
    def test_random(self):
        answer = 5
        guess = 5
        result=script.new_random_game(answer,guess)
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()