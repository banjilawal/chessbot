import unittest
from unittest.mock import create_autospec, patch

from assurance.exception.invalid_id import IdValidationException
from assurance.exception.invalid_name import NameValidationException
from chess.competitor.commander import Commander
from chess.competitor.side import SideRecord


class CompetitorTest(unittest.TestCase):

  @staticmethod
  def valid_mock_competitor(competitor_id=1, name="commander"):
    competitor = create_autospec(Commander, instance=True)
    sides_played = create_autospec(SideRecord, instance=True)

    sides_played.is_empty.return_value = True
    sides_played.size.return_value = 0
    sides_played.items = []
    sides_played.current_team = None

    competitor.id = 1
    competitor.name = "Valid Commander"
    competitor.teams = sides_played

    return competitor


  @patch('assurance.notification.name.NameValidator.validate')
  @patch('assurance.notification.id.IdValidator.validate')
  def test_competitor_failed_id_validation_raises_error(
    self,
    mock_name_validate,
    mock_id_validate
  ):
    mock_id_validate.return_value.is_success.return_value = False
    mock_id_validate.return_value.exception = IdValidationException("Invalid ID")

    mock_name_validate.return_value.is_success.return_value = True

    with self.assertRaises(IdValidationException):
      Commander(competitor_id=-1, name="commander")


  @patch('assurance.notification.name.NameValidator.validate')
  @patch('assurance.notification.id.IdValidator.validate')
  def test_competitor_failed_name_validation_raises_error(
    self,
    mock_name_validate,
    mock_id_validate
  ):
    mock_id_validate.return_value.is_success.return_value = True

    mock_name_validate.return_value.is_success.return_value = False
    mock_name_validate.return_value.exception = NameValidationException("Invalid name")

    with self.assertRaises(NameValidationException):
      Commander(competitor_id=1, name="a1")


  @patch('assurance.notification.name.NameValidator.validate')
  @patch('assurance.notification.id.IdValidator.validate')
  def test_competitor_constructed_if_params_are_valid(
    self,
    mock_name_validate,
    mock_id_validate
  ):
    mock_id_validate.return_value.is_success.return_value = True
    mock_name_validate.return_value.is_success.return_value = True

    Commander(competitor_id=1, name="commander")


if __name__ == "__main__":
  unittest.main()