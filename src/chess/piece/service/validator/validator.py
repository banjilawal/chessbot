from typing import Any

from chess.piece import PieceService
from chess.system import ValidationResult, Validator


class PieceServiceValidator(Validator[PieceService]):
    
    @classmethod
    def validate(cls, candidate: Any) -> ValidationResult[PieceService]:
        pass