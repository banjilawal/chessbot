import unittest

from assurance.exception.invalid_id import IdValidationException
from chess.system.id.validator import IdValidator
from chess.exception.id.negative_id_exception import NegativeIdException
from chess.exception.null.id import IdNullException


class IdValidatorTest(unittest.TestCase):

    def test_null_id_raises_exception(self):
        with self.assertRaises(IdValidationException) as ctx:
            IdValidator.validate(None)
        self.assertIsInstance(ctx.exception.__cause__,IdNullException)


    def test_cast_to_int_failure_raises_exception(self):
        with self.assertRaises(IdValidationException) as ctx:
            IdValidator.validate("5")
        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_negative_id_raises_exception(self):
        with self.assertRaises(IdValidationException) as ctx:
            IdValidator.validate(-1)
        self.assertIsInstance(ctx.exception.__cause__, NegativeIdException)


    def test_validation_payload_equals_input_param(self):
        result = IdValidator.validate(1)
        self.assertEqual(result.payload, 1)


if __name__ == '__main__':
    unittest.main()
