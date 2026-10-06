# src/assurance/validator/model/token/pawn/validator.py

"""
Module: assurance.validator.payload.token.pawn.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import TokenProductEnvelope, TokenEnemyValidator, TokenValidatorToolkit
from domain import (
    CombatantReadiness, PawnToken, PawnTokenBlueprint, PawnTokenPrimeExtract, PromotionState,
    Rank, Token
)
from err import (
    CombatantReadinessNullException, TokenProductEnvelopeNullException,
    PawnTokenPrimeExtractNullException, PawnTokenValidatorException,
    PromotionStateNullException
)
from exchange import RankValidationRequest, TokenValidationRequest
from transit import PawnTokenCarrier, RankCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class PawnTokenValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PawnTokenCarrier is safe to use.

    Attributes:
        loader: TokenValidatorToolkit
        enemy_validator: TokenEnemyValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[PawnTokenCarrier]:

    Super Class:
    """
    _loader: TokenValidatorToolkit
    _enemy_validator: TokenEnemyValidator
    
    def __init__(
            self,
            loader: Optional[TokenValidatorToolkit] | None = None,
            enemy_validator: Optional[TokenEnemyValidator] | None = None,
    ):
        """
        Args:
            loader: Optional[TokenValidatorToolkit]
            enemy_validator: Optional[TokenEnemyValidator]
        """
        self._toolkit = toolkit or TokenValidatorToolkit()
        self._enemy_validator = enemy_validator or TokenEnemyValidator()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            validation_reference: TokenProductEnvelope
    ) -> ValidationResult[PawnTokenCarrier]:
        """
        Assure the properties can assemble a safe PawnTokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                fields are flagged.
                    -   captor
                    -   rank
                    -   promotion_state
                    -   combatant_readiness
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            validation_reference: TokenProductEnvelope
        Returns:
            ValidationResult[PawnTokenCarrier]
        Raises:
            PawnTokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the property table is null or the wrong type.
        table_validation = self._toolkit.priming_validator.execute(
            candidate=validation_reference,
            target_model=Type[TokenProductEnvelope],
            null_exception=TokenProductEnvelopeNullException(),
        )
        if table_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenValidatorException.MSG,
                    err_code=PawnTokenValidatorException.ERR_CODE,
                    ex=table_validation.exception
                )
            )
        # Handle the case that the property table has the wrong PrimeExtract.
        extract_validation = self._toolkit.priming_validator.execute(
            candidate=validation_reference.prime_extract,
            target_model=Type[PawnTokenPrimeExtract],
            null_exception=PawnTokenPrimeExtractNullException(),
        )
        if extract_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenValidatorException.MSG,
                    err_code=PawnTokenValidatorException.ERR_CODE,
                    ex=extract_validation.exception
                )
            )
        # Handle the case that there is no blueprint in the carrier.
        prime_extract = cast(PawnTokenPrimeExtract, validation_reference.prime_extract)
        blueprint = cast(PawnTokenBlueprint, prime_extract.blueprint)
        # --- START_COMBATANT_TOKEN_READINESS_VALIDATION_PROCESS ---#
        
        # Handle the case that the readiness is flagged.
        readiness_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=CombatantReadiness,
            null_exception=CombatantReadinessNullException(),
        )
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenValidatorException.MSG,
                    err_code=PawnTokenValidatorException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # --- START_PROMOTION_STATE_VALIDATION_PROCESS ---#
        
        # Handle the case that the promotion_state is flagged.
        promotion_state_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.promotion_state,
            target_model=PromotionState,
            null_exception=PromotionStateNullException(),
        )
        if promotion_state_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenValidatorException.MSG,
                    err_code=PawnTokenValidatorException.ERR_CODE,
                    ex=promotion_state_validation.exception,
                )
            )
        # --- START_RANK_VALIDATION_PROCESS ---#
        
        # Handle the case that the rank is flagged.
        rank_validation = self._toolkit.wrapper.rank.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=blueprint.rank),
                id=IdFactory.next_id(class_name="RankValidationRequest"),
            )
        )
        if rank_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenValidatorException.MSG,
                    err_code=PawnTokenValidatorException.ERR_CODE,
                    ex=rank_validation.exception,
                )
            )
        # --- START_CAPTOR_VALIDATION_PROCESS ---#
        
        captor_placeholder = blueprint.captor
        if blueprint.captor is not None:
            # Handle the case that the not-null captor is flagged
            enemy_validation_result = self._enemy_validator.execute(
                request=TokenValidationRequest(
                    item=TokenCarrier(model=blueprint.captor),
                    id=IdFactory.next_id(class_name="TokenValidationRequest"),
                )
            )
            if enemy_validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PawnTokenValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PawnTokenValidatorException.MSG,
                        err_code=PawnTokenValidatorException.ERR_CODE,
                        ex=enemy_validation_result.exception,
                    )
                )
            # Otherwise update captor_placeholder
            captor_placeholder = cast(Token, enemy_validation_result.payload)

        # --- Extract validation payloads. ---#
        rank = cast(Rank, rank_validation.payload)
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        promotion_state = cast(PromotionState, promotion_state_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe PawnToken.
        if prime_extract.reference.has_model:
            payload = PawnToken(
                id=validation_reference.safe.id,
                team=validation_reference.safe.team,
                formation=validation_reference.safe.formation,
                home_square=validation_reference.safe.home_square,
            )
            payload.rank = rank
            payload.readiness = readiness
            payload.captor = captor_placeholder
            payload.promotion_state = promotion_state
            payload.deployment = validation_reference.safe.deployment
            payload.position = validation_reference.safe.position
            payload.previous_position = validation_reference.safe.previous_position
            
            return ValidationResult.success(PawnTokenCarrier(model=payload))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = PawnTokenBlueprint(
            id=validation_reference.safe.id,
            team=validation_reference.safe.team,
            formation=validation_reference.safe.formation,
            home_square=validation_reference.safe.home_square,
            deployment=validation_reference.safe.deployment,
            position=validation_reference.safe.position,
            previous_position=validation_reference.safe.previous_position,
            promotion_state=promotion_state,
            captor=captor_placeholder,
            readiness=readiness,
            rank=rank,
        )
        return ValidationResult.success(PawnTokenCarrier(blueprint=payload))
    
    