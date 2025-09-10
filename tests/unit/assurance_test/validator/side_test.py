import unittest
from unittest.mock import create_autospec, patch

from assurance.exception.validation.competitor import CompetitorValidationException
from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.team import SideValidationException
from assurance.validators.side import SideValidator
from chess.competitor.commander import Commander
from chess.config.game import SideProfile
from chess.exception.null.side_profile import NullSideProfileException
from chess.exception.null.side import NullSideException
from chess.side.team import Side
from unit.chess_test.competitor.competitor_test import CompetitorTest
from unit.chess_test.side.side_test import SideTest


class SideValidatorTest(unittest.TestCase):
    
    def test_null_side_raises_exception(self):
        with self.assertRaises(SideValidationException) as ctx:
            SideValidator.validate(None)
        self.assertIsInstance(ctx.exception.__cause__, NullSideException)


    def test_cast_to_side_failure_raises_exception(self):
        with self.assertRaises(SideValidationException) as ctx:
            SideValidator.validate(1)
        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_failed_id_validation_raises_exception(self):
        mock_side = create_autospec(Side, instance=True)
        mock_side.id=-1
        mock_side.profile = SideProfile.BLACK
        mock_side.competitor= CompetitorTest.valid_mock_competitor()

        with self.assertRaises(SideValidationException) as ctx:
            SideValidator.validate(mock_side)
        self.assertIsInstance(ctx.exception.__cause__, IdValidationException)


    def test_side_failed_competitor_validation_raises_exception(self):
        mock_side = create_autospec(Side, instance=True)
        mock_side.id=1
        mock_side.competitor=None
        mock_side.profile = SideProfile.BLACK

        with self.assertRaises(SideValidationException) as ctx:
            SideValidator.validate(mock_side)

        self.assertIsInstance(ctx.exception.__cause__, CompetitorValidationException)


    def test_side_null_profile_raises_exception(self):
        mock_side = create_autospec(Side, instance=True)
        mock_side.id=1


        mock_side.competitor=Commander(1, "commander")
        mock_side.profile = None

        with self.assertRaises(SideValidationException) as ctx:
            SideValidator.validate(mock_side)
        #
        self.assertIsInstance(ctx.exception.__cause__, NullSideProfileException)


    def test_side_validator_payload_equals_valid_side(self):
        side = Side(1, Commander(1, "commander"), SideProfile.BLACK)
        validation = SideValidator.validate(side)
        self.assertEqual(validation.payload, side)


if __name__ == '__main__':
    unittest.main()
