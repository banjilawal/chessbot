# src/assurance/validator/struct/register/square/validator.py

"""
Module: assurance.validator.struct.register.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import RegisterValidator, SquareRegisterLoader, SquareRegisterLayerToolkit
from domain import Square, SquareRegister
from err import SquareRegisterConsistencyException, SquareRegisterValidatorException
from exchange import SquareValidationRequest
from transit import SquareCarrier
from util import IdFactory, LoggingLevelRouter


class SquareRegisterValidator(RegisterValidator[SquareRegister]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null Entity.
        2.  Run safety checks on structs and blueprints inside an Entity's payload.

    Attributes:
        loader: SquareRegisterLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[SquareRegister]:

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            loader: Optional[SquareRegisterLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[SquareRegisterLoader]
        """
        super().__init__(loader=loader or SquareRegisterLoader())
        
    @property
    def loader(self) -> SquareRegisterLoader:
        return cast(SquareRegisterLoader, super().loader)
    
    @property
    def toolkit(self) -> SquareRegisterLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[SquareRegister]:
        """
        Certify a SquareRegister's payload is either a SquareRegister or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a SquareRegisterValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a SquareRegister
                            an empty SquareRegister.
                    -   Either the square, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a  with the correct type of payload in the success
                result.
        Args:
            item: Any
        Returns:
            ValidationResult[SquareRegister]
        Raises:
            SquareRegisterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
                
        # Handle the case that loader fails.
        load = self.loader.execute(item)
        if load.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidatorException.MSG,
                    err_code=SquareRegisterValidatorException.ERR_CODE,
                    ex=load.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        struct = cast(SquareRegister, load.payload)
        
        if struct.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidatorException.MSG,
                    err_code=SquareRegisterValidatorException.ERR_CODE,
                    ex=SquareRegisterConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterConsistencyException.MSG,
                        err_code=SquareRegisterConsistencyException.ERR_CODE,
                    )
                )
            )
        
        entry = struct.to_dict
        endpoints: Dict[str, Square] = {}
        for key in struct.to_dict:
            square_validation = self.toolkit.dependency.square.extract_model(
                request=SquareValidationRequest(
                    item=SquareCarrier(model=entry[key]),
                    id=IdFactory.next_id(class_name="SquareRegisterRequest")
                )
            )
            if square_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterValidatorException.MSG,
                        err_code=SquareRegisterValidatorException.ERR_CODE,
                        ex=square_validation.exception
                    )
                )
            square = cast(Square, square_validation.payload)
            endpoints[key] = square
            
        # --- Forward the appropriate work product to the caller. ---#
        return ValidationResult.success(
            SquareRegister(
                origin=endpoints["origin"],
                destination=endpoints["destination"],
            )
        )

    
    
