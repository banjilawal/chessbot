# src/certifier/register/carrier/validator.py

"""
Module: certifier.register.carrier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, List, cast

from blueprint import VectorRegisterBlueprint
from carrier import VectorRegisterCarrierToggle
from err import RegisterEmptyException, RegisterSetSizeException, VectorRegisterRootCertifierException
from model import Vector
from register import VectorRegister
from result import ValidationResult
from root import RootCertifier
from toolkit import VectorRegisterToolkit
from util import LoggingLevelRouter


class VectorRegisterRootCertifier(RootCertifier[VectorRegister]):
    """
    Role
        -   Integrity Maintenance
        -   Consistency Assurance


    Responsibilities:
        1.  Ensure a VectorRegisterBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: VectorRegisterToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Certifier
    """
    
    def __init__(self, toolkit: VectorRegisterToolkit | None = VectorRegisterToolkit()):
        """
        Args:
            toolkit: VectorRegisterToolkit
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> VectorRegisterToolkit:
        return cast(VectorRegisterToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult:
        """
        Certify a candidate is a VectorRegisterBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a VectorRegisterDtoCarrier.
                    -   The candidate is an empty VectorRegisterDtoCarrier.
                    -   Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a VectorRegister in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            VectorRegisterCertifierException
            VectorRegisterDtoCarrierNullException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.model_carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterRootCertifierException.MSG,
                    err_code=VectorRegisterRootCertifierException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(VectorRegisterCarrierToggle, carrier_validation.payload)
        
        # --- Cast the candidate into a VectorRegisterBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, both slots are empty
        if blueprint.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterRootCertifierException.MSG,
                    err_code=VectorRegisterRootCertifierException.ERR_CODE,
                    ex=RegisterEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RegisterEmptyException.MSG,
                        err_code=RegisterEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, one slot is empty.
        if blueprint.is_wrong_size:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterRootCertifierException.MSG,
                    err_code=VectorRegisterRootCertifierException.ERR_CODE,
                    ex=RegisterSetSizeException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RegisterSetSizeException.MSG,
                        err_code=RegisterSetSizeException.ERR_CODE,
                    )
                )
            )
        vectors: List[Vector] = []
        
        for vector in blueprint.to_list:
            validation = self.toolkit.vector_validator.execute(vector)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorRegisterRootCertifierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorRegisterRootCertifierException.MSG,
                        err_code=VectorRegisterRootCertifierException.ERR_CODE,
                        ex=validation.exception
                    )
                )
            vectors.append(cast(Vector, validation.payload))
        # --- Extract and cast payloads of the validation results. ---#
        u = vectors[0]
        v = vectors[1]
        
        if carrier.is_carrying_model:
            return ValidationResult.success(
                VectorRegisterCarrierToggle(
                    model=VectorRegister(u=u, v=v)
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            VectorRegisterCarrierToggle(
                blueprint=VectorRegisterBlueprint(u=u, v=v  )
            )
        )