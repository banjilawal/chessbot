# src/transit/dispatcher/attack/model/board/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.board.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import BoardBlueprint
from transit.dispatcher.attack import ModelAttack
from err import BoardAttackException
from domain.model import Board
from artifcat import AttackResult, MethodResultType
from operation.toolkit import BoardAttackToolkit
from util import LoggingLevelRouter


class BoardAttack(ModelAttack[Board]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Board instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[BoardAttackToolkit]

    Provides:
        -   def execute(self, blueprint: BoardBlueprint) -> AttackResult[Board]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[BoardAttackToolkit] | None = BoardAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[BoardAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> BoardAttackToolkit:
        return cast(BoardAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: BoardBlueprint) -> AttackResult[Board]:
        """
        Attack a safe Board.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The BoardBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Board then, send in the success result,
        Args:
            blueprint: BoardBlueprint
        Returns:
            AttackResult[Board]
        Raises:
            BoardAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                BoardAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardAttackException.MSG,
                    err_code=BoardAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            candidate=cast(
                BoardBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                BoardAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardAttackException.MSG,
                    err_code=BoardAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Board, assembly.payload))