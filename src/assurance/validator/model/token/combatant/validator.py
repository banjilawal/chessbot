# src/assurance/validator/model/token/combatant/validator.py

"""
Module: assurance.validator.payload.token.combatant.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import (
    TokenProductEnvelope, TokenEnemyValidator, TokenValidatorToolkit
)
from domain import (
    CombatantReadiness, CombatantToken, CombatantTokenBlueprint,
    CombatantTokenPrimeExtract, Token, TokenDeployment
)
from err import (
    CombatantReadinessNullException, CombatantTokenPrimeExtractNullException,
    CombatantTokenValidatorException, TokenProductEnvelopeNullException
)
from exchange import TokenValidationRequest
from transit import CombatantTokenCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class CombatantTokenValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CombatantTokenCarrier is safe to use.

    Attributes:
        loader: TokenValidatorToolkit
        enemy_validator: TokenEnemyValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[CombatantTokenCarrier]:

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
            reference: TokenProductEnvelope
    ) -> ValidationResult[CombatantTokenCarrier]:
        """
        Assure the properties can assemble a safe CombatantTokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                fields are flagged.
                    -   captor
                    -   combatant_readiness
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            reference: TokenProductEnvelope
        Returns:
            ValidationResult[CombatantTokenCarrier]
        Raises:
            CombatantTokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the property table is null or the wrong type.
        priming = self._toolkit.priming_validator.execute(
            candidate=reference,
            target_model=Type[TokenProductEnvelope],
            null_exception=TokenProductEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # Handle the case that the property table has the wrong PrimeExtract.
        extract_validation = self._toolkit.priming_validator.execute(
            candidate=reference.prime_extract,
            target_model=Type[CombatantTokenPrimeExtract],
            null_exception=CombatantTokenPrimeExtractNullException(),
        )
        if extract_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
                    ex=extract_validation.exception
                )
            )
        # Handle the case that there is no blueprint in the carrier.
        extract = cast(CombatantTokenPrimeExtract, extract_validation.payload)
        blueprint = cast(CombatantTokenBlueprint, extract.blueprint)
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
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # --- START_CAPTOR_VALIDATION_PROCESS ---#
        
        captor = blueprint.captor
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
                    CombatantTokenValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CombatantTokenValidatorException.MSG,
                        err_code=CombatantTokenValidatorException.ERR_CODE,
                        ex=enemy_validation_result.exception,
                    )
                )
            # Otherwise update captor_placeholder
            captor = cast(Token, enemy_validation_result.payload)

        # --- Extract validation payloads. ---#
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe CombatantToken.
        if extract.reference.has_model:
            payload = CombatantToken(
                id=reference.safe.id,
                team=reference.safe.team,
                formation=reference.safe.formation,
                home_square=reference.safe.home_square,
            )
            payload.readiness = readiness
            payload.captor = captor
            payload.position = reference.safe.position
            payload.previous_position = reference.safe.previous_position
            if reference.safe.deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE:
                payload.mark_as_deployed()
            return ValidationResult.success(CombatantTokenCarrier(model=payload))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = CombatantTokenBlueprint(
            id=reference.safe.id,
            team=reference.safe.team,
            formation=reference.safe.formation,
            home_square=reference.safe.home_square,
            deployment=reference.safe.deployment,
            position=reference.safe.position,
            previous_position=reference.safe.previous_position,
            captor=captor,
            readiness=readiness,
        )
        return ValidationResult.success(CombatantTokenCarrier(blueprint=payload))
    
    