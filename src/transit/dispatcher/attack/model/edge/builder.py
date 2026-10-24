# src/transit/dispatcher/attack/model/edge/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.edge.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import EdgeBlueprint
from transit.dispatcher.attack import ModelAttack
from err import EdgeAttackException
from domain.model import Edge
from artifcat import AttackResult, MethodResultType
from operation.toolkit import EdgeAttackToolkit
from util import LoggingLevelRouter


class EdgeAttack(ModelAttack[Edge]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Edge instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[EdgeAttackToolkit]

    Provides:
        -   def execute(self, blueprint: EdgeBlueprint) -> AttackResult[Edge]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[EdgeAttackToolkit] | None = EdgeAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[EdgeAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> EdgeAttackToolkit:
        return cast(EdgeAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: EdgeBlueprint) -> AttackResult[Edge]:
        """
        Attack a safe Edge.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The EdgeBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Edge then, send in the success result,
        Args:
            blueprint: EdgeBlueprint
        Returns:
            AttackResult[Edge]
        Raises:
            EdgeAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.validator.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                EdgeAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EdgeAttackException.MSG,
                    err_code=EdgeAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(
                EdgeBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                EdgeAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EdgeAttackException.MSG,
                    err_code=EdgeAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Edge, assembly.payload))