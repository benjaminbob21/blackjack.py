from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userblackj_dealerbust(self, input_mock, randint_mock):
        '''
        The user receives cards equal to 21 and blackjacks while dealer receives cards greater than 21 and busts. 
        The user wins since the dealer bust and user has a blackjack.
        '''
        output = run_test([1, 11], [], [8, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a Jack\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 5\n" \
                   "Dealer has 13.\n" \
                   "Drew a 10\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userblackj_dealerless21(self, input_mock, randint_mock):
        '''
        The user receives cards equal to 21 and blackjacks while the dealer receives cards less than 21.
        The user wins by getting a blackjack and having a higher hand than the dealer.
        '''
        output = run_test([7, 5, 6, 3], ['y', 'g', 'y'], [6, 6, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 5\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 18. Hit (y/n)? g\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 6\n" \
                   "Dealer has 12.\n" \
                   "Drew a 5\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userless21_dealerless21(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([4, 5, 6, 5], ['y', 'g', 'y', 'n'], [6, 4, 2, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 5\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 15. Hit (y/n)? g\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 4\n" \
                   "Dealer has 10.\n" \
                   "Drew a 2\n" \
                   "Dealer has 12.\n" \
                   "Drew a 6\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userless21_dealerbust(self, input_mock, randint_mock):
        '''
        The user receives cards equals less than 21 and blackjacks while dealer receives cards greater than 21 and busts. 
        The user wins since the dealer busts even though user has less cards.
        '''
        output = run_test([13, 12], ['n'], [8, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a Queen\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 5\n" \
                   "Dealer has 13.\n" \
                   "Drew a 10\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userbust_dealerbust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21 and bust, but user greater than dealer.
        The dealer wins since user busts.
        '''
        output = run_test([10, 11, 1], ['y'], [12, 5, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a Jack\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 31.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a King\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userbust_dealerblackj(self, input_mock, randint_mock):
        '''
        The dealers receives cards equal to 21 and blackjacks while user receives cards greater than 21 and busts. 
        The dealer wins since the user busts and dealer has a blackjack.
        '''
        output = run_test([9, 4, 2, 5, 3], ['y', 'g', 'y', 'd', 'y'], [3, 2, 1, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 4\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 15. Hit (y/n)? g\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 20. Hit (y/n)? d\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 2\n" \
                   "Dealer has 5.\n" \
                   "Drew an Ace\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userless21_dealerblackj(self, input_mock, randint_mock):
        '''
        The dealers receives cards equal to 21 and blackjacks while user receives card less than 21. 
        The dealer wins since cards greater than user card and also blackjack.
        '''
        output = run_test([9, 4, 2, 3], ['y', 'g', 'y', 'd', 'n'], [3, 2, 1, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 4\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 15. Hit (y/n)? g\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? d\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 2\n" \
                   "Dealer has 5.\n" \
                   "Drew an Ace\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userbust_dealerless21(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21 and bust, but user greater than dealer.
        The dealer wins since user busts.
        '''
        output = run_test([10, 11, 1], ['y'], [7, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a Jack\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 31.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 10\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userbustequal_dealerbustequal(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21 and bust. Both draw equal hands.
        The dealer wins since user busts.
        '''
        output = run_test([10, 11, 5], ['y'], [12, 5, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a Jack\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a King\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userblackj_dealerblackj(self, input_mock, randint_mock):
        '''
        Both user and dealer draw cards that add up to 21 and both blackjack. 
        Both user and dealer push since no one busts and both have equal hands
        '''
        output = run_test([7, 5, 6, 3], ['y', 'g', 'y'], [6, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 5\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 18. Hit (y/n)? g\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 6\n" \
                   "Dealer has 12.\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userless21equal_dealerless21equal(self, input_mock, randint_mock):
        '''
        Both dealer and user draw cards that give an equal final hand value less than 21.
        Both user and dealer push since no one busts and cards are equal.
        '''
        output = run_test([9, 4, 2, 3], ['y', 'g', 'y', 'd', 'n'], [6, 10, 2], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 4\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 15. Hit (y/n)? g\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? d\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 10\n" \
                   "Dealer has 16.\n" \
                   "Drew a 2\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
