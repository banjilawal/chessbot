# src/transit/dispatcher/attack/space/axis/north/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.axis.north.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import NorthAxisBlueprint
from transit.dispatcher.attack import AxisAttack
from err import NorthAxisAttackException
from artifcat import AttackResult, MethodResultType
from surface.space import NorthAxis
from operation.toolkit import NorthAxisAttackToolkit
from util import LoggingLevelRouter


class NorthAxisAttack(AxisAttack[NorthAxis]):
    """
    Role:
        - Attack
        - Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            attack_toolkit: Optional[NorthAxisAttackToolkit]

    Provides:
        -   def execute(origin: Vector) -> AttackResult[EastAxis]

    Super Class:
        AxisAttack
    """
    def __init__(
            self, 
            attack_toolkit: Optional[NorthAxisAttackToolkit] | None = None,
    ):
        """
        Args:
            attack_toolkit: Optional[NorthAxisAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit or NorthAxisAttackToolkit())
    
    @LoggingLevelRouter.monitor
    def execute( self, blueprint: NorthAxisBlueprint) -> AttackResult[NorthAxis]:
        """
        Attack a safe NorthAxis.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The blueprint is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a NorthAxis then,
                send in the success result,
        Args:
            blueprint: NorthAxisBlueprint
        Returns:
            AttackResult[NorthAxis]
        Raises:
            NorthAxisAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                NorthAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisAttackException.MSG,
                    err_code=NorthAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            blueprint=cast(NorthAxisBlueprint, validation.authorization_applicant)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                NorthAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisAttackException.MSG,
                    err_code=NorthAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(NorthAxis, assembly.authorization_applicant))