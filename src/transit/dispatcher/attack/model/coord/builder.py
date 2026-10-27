# src/transit/dispatcher/attack/model/coord/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.coord.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import CoordBlueprint
from transit.dispatcher.attack import ModelAttack
from err import CoordAttackException
from domain.model import Coord
from artifcat import AttackResult, MethodResultType
from operation.toolkit import CoordAttackToolkit
from util import LoggingLevelRouter


class CoordAttack(ModelAttack[Coord]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Coord instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[CoordAttackToolkit]

    Provides:
        -   def execute(self, blueprint: CoordBlueprint) -> AttackResult[Coord]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[CoordAttackToolkit] | None = CoordAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[CoordAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> CoordAttackToolkit:
        return cast(CoordAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CoordBlueprint) -> AttackResult[Coord]:
        """
        Attack a safe Coord.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The CoordBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Coord then, send in the success result,
        Args:
            blueprint: CoordBlueprint
        Returns:
            AttackResult[Coord]
        Raises:
            CoordAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                CoordAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordAttackException.MSG,
                    err_code=CoordAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            item=cast(
                CoordBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                CoordAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordAttackException.MSG,
                    err_code=CoordAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Coord, assembly.payload))