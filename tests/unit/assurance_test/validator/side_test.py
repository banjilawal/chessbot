import unittest
from unittest.mock import create_autospec

from chess.commander.exception.invalid_commander import CommanderValidationException
from assurance.exception.invalid_id import IdValidationException
from chess.team.team_exception.invalid_team import TeamValidationException
from chess.team.validator import TeamValidator
from chess.competitor.commander import Commander
from chess.team.schema.schema import TeamSchema
from chess.team.team_exception.null_team_profile import NullTeamProfileException
from chess.team.team_exception.null_team import NullTeamException
from chess.side.team import Side
from unit.chess_test.competitor.competitor_test import CompetitorTest


class SideValidatorTest(unittest.TestCase):

  def test_null_side_raises_exception(self):
    with self.assertRaises(TeamValidationException) as ctx:
      TeamValidator.validate(None)
    self.assertIsInstance(ctx.exception.__cause__, NullTeamException)


  def test_cast_to_side_failure_raises_exception(self):
    with self.assertRaises(TeamValidationException) as ctx:
      TeamValidator.validate(1)
    self.assertIsInstance(ctx.exception.__cause__, TypeError)


  def test_failed_id_validation_raises_exception(self):
    mock_side = create_autospec(Side, instance=True)
    mock_side.id=-1
    mock_side.schema = TeamSchema.BLACK
    mock_side.competitor= CompetitorTest.valid_mock_competitor()

    with self.assertRaises(TeamValidationException) as ctx:
      TeamValidator.validate(mock_side)
    self.assertIsInstance(ctx.exception.__cause__, IdValidationException)


  def test_side_failed_competitor_validation_raises_exception(self):
    mock_side = create_autospec(Side, instance=True)
    mock_side.id=1
    mock_side.competitor=None
    mock_side.schema = TeamSchema.BLACK

    with self.assertRaises(TeamValidationException) as ctx:
      TeamValidator.validate(mock_side)

    self.assertIsInstance(ctx.exception.__cause__, CommanderValidationException)


  def test_side_null_profile_raises_exception(self):
    mock_side = create_autospec(Side, instance=True)
    mock_side.id=1


    mock_side.competitor=Commander(1, "commander")
    mock_side.schema = None

    with self.assertRaises(TeamValidationException) as ctx:
      TeamValidator.validate(mock_side)
    #
    self.assertIsInstance(ctx.exception.__cause__, NullTeamProfileException)


  def test_side_validator_payload_equals_valid_side(self):
    side = Side(1, Commander(1, "commander"), TeamSchema.BLACK)
    validation = TeamValidator.validate(side)
    self.assertEqual(validation.payload, side)


if __name__ == '__main__':
  unittest.main()
