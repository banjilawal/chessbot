# src/logic/square/query/validation/validation.py

"""
Module: logic.square.query.validation.validation
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from logic.square import SquareService
from logic.board import BoardService
from logic.coord.service import CoordService
from logic.system import IdentityService, LoggingLevelRouter, ValidationResult, ValidationTransaction
from logic.square import (
    SquareContextValidationException, SquareValidationTransaction, ZeroSquareContextFlagsException, SquareContext,
    NullSquareContextException, ExcessSquareContextFlagsException, SquareContextValidationRouteException
)



class SquareContextValidationTransaction(ValidationTransaction[SquareContext]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a SquareContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails send an exception detailing the failure.

    Super Class:
        *   ValidationTransaction

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
            square_validator: SquareValidationTransaction = SquareValidationTransaction(),
    ) -> ValidationResult[SquareContext]:
        """
        # ACTION:
            1.  If the candidate fails either
                    *   A null check.
                    *   A type check.
                Send an exception chain in the ValidationResult. Else, cast candidate to SquareContext
                instance query.
            2.  Send an exception chain in the ValidationResult if either
                    *   The id
                    *   The name
                    *   The coord
                    *   The state
                    *   The board
                    *   The occupant
                are does not pass a validation check. by their services, or there is no validation
                route for the query.
            3.  The query has been certified as safe, send the validation success result.
        # PARAMETERS:
            *   candidate (Any)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service: (IdentityService)
            *   square_validator (SquareValidationTransaction)
        # RETURNS:
            *   ValidationResult[SquareContext] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload
        Raises:
            *   TypeError
            *   NullSquareContextException
            *   ZeroSquareContextFlagsException
            *   ExcessSquareContextFlagsException
            *   SquareContextValidationRouteException
            *   SquareContextValidationException
        """
        method = "SquareContextValidationTransaction.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    msg=f"{method}: {SquareContextValidationException.MSG}",
                    ex=NullSquareContextException(f"{method}: {NullSquareContextException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    msg=f"{method}: {SquareContextValidationException.MSG}",
                    ex=TypeError(
                        f"{method}: Was expecting a SquareContext, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to SquareContext for additional tests. ---#
        context = cast(SquareContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    msg=f"{method}: {SquareContextValidationException.MSG}",
                    ex=ZeroSquareContextFlagsException(f"{method}: {ZeroSquareContextFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    msg=f"{method}: {SquareContextValidationException.MSG}",
                    ex=ExcessSquareContextFlagsException(
                        f"{method}: {ExcessSquareContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation = identity_service.validate_id(candidate=context.id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        msg=f"{method}: {SquareContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-name target.
        if context.name is not None:
            validation = identity_service.validate_name(context.name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        msg=f"{method}: {SquareContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the name_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation = coord_service.validation.execute(context.coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        msg=f"{method}: {SquareContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the coord_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation = board_service.validation.execute(context.board)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        msg=f"{method}: {SquareContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-occupant target.
        if context.occupant is not None:
            validation = square_service.validation.execute(context.occupant)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        msg=f"{method}: {SquareContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-state.
        if context.state is not None:
            validation = square_validator.validate_square_state(context.occupant)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        msg=f"{method}: {SquareContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the query.
        return ValidationResult.failure(
            SquareContextValidationException(
                msg=f"{method}: {SquareContextValidationException.MSG}",
                ex=SquareContextValidationRouteException(
                    f"{method}: {SquareContextValidationRouteException.MSG}"
                )
            )
        )

