# src/space/ray/computer/register/__init__.py

"""
Module: space.ray.computer.register.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from bootstrapper import PrimingValidator
from container import LinearDestinationSet, RegisterSet
from err import LinearSpaceRegisterBuilderException, NullException
from result import BuildResult, MethodResultType


class LinearSpaceRegisterSetBuilder:
    _linear_vectors: LinearDestinationSet
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            linear_vectors: LinearDestinationSet,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            linear_vectors: LinearVectorSet,
            priming_validator: PrimingValidator            
        """
        self._linear_vectors = linear_vectors
        self._priming_validator = priming_validator
        
        
    def execute(self) -> BuildResult[RegisterSet]:
        method = f"{self.__class__.__name__}.execute"
        
        priming = self._priming_validator.execute(
            candidate=self._linear_vectors,
            target_model=Type[LinearDestinationSet],
            null_exception=NullException(),
        )
        if priming.is_failure:
            return BuildResult.failure(priming.exception)
        temp = cast(LinearDestinationSet, priming.payload)
        self._linear_vectors = temp
        
        if temp.is_empty:
            return BuildResult.failure(
                LinearSpaceRegisterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinearSpaceRegisterBuilderException.MSG,
                    err_code=LinearSpaceRegisterBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=EmptyLinearVectorSetException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyLinearVectorSetException.MSG,
                        err_code=EmptyLinearVectorSetException.ERR_CODE,
                    )
                )
            )
        self._linear_vectors = temp.remove_root_from_destinations()
        
        cursor = self._linear_vectors.root
        terminus = self
        