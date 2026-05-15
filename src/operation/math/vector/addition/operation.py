# src/operation/vector/addition/operation.py

"""
Module: operation.vector.addition.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from result import ComputationResult
from util import LoggingLevelRouter
from err import VectorAdditionException
from toolkit import VectorOperandToolkit
from operation import Operation, VectorRegisterValidator
from model import Coord, CoordBlueprint, RegisterCategory, Vector, VectorBlueprint, VectorRegister


class AddOperation(Operation[VectorRegister]):
    """
    Role:
        -   Operation
        -   Computation

    Responsibilities:
        1.  Compute the contents of a VectorRegister to each other producing either a new Vector or a Coord.

    Attributes:

    Properties:
    
    -   def execute(
            register: VectorRegister,
            toolkit : VectorRegisterToolkit = VectorRegisterToolkit(),
            register_validator: VectorRegisterValidator = VectorRegisterValidator(),
        ) -> ComputationResult[Any]:

    Super Class:
        Operation
    """
    NAME = "vector_addition"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            register: VectorRegister,
            register_validator: VectorRegisterValidator | None = None,
            operand_toolkit: VectorOperandToolkit | None = None,
    ) -> ComputationResult[Coord|Vector]:
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
            toolkit : VectorRegisterToolkit = VectorRegisterToolkit(),
            register_validator: VectorRegisterValidator = VectorRegisterValidator(),
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.execute"
        
        if register_validator is None:
            register_validator = VectorRegisterValidator()
            
        if operand_toolkit is None:
            operand_toolkit = VectorOperandToolkit()
        
        # Handle the case that, the register is not valid for addition.
        register_validation_result = register_validator.validate(register)
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
        if register.category == RegisterCategory.VECTOR_REGISTER:
            blueprint = VectorBlueprint(
                x=register.a.vector.x + register.b.vector.x,
                y=register.a.vector.y + register.b.vector.y,
            )
            build_result = operand_toolkit.vector_builder.run(
                blueprint=blueprint,
            )
        if register.category == RegisterCategory.COORD_REGISTER:
            blueprint = CoordBlueprint(
                row=register.a.coord.row + register.b.coord.row,
                column=register.a.coord.column + register.b.coord.column,
            )
            build_result = operand_toolkit.coord_builder.run(
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

# Register the operation.
WorkerRegistryController.register_worker(worker=AddOperation)
        