# src/transit/dispatcher/attack/struct/register/vector/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.register.vector.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import VectorRegisterBlueprint
from transit.dispatcher.attack import RegisterAttackDispatcher
from err import VectorRegisterAttackException
from domain.struct.register import VectorRegister
from artifcat import AttackResult, MethodResultType
from util import LoggingLevelRouter


class VectorRegisterAttack(RegisterAttackDispatcher[VectorRegister]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Register instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[VectorRegisterAttackToolkit]

    Provides:
        -   def execute(self, blueprint: RegisterVectorRegisteBlueprint) -> AttackResult[Register]

     Super Class:
         Attack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[VectorRegisterAttackToolkit] | 
                           None = VectorRegisterAttackToolkit()
    ):
        """
        Args:
            attack_toolkit: Optional[VectorRegisterAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> VectorRegisterAttackToolkit:
        return cast(VectorRegisterAttackToolkit, super().assembler)
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorRegisterBlueprint) -> AttackResult[VectorRegister]:
        """
        Attack a safe VectorRegister.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The bootstrap is not successful.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assemble product then, send in the success result,
        Args:
            blueprint: VectorRegisterBlueprint
        Returns:
            AttackResult[VectorRegister]
        Raises:
            VectorRegisterAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the bootstrap is not successful.
        blueprint_validation = self.attack_toolkit.bootstrapper.execute(job=blueprint)
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                VectorRegisterAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterAttackException.MSG,
                    err_code=VectorRegisterAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            candidate=cast(VectorRegisterBlueprint, blueprint_validation.payload)
        )
        if assembly.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                VectorRegisterAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterAttackException.MSG,
                    err_code=VectorRegisterAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(VectorRegister, assembly.payload))        