import unittest
import brackets

class BracketsTest(unittest.TestCase):
    def test_check_brackets(self):
        self.assertEqual(brackets.check_brackets("[]"), "Success")
        self.assertEqual(brackets.check_brackets("{}[]"), "Success")
        self.assertEqual(brackets.check_brackets("[()]"), "Success")
        self.assertEqual(brackets.check_brackets("(())"), "Success")
        self.assertEqual(brackets.check_brackets("{[]}()"), "Success")
        self.assertEqual(brackets.check_brackets("{"), "1")
        self.assertEqual(brackets.check_brackets("{[}"), "3")
        self.assertEqual(brackets.check_brackets("foo(bar);"), "Success")
        self.assertEqual(brackets.check_brackets("foo(bar[i);"), "10")
        self.assertEqual(brackets.check_brackets("{}([]"), "3")

if __name__ == '__main__':
    unittest.main()
