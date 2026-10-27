# src/transit/dispatcher/attack/model/snapshot/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.snapshot.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import SnapshotBlueprint
from transit.dispatcher.attack import ModelAttack
from err import SnapshotAttackException
from domain.model import Snapshot
from artifcat import AttackResult, MethodResultType
from operation.toolkit import SnapshotAttackToolkit
from util import LoggingLevelRouter


class SnapshotAttack(ModelAttack[Snapshot]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Snapshot instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[SnapshotAttackToolkit]

    Provides:
        -   def execute(self, blueprint: SnapshotBlueprint) -> AttackResult[Snapshot]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[SnapshotAttackToolkit] | None = SnapshotAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[SnapshotAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> SnapshotAttackToolkit:
        return cast(SnapshotAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SnapshotBlueprint) -> AttackResult[Snapshot]:
        """
        Attack a safe Snapshot.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The SnapshotBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Snapshot then, send in the success result,
        Args:
            blueprint: SnapshotBlueprint
        Returns:
            AttackResult[Snapshot]
        Raises:
            SnapshotAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.validator.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SnapshotAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SnapshotAttackException.MSG,
                    err_code=SnapshotAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            item=cast(
                SnapshotBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                SnapshotAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SnapshotAttackException.MSG,
                    err_code=SnapshotAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Snapshot, assembly.payload))