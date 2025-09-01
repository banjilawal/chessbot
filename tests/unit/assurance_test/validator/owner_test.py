import unittest
from unittest.mock import create_autospec, patch

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.owner import OwnerValidationException
from assurance.validators.owner import OwnerValidator
from chess.exception.null.owner import NullOwnerException
from chess.owner.model import Owner
from unit.chess_test.owner.owner_test import OwnerTest


class OwnerValidatorTest(unittest.TestCase):
    
    def test_null_owner_raises_exception(self):
        with self.assertRaises(OwnerValidationException) as ctx:
            OwnerValidator.validate(None)

        self.assertIsInstance(ctx.exception.__cause__, NullOwnerException)


    def test_cast_to_owner_failure_raises_exception(self):
        with self.assertRaises(OwnerValidationException) as ctx:
            OwnerValidator.validate(1)

        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_owner_validator_failed_id_validation_raises_exception(self):
        mock_owner = create_autospec(Owner, instance=True)
        mock_owner.id=-1
        mock_owner._name= "owner"

        with self.assertRaises(OwnerValidationException) as ctx:
            OwnerValidator.validate(mock_owner)

        self.assertIsInstance(ctx.exception.__cause__, IdValidationException)


    def test_owner_validator_failed_name_validation_raises_exception(self):
        mock_owner = create_autospec(Owner, instance=True)
        mock_owner.id=1
        mock_owner._name="A"

        with self.assertRaises(OwnerValidationException) as ctx:
            OwnerValidator.validate(mock_owner)

        self.assertIsInstance(ctx.exception.__cause__, NameValidationException)


    def test_owner_validator_payload_equals_valid_owner(self):
        owner = OwnerTest.valid_mock_owner()
        validation = OwnerValidator.validate(owner)
        self.assertEqual(validation.payload, owner)


if __name__ == '__main__':
    unittest.main()
