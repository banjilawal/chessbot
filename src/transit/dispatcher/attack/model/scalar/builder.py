# src/transit/dispatcher/attack/model/scalar/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.scalar.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import ScalarBlueprint
from transit.dispatcher.attack import ModelAttack
from err import ScalarAttackException
from domain.model import Scalar
from artifcat import AttackResult, MethodResultType
from operation.toolkit import ScalarAttackToolkit
from util import LoggingLevelRouter


class ScalarAttack(ModelAttack[Scalar]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Scalar instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[ScalarAttackToolkit]

    Provides:
        -   def execute(self, blueprint: ScalarBlueprint) -> AttackResult[Scalar]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[ScalarAttackToolkit] | None = ScalarAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[ScalarAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> ScalarAttackToolkit:
        return cast(ScalarAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ScalarBlueprint) -> AttackResult[Scalar]:
        """
        Attack a safe Scalar.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The ScalarBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Scalar then, send in the success result,
        Args:
            blueprint: ScalarBlueprint
        Returns:
            AttackResult[Scalar]
        Raises:
            ScalarAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                ScalarAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarAttackException.MSG,
                    err_code=ScalarAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            item=cast(
                ScalarBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                ScalarAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarAttackException.MSG,
                    err_code=ScalarAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Scalar, assembly.payload))