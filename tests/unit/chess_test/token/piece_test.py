import unittest
from unittest.mock import create_autospec, patch

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from chess.geometry.coordinate.coord import Coordinate
from chess.rank.base import Rank
from chess.team.model import Team
from chess.token.model.base import Piece



class PieceTest(unittest.TestCase):

    @staticmethod
    def valid_mock_piece(
        piece_id=1,
        name="piece"
    ):
        piece = create_autospec(Piece, instance=True)
        mock_team = create_autospec(Team, instance=True)
        mock_rank = create_autospec(Rank, instance=True)

        piece.id = piece_id
        piece.name = name
        piece.rank = mock_rank
        piece.team = mock_team

        return piece


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_piece_failed_id_validation_raises_error(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = False
        mock_id_validate.return_value.exception = IdValidationException("Invalid ID")

        mock_name_validate.return_value.is_success.return_value = True

        with self.assertRaises(IdValidationException):
            Piece(piece_id=-1, name="piece")


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_piece_failed_name_validation_raises_error(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True

        mock_name_validate.return_value.is_success.return_value = False
        mock_name_validate.return_value.exception = NameValidationException("Invalid name")

        with self.assertRaises(NameValidationException):
            Piece(piece_id=1, name="a1")


    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_piece_constructed_if_params_are_valid(
        self,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True
        mock_name_validate.return_value.is_success.return_value = True

        Piece(piece_id=1, name="piece")


if __name__ == "__main__":
    unittest.main()