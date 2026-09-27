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
    Coord, Formation, CombatantReadiness, PawnToken, HomeSquare, PawnTokenBlueprint,
    PawnTokenPrimeExtract, PromotionState, Rank, Team, TeamValidationRequest, TokenDeployment
)
from err import (
    CombatantReadinessNullException, FormationNullException, PawnTokenValidatorException, PromotionStateNullException,
    EmptyTeamCarrierException, EmptyPawnTokenCarrierException, TokenDeploymentNullException
)
from exchange import RankValidationRequest
from transit import PawnTokenCarrier, RankCarrier, TeamCarrier, TokenCarrier
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
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            deployment: TokenDeployment,
            prime_extract: PawnTokenPrimeExtract,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
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
            id: int
            team: Team
            formation: Formation
            home_square: HomeSquare
            deployment: TokenDeployment
            prime_extract: TokenPrimeExtract
            previous_position: Optional[Coord]
            position: Optional[Coord]
            
        Returns:
            ValidationResult[PawnTokenPrimeExtract]
        Raises:
            PawnTokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = prime_extract.blueprint
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
        validated_captor = blueprint.captor
        if blueprint.captor is not None:
            token_validation_
            captor_validation_result =
        
        # --- Extract validation payloads. ---#
        rank = cast(Rank, rank_validation.payload)
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        promotion_state = cast(PromotionState, promotion_state_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe PawnToken.
        if prime_extract.carrier.has_model:
            model = PawnToken(
                id=id,
                team=team,
                formation=formation,
                home_square=home_square,
            )
            model.readiness = readiness
            model.deployment = deployment
            model.rank = rank
            model.captor = blueprint.captor
            model.position = position
            model.promotion_state = promotion_state
            model.previous_position = previous_position
            return ValidationResult.success(TokenCarrier(model=model))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = VectorBlueprint(x=x, y=y)
        return ValidationResult.success(VectorCarrier(blueprint=payload))
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case.
        if prime_extract.has_model:
            model = PawnToken(
                id=id,
                team=team,
                home_square=home_square,
                formation=formation,
            )

            
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
    
    