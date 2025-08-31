import unittest

from assurance.exception.validation.name import NameValidationException
from assurance.validators.name import NameValidator
from chess.exception.name import BlankNameException, NameTooShortException, NameTooLongException
from chess.exception.null.name import NullNameException


class NameValidatorTest(unittest.TestCase):

    def test_null_name_raises_exception(self):
        with self.assertRaises(NameValidationException) as ctx:
            NameValidator.validate(None)
        self.assertIsInstance(ctx.exception.__cause__, NullNameException)


    def test_cast_to_str_failure_raises_exception(self):
        with self.assertRaises(NameValidationException) as ctx:
            NameValidator.validate(1)
        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_blank_name_raises_exception(self):
        with self.assertRaises(NameValidationException) as ctx:
            NameValidator.validate(" ")
        self.assertIsInstance(ctx.exception.__cause__, BlankNameException)

    def test_name_too_short_raises_exception(self):
        with self.assertRaises(NameValidationException) as ctx:
            NameValidator.validate("a")
        self.assertIsInstance(ctx.exception.__cause__, NameTooShortException)


    def test_name_too_long_raises_exception(self):
        long_name = "x" * 41
        with self.assertRaises(NameValidationException) as ctx:
            NameValidator.validate(long_name)
        self.assertIsInstance(ctx.exception.__cause__, NameTooLongException)


    def test_valid_name_returns_result(self):
        result = NameValidator.validate("A-1")
        self.assertEqual(result.payload, "A-1")


if __name__ == '__main__':
    unittest.main()
