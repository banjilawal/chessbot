# src/space/builder/register/__init__.py

"""
Module: space.builder.register.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from bootstrapper import PrimingValidator
from container import RegisterSet
from result import BuildResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="TargetVectorSet")


class RegisterBuilder(ABC, Generic[T]):
    _points: T
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            points: T,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            points: T
            priming_validator: PrimingValidator            
        """
        self._points = points
        self._priming_validator = priming_validator
        
    @property
    def points(self) -> T:
        return self._points
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[RegisterSet]:
        pass
        

        

        
        
    # def _validation(self, candidate: Any) -> ValidationResult[LinearTargetSet]:
    #     method = f"{self.__class__.__name__}"
    #     
    #     priming = self._priming_validator.execute(
    #         candidate=self._linear_sett,
    #         target_model=Type[LinearTargetSet],
    #         null_exception=NullException(),
    #     )
    #     if priming.is_failure:
    #         return ValidationResult.failure(priming.exception)
    #     linear_sett = cast(LinearTargetSet, priming.payload)
    #     
    #     if linear_sett.is_empty:
    #         return BuildResult.failure(
    #             LinearSpaceRegisterBuilderException(
    #                 cls_mthd=method,
    #                 cls_name=self.__class__.__name__,
    #                 msg=LinearSpaceRegisterBuilderException.MSG,
    #                 err_code=LinearSpaceRegisterBuilderException.ERR_CODE,
    #                 mthd_rslt_type=MethodResultType.BUILD_RESULT,
    #                 ex=EmptyLinearVectorSetException(
    #                     cls_mthd=method,
    #                     cls_name=self.__class__.__name__,
    #                     msg=EmptyLinearVectorSetException.MSG,
    #                     err_code=EmptyLinearVectorSetException.ERR_CODE,
    #                 )
    #             )
    #         )
    #     self._linear_sett = temp