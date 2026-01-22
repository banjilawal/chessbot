# src/chess/points/origin/coord_stack_validator.py

"""
Module: chess.points.origin.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""


from typing import Any, cast


from chess.piece import PieceValidator
from chess.square import SquareValidator
from chess.system import LoggingLevelRouter, Validator, ValidationResult
from chess.domain import DomainOrigin, InvalidDomainOriginException, NullDomainOriginException




class DomainOriginValidator(Validator[DomainOrigin]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a DomainOrigin instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * DomainOriginValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            piece_validator: type[PieceValidator] = PieceValidator,
            square_validator: type[SquareValidator] = SquareValidator
    ) -> ValidationResult[DomainOrigin]:
        """
        # ACTION:
        Use chained PieceValidator and SquareValidator to ensure a candidate is a valid DomainOrigin before
        the client can use it.

        # PARAMETERS:
          * candidate (Any): Object to verify is a Domain.
          * piece_validator (type[PieceValidator]): Injected into validator.
          * validator (type[SquareValidator]): verifies the relationship between the
                Domain's owning Token and Square.

        # RETURNS:
          ValidationResult[DomainOrigin] containing either:
                - On success: DomainOrigin in the payload.
                - On failure: Exception.

        # RAISES:
            * TypeError
            * InvalidDomainOriginException
        """
        method = "DomainOriginValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullDomainOriginException(
                        f"{method}: {NullDomainOriginException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, DomainOrigin):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected DomainOrigin, got {type(candidate).__name__} instead.")
                )
            
            domain_origin = cast(DomainOrigin, candidate)
            
            piece_square_binding_validation = square_validator.validate_piece_square_binding(
                square_candidate=domain_origin.square,
                piece_candidate=domain_origin.owner,
                piece_validator=piece_validator,
            )
            
            if piece_square_binding_validation.is_failure():
                return ValidationResult.failure(piece_square_binding_validation.exception)
            
            ValidationResult.success(payload=domain_origin)
            
        except Exception as e:
            return ValidationResult.failure(
                InvalidDomainOriginException(
                    f"{method}: {InvalidDomainOriginException.DEFAULT_MESSAGE}", e
                )
            )