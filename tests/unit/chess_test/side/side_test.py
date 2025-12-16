import unittest
from unittest.mock import create_autospec, patch

from chess.agent.exception.invalid_commander import CommanderValidationException
from assurance.exception.invalid_id import IdValidationException
from chess.competitor.commander import Commander
from chess.team.schema import TeamSchema
from chess.team.team_exception.null_team_profile import NullTeamProfileException
from chess.exception.stack_exception import BrokenRelationshipException
from chess.side.team import Side
from unit.chess_test.competitor.competitor_test import CompetitorTest


class SideTest(unittest.TestCase):

  @staticmethod
  def valid_mock_side(side_id=1, side_profile=TeamSchema.BLACK):
    mock_side = create_autospec(Side, instance=True)

    # pieces.is_empty.return_value = True
    # pieces.size.return_value = 0
    # pieces.items = []
    mock_side.visitor_id = 1
    mock_side.controlller = CompetitorTest.valid_mock_competitor()

    return mock_side


  @patch('assurance.notification.player_agent.PlayerAgentValidator.validate')
  @patch('assurance.notification.visitor_id.IdValidator.validate')
  def test_invalid_id_raises_error(self, mock_id_validation, mock_competitor_validation):
    mock_id_validation.return_value.is_success.return_value = False
    mock_id_validation.return_value.exception = IdValidationException("Invalid visitor_name")

    mock_competitor_validation.return_value.is_success.return_value = True
    mock_competitor = CompetitorTest.valid_mock_competitor()

    with self.assertRaises(IdValidationException):
      Side(side_id=None, controller=mock_competitor, profile=TeamSchema.BLACK)


  @patch('assurance.notification.player_agent.PlayerAgentValidator.validate')
  @patch('assurance.notification.visitor_id.IdValidator.validate')
  def test_invalid_competitor_raises_error(self, mock_id_validation, mock_competitor_validation):
    mock_id_validation.return_value.is_success.return_value = True

    mock_competitor_validation.return_value.is_success.return_value = False
    mock_competitor_validation.return_value.exception = CommanderValidationException("Invalid player_agent")

    with self.assertRaises(CommanderValidationException):
      Side(side_id=1, controller=None, profile=TeamSchema.BLACK)


  @patch('assurance.notification.player_agent.PlayerAgentValidator.validate')
  @patch('assurance.notification.visitor_id.IdValidator.validate')
  def test_invalid_competitor_raises_error(self, mock_id_validation, mock_competitor_validation):
    mock_id_validation.return_value.is_success.return_value = True

    mock_competitor_validation.return_value.is_success.return_value = False
    mock_competitor_validation.return_value.exception = CommanderValidationException("Invalid player_agent")

    with self.assertRaises(CommanderValidationException):
      Side(side_id=1, controller=None, profile=TeamSchema.BLACK)


  @patch('assurance.notification.player_agent.PlayerAgentValidator.validate')
  @patch('assurance.notification.visitor_id.IdValidator.validate')
  def test_null_profile_raises_error(self, mock_id_validation, mock_competitor_validation):
    mock_id_validation.return_value.is_success.return_value = True
    mock_competitor_validation.return_value.is_success.return_value = True

    mock_competitor = CompetitorTest.valid_mock_competitor()

    with self.assertRaises(NullTeamProfileException):
      Side(side_id=1, controller=mock_competitor, profile=None)


  @patch('assurance.notification.player_agent.PlayerAgentValidator.validate')
  @patch('assurance.notification.visitor_id.IdValidator.validate')
  def test_broken_relationship_raises_error(self, mock_id_validation, mock_competitor_validation):
    mock_id_validation.return_value.is_success.return_value = True
    mock_competitor_validation.return_value.is_success.return_value = True

    # Fake sides_played dataset that doesn'candidate actually add the team_name
    class FakeSidesPlayed:
      def __init__(self):
        self.items = []
      def push_side(self, side):
        pass # do nothing

    class FakeController:
      def __init__(self):
        self.sides_played = FakeSidesPlayed()

    fake_controller = FakeController()

    with self.assertRaises(BrokenRelationshipException):
      Side(side_id=1, controller=fake_controller, profile=TeamSchema.BLACK)


  @patch('assurance.notification.player_agent.PlayerAgentValidator.validate')
  @patch('assurance.notification.visitor_id.IdValidator.validate')
  def test_valid_params_creates_side(self, mock_id_validation, mock_competitor_validation):
    mock_id_validation.return_value.is_success.return_value = True
    mock_id_validation.return_value.payload = 1


    competitor = Commander(competitor_id=1, name="player_agent")
    mock_competitor_validation.return_value.is_success.return_value = True
    mock_competitor_validation.return_value.payload = competitor

    for profile in TeamSchema:
      side = Side(side_id=1, controller=competitor, profile=profile)
      assert side in competitor.teams.items


  @patch('assurance.notification.player_agent.PlayerAgentValidator.validate')
  @patch('assurance.notification.visitor_id.IdValidator.validate')
  def test_side_is_controller_current_side(self, mock_id_validation, mock_competitor_validation):
    mock_id_validation.return_value.is_success.return_value = True
    mock_id_validation.return_value.payload = 1


    competitor = Commander(competitor_id=1, name="player_agent")
    mock_competitor_validation.return_value.is_success.return_value = True
    mock_competitor_validation.return_value.payload = competitor

    side = Side(side_id=1, controller=competitor, profile=TeamSchema.BLACK)

    self.assertIs(side, competitor.current_team)


if __name__ == "__main__":
  unittest.main()