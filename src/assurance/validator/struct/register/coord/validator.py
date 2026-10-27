# src/assurance/validator/struct/register/coord/validator.py

"""
Module: assurance.validator.struct.register.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import RegisterValidator, CoordRegisterLoader, CoordRegisterLayerToolkit
from domain import Coord, CoordRegister
from err import CoordRegisterConsistencyException, CoordRegisterValidatorException
from exchange import CoordValidationRequest
from transit import CoordCarrier
from util import IdFactory, LoggingLevelRouter


class CoordRegisterValidator(RegisterValidator[CoordRegister]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null Entity.
        2.  Run safety checks on structs and blueprints inside an Entity's payload.

    Attributes:
        loader: CoordRegisterLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[CoordRegister]:

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            loader: Optional[CoordRegisterLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[CoordRegisterLoader]
        """
        super().__init__(loader=loader or CoordRegisterLoader())
        
    @property
    def loader(self) -> CoordRegisterLoader:
        return cast(CoordRegisterLoader, super().loader)
    
    @property
    def toolkit(self) -> CoordRegisterLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordRegister]:
        """
        Certify a CoordRegister's payload is either a CoordRegister or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a CoordRegisterValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a CoordRegister
                            an empty CoordRegister.
                    -   Either the coord, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a  with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordRegister]
        Raises:
            CoordRegisterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
                
        # Handle the case that loader fails.
        load = self.loader.execute(candidate)
        if load.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidatorException.MSG,
                    err_code=CoordRegisterValidatorException.ERR_CODE,
                    ex=load.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        struct = cast(CoordRegister, load.payload)
        
        if struct.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidatorException.MSG,
                    err_code=CoordRegisterValidatorException.ERR_CODE,
                    ex=CoordRegisterConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordRegisterConsistencyException.MSG,
                        err_code=CoordRegisterConsistencyException.ERR_CODE,
                    )
                )
            )
        
        entry = struct.to_dict
        endpoints: Dict[str, Coord] = {}
        for key in struct.to_dict:
            coord_validation = self.toolkit.dependency.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=entry[key]),
                    id=IdFactory.next_id(class_name="CoordRegisterRequest")
                )
            )
            if coord_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CoordRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordRegisterValidatorException.MSG,
                        err_code=CoordRegisterValidatorException.ERR_CODE,
                        ex=coord_validation.exception
                    )
                )
            coord = cast(Coord, coord_validation.payload)
            endpoints[key] = coord
            
        # --- Forward the appropriate work product to the caller. ---#
        return ValidationResult.success(
            CoordRegister(
                origin=endpoints["origin"],
                destination=endpoints["destination"],
            )
        )

    
    
