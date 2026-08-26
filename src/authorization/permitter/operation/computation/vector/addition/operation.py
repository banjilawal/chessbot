# src/operation/computation/vector/addition/operation.py

"""
Module: operation.computation.vector.addition.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional


from transit.dispatcher.builder import RegisterBuilder, VectorToggleRegisterBuilder
from selector import VectorToggle

from operation.utility import VectorToggleUtility
from artifcat import ComputationResult
from util import LoggingLevelRouter


class AddVector(Computation[VectorToggle]):
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Compute the contents of a VectorRegister to each other producing either a new Vector or a Coord.

    Attributes:
            permitter: Optional[AddVectorPermitter]
            
    Provides:
        -   def execute(self, request: AddVectorRequest) -> ComputationResult[VectorToggle]

    Super Class:
        Computation
    """
    
    def __init__(self, permitter: Optional[AddVectorPermitter] | None = None):
        """
        Args:
            permitter: Optional[AddVectorPermitter]
        """
        super().__init__(permitter=permitter or AddVectorPermitter())
        
    @property
    def permitter(self) -> AddVectorPermitter:
        return cast(AddVectorPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorRequest) -> ComputationResult[VectorToggle]:
        pass
    
    
    _register_builder: Optional[RegisterBuilder]
    _vector_toggle_utility: Optional[VectorToggleUtility]
    
    def __init__(
            self,
            register_builder: Optional[VectorToggleRegisterBuilder]
                              | None = VectorToggleRegisterBuilder(),
            vector_toggle_utility: Optional[VectorToggleUtility] | None = VectorToggleUtility(),
    ):
        """
        Args:
            register_builder: Optional[VectorToggleRegisterBuilder]
            vector_toggle_utility: Optional[VectorToggleUtility]
        """
        self._register_builder = register_builder
        self._vector_toggle_utility = vector_toggle_utility
        
    @LoggingLevelRouter.monitor
    def execute(
            self,
            u: VectorToggle,
            v: VectorToggle,
    ) -> ComputationResult[VectorToggle]:
        """
        Add the contents of a VectorRegister to each other.
        
        Action:
            1.  Send an exception chain in the ComputationResult if any of
                these conditions occur
                    -   The operand is null
                    -   The operand is flagged unsafe.
                    -   Building the other type fails.
            2.  Otherwise, send the success result.
        Args:
            scalar: Scalar,
            register: VectorRegister,
            utility : VectorRegisterUtility = VectorRegisterUtility(),
            register_validator: VectorRegisterValidator = VectorRegisterValidator(),
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{self.__class__.__name__}.execute"
        
        register_build_result =
        for operand in [u, v]:
            validation = self._vector_toggle_utility.v
        
        if register_validator is None:
            register_validator = VectorRegisterValidator()
            
        if operand_utility is None:
            operand_utility = VectorToggleUtility()
            
        
        
        # Handle the case that, the register is not valid for addition.
        register_validation_result = register_validator.execute(register)
        if register_validation_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                VectorAdditionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=register_validation_result.exception
                )
        )
        build_result = None
        if register.is_vector_register:
            blueprint = VectorBlueprint(
                x=register.a.entity.x + register.b.entity.x,
                y=register.a.entity.y + register.b.entity.y,
            )
            build_result = operand_utility.vector_builder.execute(
                blueprint=blueprint,
            )
        if register.category == RegisterContentType.COORD_REGISTER:
            blueprint = CoordBlueprint(
                row=register.a.entity.row + register.b.entity.row,
                column=register.a.entity.column + register.b.entity.column,
            )
            build_result = operand_utility.coord_builder.execute(
                blueprint=blueprint,
            )
        # Handle the case that, the build did not produce a result.
        if build_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                VectorAdditionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=build_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(build_result.payload)

        