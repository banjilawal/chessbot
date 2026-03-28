# src/logic/points/origin/coord_stack_validator.py

"""
Module: logic.points.origin.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""


from typing import Any, cast


from logic.piece import PieceValidator
from logic.square import SquareValidationTransaction
from logic.system import LoggingLevelRouter, ValidationTransaction, ValidationResult
from logic.domain import DomainOrigin, InvalidDomainOriginException, NullDomainOriginException




class DomainOriginValidationTransaction(ValidationTransaction[DomainOrigin]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a DomainOrigin instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   ValidationTransaction

    # PROVIDES:
        * DomainOriginValidationTransaction


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            piece_validator: type[PieceValidator] = PieceValidator,
            square_validator: type[SquareValidationTransaction] = SquareValidationTransaction
    ) -> ValidationResult[DomainOrigin]:
        """
        # ACTION:
        Use chained PieceValidator and SquareValidationTransaction to ensure a candidate is a valid DomainOrigin before
        the client can use it.

        # PARAMETERS:
          * candidate (Any): Object to verify is a Domain.
          * piece_validator (type[PieceValidator]): Injected into validation.
          * validation (type[SquareValidationTransaction]): verifies the relationship between the
                Domain's owning Token and Square.

        # RETURNS:
          ValidationResult[DomainOrigin] containing either:
                - On success: DomainOrigin in the payload.
                - On failure: Exception.

        Raises:
            * TypeError
            * InvalidDomainOriginException
        """
        method = "DomainOriginValidationTransaction.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullDomainOriginException(
                        f"{method}: {NullDomainOriginException.MSG}"
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
                    f"{method}: {InvalidDomainOriginException.MSG}", e
                )
            )