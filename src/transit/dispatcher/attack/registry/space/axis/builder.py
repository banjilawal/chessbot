# src/transit/dispatcher/attack/registry/space/axis/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.registry.space.axis.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import AxisReservoirBlueprint
from transit.dispatcher.attack import SpaceReservoirAttackDispatcher
from err import AxisReservoirAttackException
from surface.topology import AxisReservoir
from artifcat import AttackResult, MethodResultType
from operation.toolkit import AxisReservoirAttackToolkit
from util import LoggingLevelRouter


class AxisReservoirAttack(SpaceReservoirAttackDispatcher[AxisReservoir]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Axis instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[AxisReservoirAttackToolkit]

    Provides:
        -   def execute(self, blueprint: AxisReservoirBlueprint) -> AttackResult[Axis]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[AxisReservoirAttackToolkit] |
                             None = AxisReservoirAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[AxisReservoirAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> AxisReservoirAttackToolkit:
        return cast(AxisReservoirAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AxisReservoirBlueprint) -> AttackResult[AxisReservoir]:
        """
        Attack a safe Axis.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The AxisReservoirBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Axis then, send in the success result,
        Args:
            blueprint: AxisReservoirBlueprint
        Returns:
            AttackResult[Axis]
        Raises:
            AxisReservoirAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                AxisReservoirAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisReservoirAttackException.MSG,
                    err_code=AxisReservoirAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            candidate=cast(AxisReservoirBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                AxisReservoirAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisReservoirAttackException.MSG,
                    err_code=AxisReservoirAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(AxisReservoir, assembly.payload))