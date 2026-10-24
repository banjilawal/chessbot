# src/transit/dispatcher/attack/registry/space/quadrant/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.registry.space.quadrant.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import QuadrantReservoirBlueprint
from transit.dispatcher.attack import SpaceReservoirAttackDispatcher
from err import QuadrantReservoirAttackException
from surface.topology import QuadrantReservoir
from artifcat import AttackResult, MethodResultType
from operation.toolkit import QuadrantReservoirAttackToolkit
from util import LoggingLevelRouter


class QuadrantReservoirAttack(SpaceReservoirAttackDispatcher[QuadrantReservoir]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Quadrant instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[QuadrantReservoirAttackToolkit]

    Provides:
        -   def execute(self, blueprint: QuadrantReservoirBlueprint) -> AttackResult[Quadrant]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[QuadrantReservoirAttackToolkit] |
                             None = QuadrantReservoirAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[QuadrantReservoirAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> QuadrantReservoirAttackToolkit:
        return cast(QuadrantReservoirAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: QuadrantReservoirBlueprint) -> AttackResult[QuadrantReservoir]:
        """
        Attack a safe Quadrant.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The QuadrantReservoirBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Quadrant then, send in the success result,
        Args:
            blueprint: QuadrantReservoirBlueprint
        Returns:
            AttackResult[Quadrant]
        Raises:
            QuadrantReservoirAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                QuadrantReservoirAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantReservoirAttackException.MSG,
                    err_code=QuadrantReservoirAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(QuadrantReservoirBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                QuadrantReservoirAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantReservoirAttackException.MSG,
                    err_code=QuadrantReservoirAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(QuadrantReservoir, assembly.payload))