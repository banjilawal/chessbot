# src/transit/dispatcher/attack/model/rank/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.rank.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import RankBlueprint
from transit.dispatcher.attack import ModelAttack
from err import RankAttackException
from domain.model import Rank
from artifcat import AttackResult, MethodResultType
from operation.toolkit import RankAttackToolkit
from util import LoggingLevelRouter


class RankAttack(ModelAttack[Rank]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Rank instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[RankAttackToolkit]

    Provides:
        -   def execute(self, blueprint: RankBlueprint) -> AttackResult[Rank]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[RankAttackToolkit] | None = RankAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[RankAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> RankAttackToolkit:
        return cast(RankAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RankBlueprint) -> AttackResult[Rank]:
        """
        Attack a safe Rank.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The RankBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Rank then, send in the success result,
        Args:
            blueprint: RankBlueprint
        Returns:
            AttackResult[Rank]
        Raises:
            RankAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                RankAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankAttackException.MSG,
                    err_code=RankAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            item=cast(
                RankBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                RankAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankAttackException.MSG,
                    err_code=RankAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Rank, assembly.payload))