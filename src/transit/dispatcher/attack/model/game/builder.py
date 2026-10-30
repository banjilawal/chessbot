# src/transit/dispatcher/attack/model/game/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.game.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import GameBlueprint
from transit.dispatcher.attack import ModelAttack
from err import GameAttackException
from domain.model import Game
from artifcat import AttackResult, MethodResultType
from operation.toolkit import GameAttackToolkit
from util import LoggingLevelRouter


class GameAttack(ModelAttack[Game]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Game instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[GameAttackToolkit]

    Provides:
        -   def execute(self, blueprint: GameBlueprint) -> AttackResult[Game]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[GameAttackToolkit] | None = GameAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[GameAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> GameAttackToolkit:
        return cast(GameAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: GameBlueprint) -> AttackResult[Game]:
        """
        Attack a safe Game.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The GameBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Game then, send in the success result,
        Args:
            blueprint: GameBlueprint
        Returns:
            AttackResult[Game]
        Raises:
            GameAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.validator.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                GameAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameAttackException.MSG,
                    err_code=GameAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            candidate=cast(
                GameBlueprint,
                blueprint_validation.authorization_applicant
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                GameAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameAttackException.MSG,
                    err_code=GameAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Game, assembly.authorization_applicant))