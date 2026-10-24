# src/transit/dispatcher/attack/model/struct/node/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.node.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import NodeBlueprint
from transit.dispatcher.attack import ModelAttack
from err import NodeAttackException
from domain.model import Node
from artifcat import AttackResult, MethodResultType
from operation.toolkit import NodeAttackToolkit
from util import LoggingLevelRouter


class NodeAttack(ModelAttack[Node]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Node instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[NodeAttackToolkit]

    Provides:
        -   def execute(self, blueprint: NodeBlueprint) -> AttackResult[Node]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[NodeAttackToolkit] | None = NodeAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[NodeAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> NodeAttackToolkit:
        return cast(NodeAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: NodeBlueprint) -> AttackResult[Node]:
        """
        Attack a safe Node.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The NodeBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Node then, send in the success result,
        Args:
            blueprint: NodeBlueprint
        Returns:
            AttackResult[Node]
        Raises:
            NodeAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.validator.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                NodeAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NodeAttackException.MSG,
                    err_code=NodeAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(
                NodeBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                NodeAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NodeAttackException.MSG,
                    err_code=NodeAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Node, assembly.payload))