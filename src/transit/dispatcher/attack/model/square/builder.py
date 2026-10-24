# src/transit/dispatcher/attack/model/square/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.square.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import SquareBlueprint
from transit.dispatcher.attack import ModelAttack
from err import SquareAttackException
from domain.model import Square
from artifcat import AttackResult, MethodResultType
from operation.toolkit import SquareAttackToolkit
from util import LoggingLevelRouter


class SquareAttack(ModelAttack[Square]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Square instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[SquareAttackToolkit]

    Provides:
        -   def execute(self, blueprint: SquareBlueprint) -> AttackResult[Square]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[SquareAttackToolkit] | None = SquareAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[SquareAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> SquareAttackToolkit:
        return cast(SquareAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SquareBlueprint) -> AttackResult[Square]:
        """
        Attack a safe Square.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The SquareBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Square then, send in the success result,
        Args:
            blueprint: SquareBlueprint
        Returns:
            AttackResult[Square]
        Raises:
            SquareAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SquareAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareAttackException.MSG,
                    err_code=SquareAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(
                SquareBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                SquareAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareAttackException.MSG,
                    err_code=SquareAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Square, assembly.payload))