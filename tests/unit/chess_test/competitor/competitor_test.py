import unittest
from unittest.mock import create_autospec, patch

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from chess.competitor.model import Competitor
from chess.competitor.side import SideRecord
from chess.config.game import SideProfile


class CompetitorTest(unittest.TestCase):

    @staticmethod
    def valid_mock_competitor(competitor_id=1, name="competitor"):
        competitor = create_autospec(Competitor, instance=True)
        sides_played = create_autospec(SideRecord, instance=True)

        sides_played.is_empty.return_value = True
        sides_played.size.return_value = 0
        sides_played.items = []
        sides_played.current_side = None

        competitor.id = 1
        competitor.name = "Valid Competitor"
        competitor.sides_played = sides_played

        return competitor


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_competitor_failed_id_validation_raises_error(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = False
        mock_id_validate.return_value.exception = IdValidationException("Invalid ID")

        mock_name_validate.return_value.is_success.return_value = True

        with self.assertRaises(IdValidationException):
            Competitor(competitor_id=-1, name="competitor")


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_competitor_failed_name_validation_raises_error(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True

        mock_name_validate.return_value.is_success.return_value = False
        mock_name_validate.return_value.exception = NameValidationException("Invalid name")

        with self.assertRaises(NameValidationException):
            Competitor(competitor_id=1, name="a1")


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_competitor_constructed_if_params_are_valid(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True
        mock_name_validate.return_value.is_success.return_value = True

        Competitor(competitor_id=1, name="competitor")


if __name__ == "__main__":
    unittest.main()