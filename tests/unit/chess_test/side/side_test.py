import unittest
from unittest.mock import create_autospec, patch

from assurance.exception.validation.competitor import CompetitorValidationException
from assurance.exception.validation.id import IdValidationException
from chess.competitor.model import Competitor
from chess.config.game import SideProfile
from chess.exception.null.side_profile import NullSideProfileException
from chess.exception.stack import BrokenRelationshipException
from chess.side.team import Side
from unit.chess_test.competitor.competitor_test import CompetitorTest


class SideTest(unittest.TestCase):

    @staticmethod
    def valid_mock_side(side_id=1, side_profile=SideProfile.BLACK):
        mock_side = create_autospec(Side, instance=True)

        # pieces.is_empty.return_value = True
        # pieces.size.return_value = 0
        # pieces.items = []
        mock_side.id = 1
        mock_side.controlller = CompetitorTest.valid_mock_competitor()

        return mock_side


    @patch('assurance.validators.competitor.CompetitorValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_invalid_id_raises_error(self, mock_id_validation, mock_competitor_validation):
        mock_id_validation.return_value.is_success.return_value = False
        mock_id_validation.return_value.exception = IdValidationException("Invalid name")

        mock_competitor_validation.return_value.is_success.return_value = True
        mock_competitor = CompetitorTest.valid_mock_competitor()

        with self.assertRaises(IdValidationException):
            Side(side_id=None, controller=mock_competitor, profile=SideProfile.BLACK)


    @patch('assurance.validators.competitor.CompetitorValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_invalid_competitor_raises_error(self, mock_id_validation, mock_competitor_validation):
        mock_id_validation.return_value.is_success.return_value = True

        mock_competitor_validation.return_value.is_success.return_value = False
        mock_competitor_validation.return_value.exception = CompetitorValidationException("Invalid competitor")

        with self.assertRaises(CompetitorValidationException):
            Side(side_id=1, controller=None, profile=SideProfile.BLACK)


    @patch('assurance.validators.competitor.CompetitorValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_invalid_competitor_raises_error(self, mock_id_validation, mock_competitor_validation):
        mock_id_validation.return_value.is_success.return_value = True

        mock_competitor_validation.return_value.is_success.return_value = False
        mock_competitor_validation.return_value.exception = CompetitorValidationException("Invalid competitor")

        with self.assertRaises(CompetitorValidationException):
            Side(side_id=1, controller=None, profile=SideProfile.BLACK)


    @patch('assurance.validators.competitor.CompetitorValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_null_profile_raises_error(self, mock_id_validation, mock_competitor_validation):
        mock_id_validation.return_value.is_success.return_value = True
        mock_competitor_validation.return_value.is_success.return_value = True

        mock_competitor = CompetitorTest.valid_mock_competitor()

        with self.assertRaises(NullSideProfileException):
            Side(side_id=1, controller=mock_competitor, profile=None)


    @patch('assurance.validators.competitor.CompetitorValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_broken_relationship_raises_error(self, mock_id_validation, mock_competitor_validation):
        mock_id_validation.return_value.is_success.return_value = True
        mock_competitor_validation.return_value.is_success.return_value = True

        # Fake sides_played collection that doesn't actually add the side
        class FakeSidesPlayed:
            def __init__(self):
                self.items = []
            def push_side(self, side):
                pass  # do nothing

        class FakeController:
            def __init__(self):
                self.sides_played = FakeSidesPlayed()

        fake_controller = FakeController()

        with self.assertRaises(BrokenRelationshipException):
            Side(side_id=1, controller=fake_controller, profile=SideProfile.BLACK)


    @patch('assurance.validators.competitor.CompetitorValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_valid_params_creates_side(self, mock_id_validation, mock_competitor_validation):
        mock_id_validation.return_value.is_success.return_value = True
        mock_id_validation.return_value.payload = 1


        competitor = Competitor(competitor_id=1, name="competitor")
        mock_competitor_validation.return_value.is_success.return_value = True
        mock_competitor_validation.return_value.payload = competitor

        for profile in SideProfile:
            side = Side(side_id=1, controller=competitor, profile=profile)
            assert side in competitor.sides_played.items


    @patch('assurance.validators.competitor.CompetitorValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_side_is_controller_current_side(self, mock_id_validation, mock_competitor_validation):
        mock_id_validation.return_value.is_success.return_value = True
        mock_id_validation.return_value.payload = 1


        competitor = Competitor(competitor_id=1, name="competitor")
        mock_competitor_validation.return_value.is_success.return_value = True
        mock_competitor_validation.return_value.payload = competitor

        side = Side(side_id=1, controller=competitor, profile=SideProfile.BLACK)

        self.assertIs(side, competitor.current_side)


if __name__ == "__main__":
    unittest.main()