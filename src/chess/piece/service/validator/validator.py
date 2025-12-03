from typing import Any

from chess.piece import PieceIntegrityService
from chess.system import ValidationResult, Validator


class PieceServiceValidator(Validator[PieceIntegrityService]):
    
    @classmethod
    def validate(cls, candidate: Any) -> ValidationResult[PieceIntegrityService]:
        pass