# src/transit/dispatcher/attack/toggle/vector/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.toggle.vector.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import CartesianToggleBlueprint
from transit.dispatcher.attack import ToggleAttackDispatcher
from err import CartesianToggleAttackException
from artifcat import AttackResult, MethodResultType
from domain.struct.toggle import CartesianToggle
from operation.toolkit import CartesianToggleAttackToolkit
from util import LoggingLevelRouter


class CartesianToggleAttack(ToggleAttackDispatcher[CartesianToggle]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Picks toggle a
                - Coord: Geometric quantity
                - Vector: Linear Vector
            as an toggle for multiplication, conversion or simple addition.

    Attributes:
        attack_toolkit: Optional[CartesianToggleAttackToolkit]

    Provides:
        
        - _equal_vector_points(point: Point) -> bool
        - _equal_coord_points(self, point: Point) -> bool
    Super Class:
        ToggleAttack
    """
    
    def __init__(self, attack_toolkit: Optional[CartesianToggleAttackToolkit] |
                                        None = CartesianToggleAttackToolkit()
    ):
        """
        Args:
            attack_toolkit: Optional[CartesianToggleAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
        
    @property
    def attack_toolkit(self) -> CartesianToggleAttackToolkit:
        return cast(CartesianToggleAttackToolkit, super().assembler)
        
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CartesianToggleBlueprint,) -> AttackResult[CartesianToggle]:
        """
        Attack a safe CartesianToggle.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The bootstrap is not successful.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assemble product then, send in the success result,
        Args:
            blueprint: CartesianToggleBlueprint
        Returns:
            AttackResult[CartesianToggle]
        Raises:
            CartesianToggleAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the bootstrap is not successful.
        blueprint_validation = self.attack_toolkit.root_certifier.execute(job=blueprint)
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                CartesianToggleAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleAttackException.MSG,
                    err_code=CartesianToggleAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            candidate=cast(CartesianToggleBlueprint, blueprint_validation.payload)
        )
        if assembly.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                CartesianToggleAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleAttackException.MSG,
                    err_code=CartesianToggleAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(CartesianToggle, assembly.payload))