# src/transit/dispatcher/attack/model/player/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.player.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import PlayerBlueprint
from transit.dispatcher.attack import ModelAttack
from err import PlayerAttackException
from domain.model import Player
from artifcat import AttackResult, MethodResultType
from operation.toolkit import PlayerAttackToolkit
from util import LoggingLevelRouter


class PlayerAttack(ModelAttack[Player]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Player instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[PlayerAttackToolkit]

    Provides:
        -   def execute(self, blueprint: PlayerBlueprint) -> AttackResult[Player]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[PlayerAttackToolkit] | None = PlayerAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[PlayerAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> PlayerAttackToolkit:
        return cast(PlayerAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: PlayerBlueprint) -> AttackResult[Player]:
        """
        Attack a safe Player.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The PlayerBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Player then, send in the success result,
        Args:
            blueprint: PlayerBlueprint
        Returns:
            AttackResult[Player]
        Raises:
            PlayerAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                PlayerAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerAttackException.MSG,
                    err_code=PlayerAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(
                PlayerBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                PlayerAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerAttackException.MSG,
                    err_code=PlayerAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Player, assembly.payload))