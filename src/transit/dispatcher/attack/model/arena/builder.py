# src/transit/dispatcher/attack/model/arena/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.arena.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import ArenaBlueprint
from transit.dispatcher.attack import ModelAttack
from err import ArenaAttackException
from domain.model import Arena
from artifcat import AttackResult, MethodResultType
from operation.toolkit import ArenaAttackToolkit
from util import LoggingLevelRouter


class ArenaAttack(ModelAttack[Arena]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Arena instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[ArenaAttackToolkit]

    Provides:
        -   def execute(self, blueprint: ArenaBlueprint) -> AttackResult[Arena]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[ArenaAttackToolkit] | None = ArenaAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[ArenaAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> ArenaAttackToolkit:
        return cast(ArenaAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ArenaBlueprint) -> AttackResult[Arena]:
        """
        Attack a safe Arena.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The ArenaBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Arena then, send in the success result,
        Args:
            blueprint: ArenaBlueprint
        Returns:
            AttackResult[Arena]
        Raises:
            ArenaAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                ArenaAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaAttackException.MSG,
                    err_code=ArenaAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            candidate=cast(
                ArenaBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                ArenaAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaAttackException.MSG,
                    err_code=ArenaAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Arena, assembly.payload))