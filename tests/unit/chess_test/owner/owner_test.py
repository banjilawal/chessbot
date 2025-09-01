import unittest
from unittest.mock import create_autospec, patch

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from chess.owner.base import Owner
from chess.team.stack import TeamHistory


class OwnerTest(unittest.TestCase):

    @staticmethod
    def valid_mock_owner(owner_id=1, name="owner"):
        mock_owner = create_autospec(Owner, instance=True)
        mock_team_history = create_autospec(TeamHistory, instance=True)

        mock_team_history.is_empty.return_value = True
        mock_team_history.size.return_value = 0
        mock_team_history.items = []
        mock_team_history.current_team = None

        mock_owner.id = 1
        mock_owner.name = "Valid Owner"
        mock_owner.team_history = mock_team_history

        return mock_owner


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_owner_failed_id_validation_raises_error(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = False
        mock_id_validate.return_value.exception = IdValidationException("Invalid ID")

        mock_name_validate.return_value.is_success.return_value = True

        with self.assertRaises(IdValidationException):
            Owner(owner_id=-1, name="owner")


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_owner_failed_name_validation_raises_error(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True

        mock_name_validate.return_value.is_success.return_value = False
        mock_name_validate.return_value.exception = NameValidationException("Invalid name")

        with self.assertRaises(NameValidationException):
            Owner(owner_id=1, name="a1")


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_owner_constructed_if_params_are_valid(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True
        mock_name_validate.return_value.is_success.return_value = True

        Owner(owner_id=1, name="owner")


if __name__ == "__main__":
    unittest.main()