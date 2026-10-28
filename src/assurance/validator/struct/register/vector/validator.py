# src/assurance/validator/struct/register/vector/validator.py

"""
Module: assurance.validator.struct.register.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import RegisterValidator, VectorRegisterLoader, VectorRegisterLayerToolkit
from domain import Vector, VectorRegister
from err import VectorRegisterConsistencyException, VectorRegisterValidatorException
from exchange import VectorValidationRequest
from transit import VectorCarrier
from util import IdFactory, LoggingLevelRouter


class VectorRegisterValidator(RegisterValidator[VectorRegister]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null Entity.
        2.  Run safety checks on structs and blueprints inside an Entity's payload.

    Attributes:
        loader: VectorRegisterLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[VectorRegister]:

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            loader: Optional[VectorRegisterLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[VectorRegisterLoader]
        """
        super().__init__(loader=loader or VectorRegisterLoader())
        
    @property
    def loader(self) -> VectorRegisterLoader:
        return cast(VectorRegisterLoader, super().loader)
    
    @property
    def toolkit(self) -> VectorRegisterLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[VectorRegister]:
        """
        Certify a VectorRegister's payload is either a VectorRegister or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a VectorRegisterValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a VectorRegister
                            an empty VectorRegister.
                    -   Either the vector, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a  with the correct type of payload in the success
                result.
        Args:
            item: Any
        Returns:
            ValidationResult[VectorRegister]
        Raises:
            VectorRegisterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
                
        # Handle the case that loader fails.
        load = self.loader.execute(item)
        if load.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidatorException.MSG,
                    err_code=VectorRegisterValidatorException.ERR_CODE,
                    ex=load.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        struct = cast(VectorRegister, load.payload)
        
        if struct.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidatorException.MSG,
                    err_code=VectorRegisterValidatorException.ERR_CODE,
                    ex=VectorRegisterConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorRegisterConsistencyException.MSG,
                        err_code=VectorRegisterConsistencyException.ERR_CODE,
                    )
                )
            )
        
        entry = struct.to_dict
        endpoints: Dict[str, Vector] = {}
        for key in struct.to_dict:
            vector_validation = self.toolkit.dependency.vector.extract_model(
                request=VectorValidationRequest(
                    item=VectorCarrier(model=entry[key]),
                    id=IdFactory.next_id(class_name="VectorRegisterRequest")
                )
            )
            if vector_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorRegisterValidatorException.MSG,
                        err_code=VectorRegisterValidatorException.ERR_CODE,
                        ex=vector_validation.exception
                    )
                )
            vector = cast(Vector, vector_validation.payload)
            endpoints[key] = vector
            
        # --- Forward the appropriate work product to the caller. ---#
        return ValidationResult.success(
            VectorRegister(
                origin=endpoints["origin"],
                destination=endpoints["destination"],
            )
        )

    
    
