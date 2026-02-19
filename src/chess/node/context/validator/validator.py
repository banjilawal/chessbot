# src/chess/node/context/validator/validator.py

"""
Module: chess.node.context.validator.validator
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from chess.board import BoardService
from chess.coord.service import CoordService
from chess.node.state import NodeState
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.node import (
    NodeContextValidationFailedException, ZeroNodeContextFlagsException, NodeContext,
    NullNodeContextException, ExcessiveNodeContextFlagsException, NodeContextValidationRouteException
)
from chess.token import TokenService


class NodeContextValidator(Validator[NodeContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a NodeContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

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
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            token_service: TokenService = TokenService(),
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[NodeContext]:
        """
        # ACTION:
            1.  If Candidate fails existence or type checks return the exception chain in the ValidationResult. Else,
                test how many optional attributes are not null.
            2.  If only one attribute is one and only one attribute is not null return the exception chain in the
                ValidationResult.
            3.  If no route is found for the enabled attribute send an exception chain in the ValidationResult.
            4.  If a validation route exists return the outcome of the validation to the caller.
        # PARAMETERS:
            *   candidate (Any)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   token_service (TokenService)
            *   identity_service (IdentityService):
        # RETURNS:
            *   ValidationResult[NodeContext] containing either:
                    - On failure:   Exception.
                    - On success:   NodeContext in the payload.
        # RAISES:
            *   TypeError
            *   NullNodeContextException
            *   ZeroNodeContextFlagsException
            *   ExcessiveNodeContextFlagsException
            *   NodeContextValidationRouteException
            *   NodeContextValidationFailedException
        """
        method = "NodeContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullNodeContextException(f"{method}: {NullNodeContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, NodeContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Was expecting a NodeContext, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to NodeContext for additional tests. ---#
        context = cast(NodeContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroNodeContextFlagsException(f"{method}: {ZeroNodeContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ExcessiveNodeContextFlagsException(
                        f"{method}: {ExcessiveNodeContextFlagsException.DEFAULT_MESSAGE}"
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
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-name target.
        if context.name is not None:
            validation = identity_service.validate_name(context.name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the name_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation = coord_service.validator.validate(context.coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the coord_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation = board_service.validator.validate(context.board)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-occupant target.
        if context.occupant is not None:
            validation = token_service.validator.validate(context.occupant)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-state.
        if context.state is not None:
            if not isinstance(context.state, NodeState):
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=TypeError(
                            f"{method}: Was expecting a NodeState, got {type(candidate).__name__} instead."
                        )
                    )
                )
            # On certification success return the board_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            NodeContextValidationFailedException(
                message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                ex=NodeContextValidationRouteException(
                    f"{method}: {NodeContextValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )

