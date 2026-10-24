# src/transit/dispatcher/attack/model/token/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.token.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import TokenBlueprint
from transit.dispatcher.attack import ModelAttack
from err import TokenAttackException
from domain.model import Token
from artifcat import AttackResult, MethodResultType
from operation.toolkit import TokenAttackToolkit
from util import LoggingLevelRouter


class TokenAttack(ModelAttack[Token]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

    Attributes:
            attack_toolkit: Optional[TokenAttackToolkit]

    Provides:
        -   def execute(self, blueprint: TokenBlueprint) -> AttackResult[Token]

     Super Class:
         ModelAttack
     """
    
    def __init__(
            self,
            attack_toolkit: Optional[TokenAttackToolkit] |
                             None = TokenAttackToolkit(),
    ):
        """
        Args:
            attack_toolkit: Optional[TokenAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> TokenAttackToolkit:
        return cast(TokenAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> AttackResult[Token]:
        """
        Attack a safe Token.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The TokenBlueprint object is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Token then, send in the success result,
        Args:
            blueprint: TokenBlueprint
        Returns:
            AttackResult[Token]
        Raises:
            TokenAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                TokenAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenAttackException.MSG,
                    err_code=TokenAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(TokenBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
        # Send the exception chain on failure.
            return AttackResult.failure(
                TokenAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenAttackException.MSG,
                    err_code=TokenAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(Token, assembly.payload))