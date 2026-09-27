# src/assurance/validator/model/token/pawn/validator.py

"""
Module: assurance.validator.model.token.pawn.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import TokenValidatorToolkit
from domain import (
    Formation, CombatantReadiness, PawnToken, HomeSquare, PawnTokenBlueprint,
    PawnTokenPrimeExtract, PromotionState, Team, TeamValidationRequest, TokenDeployment
)
from err import (
    CombatantReadinessNullException, FormationNullException, PawnTokenValidatorException, PromotionStateNullException,
    EmptyTeamCarrierException, EmptyPawnTokenCarrierException, TokenDeploymentNullException
)
from transit import PawnTokenCarrier, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class PawnTokenValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PawnTokenCarrier is safe to use.

    Attributes:
        toolkit: TokenValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[PawnTokenCarrier]:

    Super Class:
    """
    _toolkit: TokenValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
        """
        self._toolkit=toolkit or TokenValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            prime_extract: PawnTokenPrimeExtract
    ) -> ValidationResult[PawnTokenPrimeExtract]:
        """
        Send a validated PawnToken or Blueprint which inside the validated
        PawnTokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The carrier is empty.
                    - The id check fails.
                    - The team check fails.
                    - The formation is null or the wrong type.
                    - The readiness is null or the wrong type.
                    - the deployment is null or the wrong type.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            prime_extract: PawnTokenCarrier
        Returns:
            ValidationResult[PawnTokenPrimeExtract]
        Raises:
            PawnTokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = prime_extract.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenValidatorException.MSG,
                    err_code=PawnTokenValidatorException.ERR_CODE,
                    ex=EmptyPawnTokenCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyPawnTokenCarrierException.MSG,
                        err_code=EmptyPawnTokenCarrierException.ERR_CODE,
                    ),
                )
            )



        # Handle the case that the readiness does not pass a validation check.
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

        # Handle the case that the deployment does not pass a validation check.
        promotion_state_validation = self._toolkit.wrapper.priming_validator.execute(
            candidate=blueprint.promotion_state,
            target_model=PromotionState,
            null_exception=PromotionStateNullException(),
        )
        if deployment_validation.is_failure:
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

        # --- Extract validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_carrier.entity)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        promotion_state = cast(PromotionState, promotion_state_validation.payload)
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case.
        if prime_extract.has_model:
            model = PawnToken(
                id=id,
                team=team,
                home_square=home_square,
                formation=formation,
            )
            model.readiness = readiness
            model.deployment = deployment
            model.rank = blueprint.rank
            model.captor = blueprint.captor
            model.position = blueprint.position
            model.promotion_state = promotion_state
            model.previous_position = model.previous_position
            
            return ValidationResult.success(PawnTokenCarrier(model=model))
        # Else the blueprint case
        return ValidationResult.success(
            PawnTokenCarrier(
                blueprint=PawnTokenBlueprint(
                    id=id,
                    team=team,
                    rank=blueprint.rank,
                    formation=formation,
                    readiness=readiness,
                    deployment=deployment,
                    home_square=home_square,
                    captor=blueprint.captor,
                    position=blueprint.position,
                    promotion_state=promotion_state,
                    previous_position=blueprint.previous_position,
            )
        )
    )
    
    