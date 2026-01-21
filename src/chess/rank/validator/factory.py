# src/chess/rank/validator/factory.py

"""
Module: chess.rank.validator.factory
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    Bishop, BishopValidator, InvalidRankException, King, KingValidator, Knight, KnightValidator,
    NullRankException, Pawn, PawnValidator, Queen, QueenValidator, Rank, RankSpecValidator, Rook, RookValidator
)
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult


class RankValidatorFactory(Validator[Rank]):
    """
    # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Verifies a candidate is a Rank instance that meets integrity requirements, before
        the candidate is used.

    # PROVIDES:
    ValidationResult[Rank] containing either:
        - On success: Rank in the payload.
        - On failure: Exception.

    # ATTRIBUTES:

    # CONSTRUCTOR:
    Default Constructor

    # CLASS METHODS:
        def validate(
                candidate: Any, rook_validator: RookValidator, king_validator: KingValidator,
                pawn_validator: PawnValidator, queen_validator: QueenValidator,
                knight_validator: KnightValidator, bishop_validator: BishopValidator,
        ) -> ValidationResult[Rank]: ValidationResult[(Team, Game)]:

    # INSTANCE METHODS:
        *   rank_spec_validator: PersonaValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            rook_validator: RookValidator = RookValidator(),
            king_validator: KingValidator = KingValidator(),
            pawn_validator: PawnValidator = PawnValidator(),
            queen_validator: QueenValidator = QueenValidator(),
            knight_validator: KnightValidator = KnightValidator(),
            bishop_validator: BishopValidator = BishopValidator(),
    ) -> ValidationResult[Rank]:
        """
        # ACTION:
        1.  Check if the candidate is null. If so return an exception in a ValidationResult.
        2.  If the candidate is not a Rank instance return an exception in a ValidationResult.
        3.  Find the candidate's matching concrete rank and hand off its validation to the
            subclass validator.

        # PARAMETERS:
            *   candidate (Any)
            *   rook_validator (RookValidator)
            *   king_validator (KingValidator)
            *   pawn_validator (PawnValidator)
            *   queen_validator (QueenValidator)
            *   knight_validator (KnightValidator)
            *   bishop_validator (BishopValidator)
            
        # RETURNS:
        ValidationResult[Rank] containing either:
            - On success: Rank in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullRankException
            *   RankValidationFailedException
        """
        method = "RankValidatorFactory.validate"
        try:
            # Make sure its not null first.
            if candidate is None:
                return ValidationResult.failure(
                    NullRankException(f"{method} {NullRankException.DEFAULT_MESSAGE}")
                )
            # Verify candidate is a Rank instance. Cast to a Rank if so.
            if not isinstance(candidate, Rank):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Rank, got {type(candidate).__name__} instead.")
                )
            rank = cast(Rank, candidate)
            # Pick which validator to run.
            if isinstance(candidate, King):
                return king_validator.validate(rank)
            if isinstance(candidate, Queen):
                return queen_validator.validate(rank)
            if isinstance(candidate, Rook):
                return rook_validator.validate(rank)
            if isinstance(candidate, Bishop):
                return bishop_validator.validate(rank)
            if isinstance(candidate, Knight):
                return knight_validator.validate(rank)
            if isinstance(candidate, Pawn):
                return pawn_validator.validate(rank)
            
        # If the candidate is not any of the concrete Ranks control passes to the except block.
        # The unhandled exception is wrapped inside an RankValidationFailedException which is sent inside
        # a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankException(ex=ex, message=f"{method}: {InvalidRankException.DEFAULT_MESSAGE}")
            )


# src/chess/rank/factory/factory.py

"""
Module: chess.rank.factory.factory
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""

from chess.persona import Persona, PersonaService
from chess.system import Builder, ValidationResult, LoggingLevelRouter, id_emitter
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, RankValidationFailedException, RankBuildRouteException, Rook


class RankValiatorFactory(Validator[Rank]):
    """
    # ROLE: Factory, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Produce Rank instances whose integrity is guaranteed at creation.
    2.  Manage construction of Rank instances that can be used safely by the client.
    3.  Ensure params for Rank creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
        *   RankFactory

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls, candidate: Any,
            persona_service: PersonaService = PersonaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Rank]:
        """
        # ACTION:
        Given a Persona, return an appropriate Rank object.

        # PARAMETERS:
            * persona (Persona)

        # RETURNS:
          ValidationResult[Rank] containing either:
                - On success: a concrete Rank in the payload.
                - On failure: Exception.

        # RAISES:
            * RankValidationFailedException
        """
        method = "RankFactory.builder"
        # Handle the case that the candidate does not exist.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullRankException(f"{method}: {NullRankException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the candidate is the wrong type.
        if not isinstance(candidate, Rank):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a Rank, got {type(candidate).__name__} instead.")
                )
            )
    
        # Entry point into validating a King instance.
        if isinstance(candidate, King):
            return cls._validate_king(
                candidate=candidate,
                identity_service=identity_service,
            )
        # Entry point into validating a King instance.
        if isinstance(candidate, Pawn):
            return cls._validate_pawn(
                candidate=candidate,
                indentify_service=identity_service,
            )
        # Entry point into validating a Knight instance.
        if isinstance(candidate, Knight):
            return cls._validate_knight(
                candidate=candidate,
                identity_service=identity_service
            )
        # Entry point into validating a Bishop instance.
        if isinstance(candidate, Bishop):
            return cls._validate_rook(
                candidate=candidate,
                identity_service=identity_service,
            )
        # Entry point into validating a Rook instance.
        if isinstance(candidate, Rook):
            return cls._validate_bishop(
                candidate=candidate,
                indentify_service=identity_service,
            )
        # Entry point into validating a Queen instance.
        if isinstance(candidate, Queen):
            return cls._validate_queen(
                candidate=candidate,
                identity_service=identity_service,
            )
        
        # Return the exception chain if there is no build route for the context.
        return ValidationResult.failure(
            RankValidationFailedException(
                message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                ex=RankBuildRouteException(f"{method}: {RankBuildRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_king(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[King]:
        method = "RankFactory._validate_king"
        
        # Handle the case that the candidate is not a King.
        if not isinstance(candidate, King):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a King, got {type(candidate).__name__} instead.")
                )
            )
        # Handle the case that the id is not certified safe.
        king = cast(King, candidate)
        id_validation = identity_service.validate_id(king.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that some of the params do match a King's
        if (
                king.ransom != Persona.KING.ransom or
                king.team_quota != Persona.KING.quota or
                king.name.upper() != Persona.KING.name.upper() or
                king.designation.upper() != Persona.KING.designation.upper()
        ):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=WrongingAttributeValueException(
                        f"{method}: {WrongKingAttributeValueException.DEFAUL_MESSAGE}")
                )
            )
        # On success send the king instance to the called.
        return ValidationResult.success(payload=king)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_pawn(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[Pawn]:
        method = "RankFactory._validate_pawn"
        
        # Handle the case that the candidate is not a Pawn.
        if not isinstance(candidate, Pawn):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a Pawn, got {type(candidate).__name__} instead.")
                )
            )
        # Handle the case that the id is not certified safe.
        pawn = cast(Pawn, candidate)
        id_validation = identity_service.validate_id(pawn.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.ex
                )
            )
        # Handle the case that some of the params do match a Pawn's
        if (
                pawn.ransom != Persona.PAWN.ransom or
                pawn.team_quota != Persona.PAWN.quota or
                pawn.name.upper() != Persona.PAWN.name.upper() or
                pawn.designation.upper() != Persona.PAWN.designation.upper()
        ):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=WrongPawnAttributeValueException(
                        f"{method}: {WrongPawnAttributeValueException.DEFAUL_MESSAGE}"
                    )
                )
            )
        # On success send the king instance to the called.
        return ValidationResult.success(pawn)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_knight(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[Knight]:
        method = "RankFactory._validate_knight"
        
        # Handle the case that the candidate is not a Knight.
        if not isinstance(candidate, Knight):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a Knight, got {type(candidate).__name__} instead.")
                )
            )
        # Handle the case that the id is not certified safe.
        knight = cast(Knight, candidate)
        id_validation = identity_service.validate_id(knight.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that some of the params do match a Knight's
        if (
                knight.ransom != Persona.KNIGHT.ransom or
                knight.team_quota != Persona.KNIGHT.quota or
                knight.name.upper() != Persona.KNIGHT.name.upper() or
                knight.designation.upper() != Persona.KNIGHT.designation.upper()
        ):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=WrongingAttributeValueException(
                        f"{method}: {WrongKnightAttributeValueException.DEFAUL_MESSAGE}"
                    )
                )
            )
        # On success send the knight instance to the called.
        return ValidationResult.success(payload=knight)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_bishop(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[Bishop]:
        method = "RankFactory._validate_bishop"
        
        # Handle the case that the candidate is not a Bishop.
        if not isinstance(candidate, Bishop):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a Bishop, got {type(candidate).__name__} instead.")
                )
            )
        # Handle the case that the id is not certified safe.
        bishop = cast(Bishop, candidate)
        id_validation = identity_service.validate_id(bishop.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.ex
                )
            )
        # Handle the case that some of the params do match a Bishop's
        if (
                bishop.ransom != Persona.BISHOP.ransom or
                bishop.team_quota != Persona.BISHOP.quota or
                bishop.name.upper() != Persona.BISHOP.name.upper() or
                bishop.designation.upper() != Persona.BISHOP.designation.upper()
        ):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=WrongBishopAttributeValueException(
                        f"{method}: {WrongBishopAttributeValueException.DEFAUL_MESSAGE}"
                    )
                )
            )
        # On success send the knight instance to the called.
        return ValidationResult.success(bishop)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_rook(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[Rook]:
        method = "RankFactory._validate_rook"
        
        # Handle the case that the candidate is not a Rook.
        if not isinstance(candidate, Rook):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a Rook, got {type(candidate).__name__} instead.")
                )
            )
        # Handle the case that the id is not certified safe.
        rook = cast(Rook, candidate)
        id_validation = identity_service.validate_id(rook.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that some of the params do match a Rook's
        if (
                rook.ransom != Persona.ROOK.ransom or
                rook.team_quota != Persona.ROOK.quota or
                rook.name.upper() != Persona.ROOK.name.upper() or
                rook.designation.upper() != Persona.ROOK.designation.upper()
        ):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=WrongingAttributeValueException(
                        f"{method}: {WrongRookAttributeValueException.DEFAUL_MESSAGE}"
                    )
                )
            )
        # On success send the rook instance to the called.
        return ValidationResult.success(payload=rook)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_queen(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[Queen]:
        method = "RankFactory._validate_queen"
        
        # Handle the case that the candidate is not a Queen.
        if not isinstance(candidate, Queen):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a Queen, got {type(candidate).__name__} instead.")
                )
            )
        # Handle the case that the id is not certified safe.
        queen = cast(Queen, candidate)
        id_validation = identity_service.validate_id(queen.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.ex
                )
            )
        # Handle the case that some of the params do match a Queen's
        if (
                queen.ransom != Persona.QUEEN.ransom or
                queen.team_quota != Persona.QUEEN.quota or
                queen.name.upper() != Persona.QUEEN.name.upper() or
                queen.designation.upper() != Persona.QUEEN.designation.upper()
        ):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RankValidationFailedException(
                    message=f"{method}: {RankValidationFailedException.DEFAULT_MESSAGE}",
                    ex=WrongQueenAttributeValueException(
                        f"{method}: {WrongQueenAttributeValueException.DEFAUL_MESSAGE}"
                    )
                )
            )
        # On success send the rook instance to the called.
        return ValidationResult.success(queen)


