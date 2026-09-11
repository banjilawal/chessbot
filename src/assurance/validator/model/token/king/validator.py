# src/assurance/validator/model/token/king/validator.py

"""
Module: assurance.validator.model.token.king.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from domain import KingTokenBlueprint, KingToken, HomeSquare, Rank
from transit import KingTokenCarrier
from util import LoggingLevelRouter


class KingTokenCarrierValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier and its contents instance is safe before use.

    Attributes:

    Provides:
        -   def execute(
                    id: int,
                    carrier: KingTokenCarrier,
                    home_square: HomeSquare,
            ) -> ValidationResult[KingTokenCarrier]

    Super Class:
    """
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            id: int,
            home_square: HomeSquare,
            validated_carrier: KingTokenCarrier,
    ) -> ValidationResult[KingTokenCarrier]:
        """
        Send a validated KingToken or Blueprint which inside the validated
        KingTokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a TokenCarrier or its null.
                    - The candidate is an empty TokenCarrier.
                    - Any Token attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            id: int
            home_square: HomeSquare
            validated_carrier: KingTokenCarrier
        Returns:
            ValidationResult[KingTokenCarrier]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"

        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = cast(KingTokenBlueprint, validated_carrier.extract_blueprint())

        if validated_carrier.is_carrying_model:
            model = KingToken(
                id=id,
                team=blueprint.team,
                home_square=home_square,
                formation=blueprint.formation,
            )
            model.rank = rank,
            model.captor = blueprint.captor
            model.readiness = blueprint.readiness
            model.deployment = blueprint.deployment
            model.position = blueprint.position
            model.current_position = model.previous_position
            
            return ValidationResult.success(
                KingTokenCarrier(model=model)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            KingTokenCarrier(blueprint=blueprint)
        )
    
    