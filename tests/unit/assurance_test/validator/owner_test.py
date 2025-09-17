import unittest
from unittest.mock import create_autospec

from assurance.exception.invalid_id import IdValidationException
from assurance.exception.invalid_name import NameValidationException
from chess.commander.exception.invalid_commander import CommanderValidationException
from chess.commander.validator import CommanderValidator
from chess.commander.exception import NullCommanderException
from chess.competitor.commander import Commander
from unit.chess_test.competitor.competitor_test import CompetitorTest


class CompetitorValidatorTest(unittest.TestCase):
    
    def test_null_competitor_raises_exception(self):
        with self.assertRaises(CommanderValidationException) as ctx:
            CommanderValidator.validate(None)

        self.assertIsInstance(ctx.exception.__cause__, NullCommanderException)


    def test_cast_to_competitor_failure_raises_exception(self):
        with self.assertRaises(CommanderValidationException) as ctx:
            CommanderValidator.validate(1)

        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_competitor_validator_failed_id_validation_raises_exception(self):
        mock_competitor = create_autospec(Commander, instance=True)
        mock_competitor.id=-1
        mock_competitor._name= "commander"

        with self.assertRaises(CommanderValidationException) as ctx:
            CommanderValidator.validate(mock_competitor)

        self.assertIsInstance(ctx.exception.__cause__, IdValidationException)


    def test_competitor_validator_failed_name_validation_raises_exception(self):
        mock_competitor = create_autospec(Commander, instance=True)
        mock_competitor.id=1
        mock_competitor._name="A"

        with self.assertRaises(CommanderValidationException) as ctx:
            CommanderValidator.validate(mock_competitor)

        self.assertIsInstance(ctx.exception.__cause__, NameValidationException)


    def test_competitor_validator_payload_equals_valid_competitor(self):
        competitor = CompetitorTest.valid_mock_competitor()
        validation = CommanderValidator.validate(competitor)
        self.assertEqual(validation.payload, competitor)


if __name__ == '__main__':
    unittest.main()
