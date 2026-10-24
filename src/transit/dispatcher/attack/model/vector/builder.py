# src/transit/dispatcher/attack/model/vector/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.vector.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import VectorBlueprint
from transit.dispatcher.attack import ModelAttack
from err import VectorAttackException
from domain.model import Vector
from artifcat import AttackResult, MethodResultType
from operation.toolkit import VectorAttackToolkit
from util import LoggingLevelRouter


class VectorAttack(ModelAttack[Vector]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Vector instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[VectorAttackToolkit]

    Provides:
        -   def execute(self, blueprint: VectorBlueprint) -> AttackResult[Vector]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[VectorAttackToolkit] | None = VectorAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[VectorAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> VectorAttackToolkit:
        return cast(VectorAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorBlueprint) -> AttackResult[Vector]:
        """
        Attack a safe Vector.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The VectorBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Vector then, send in the success result,
        Args:
            blueprint: VectorBlueprint
        Returns:
            AttackResult[Vector]
        Raises:
            VectorAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                VectorAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAttackException.MSG,
                    err_code=VectorAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(
                VectorBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                VectorAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAttackException.MSG,
                    err_code=VectorAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Vector, assembly.payload))