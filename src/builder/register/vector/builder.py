# src/builder/register/vector/builder.py

"""
Module: builder.register.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import RegisterBuilder
from model import Vector
from register import VectorRegister
from result import BuildResult
from util import LoggingLevelRouter
from validator import VectorValidator


class VectorRegisterBuilder(RegisterBuilder[VectorRegister]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        u: Vector
        v: Vector
        endpoint_validator: Optional[VectorValidator]

    Provides:

    Super Class:
        RegisterBuilder
    """
    
    def __init__(
            self,
            u: Vector,
            v: Vector,
            endpoint_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            u: Vector
            v: Vector
            endpoint_validator: Optional[VectorValidator]
        """
        super().__init__(
            a=u,
            b=v,
            endpoint_validator=endpoint_validator
        )

        
    @property
    def u(self) -> Vector:
        return cast(Vector, self.a)
    
    @property
    def v(self) -> Vector:
        return cast(Vector, self.b)
    
    @property
    def endpoint_validator(self) -> VectorValidator:
        return cast(VectorValidator, self.endpoint_validator)
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[VectorRegister]:
        method = f"{self.__class__.__name__}.execute"
        
        for vector in [self.u, self.v]:
            validation = self.endpoint_validator.execute(vector)
            # Send the exception chain in the result.
            return BuildResult.failure(
                VectorRegisterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterBuilderException.MSG,
                    err_code=VectorRegisterBuilderException.ERR_CODE,
                    mthd_rslt=MethodResultType.BUILD_RESULT,
                    ex=validation.exception,
                )
            )
        return BuildResult.success(VectorRegister(u=self.u, v=self.v))

    
