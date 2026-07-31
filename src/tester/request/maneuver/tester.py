# src/tester/request/maneuver/token/tester.py

"""
Module: tester.request.maneuver.token.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, Type, cast

from bootstrapper import ManeuverRequestBootstrapper
from err import ManeuverRequestTesterException
from microservice import IdentityService
from request.maneuver import ManeuverRequest
from result import MethodResultType, ValidationResult
from tester import RequestTester
from util import LoggingLevelRouter


class ManeuverRequestTester(RequestTester):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a maneuver that can be promoted.
        
    Attributes:
        pawn_tester: ManeuverPawnTester
        identity_service: IdentityService
        priming_validator: PrimingValidator
        carrier_validator: ManeuverPermitterBootstrapper
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _pawn_tester: ManeuverPawnTester
    _identity_service: IdentityService
    _bootstrapper: ManeuverRequestBootstrapper
    _maneuver_level_tester: ManeuverLevelTester
    
    def __init__(
            self,
            pawn_tester: ManeuverPawnTester | None = ManeuverPawnTester(),
            identity_service: IdentityService | None = IdentityService(),
            maneuver_level_tester: ManeuverLevelTester | None = ManeuverLevelTester(),
            bootstrapper: ManeuverRequestBootstrapper | None = ManeuverRequestBootstrapper(),
    ):
        """
        Args:
            pawn_tester: ManeuverPawnTester
            identity_service: IdentityService
            maneuver_level_tester: ManeuverLevelTester
            bootstrapper: ManeuverPermitterBootstrapper
        """
        self._bootstrapper = bootstrapper
        self._pawn_tester = pawn_tester
        self._identity_service = identity_service
        self._maneuver_level_tester = maneuver_level_tester
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verifies the subject is a promotable maneuver.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   The subject is not a free maneuver.
                    -   The maneuver has already been promoted.
                    -   Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            ManeuverRequestTesterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the ManeuverRequest is not bootstrapped successfully.
        bootstrap = self._bootstrapper.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                ManeuverRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestTesterException.MSG,
                    err_code=ManeuverRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=bootstrap.exception
                )
            )
        request = cast(ManeuverRequest, bootstrap.payload)
        
        # handle the case that, the item is not a safe token.
        id_test = self._identity_service.validate_id(request.id)
        if id_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                ManeuverRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestTesterException.MSG,
                    err_code=ManeuverRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=id_test.exception
                )
            )
        # Handle the case that, the subject is not a pawn.
        pawn_test = self._pawn_tester.execute(subject=request.candidate)
        if pawn_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                ManeuverRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestTesterException.MSG,
                    err_code=ManeuverRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=pawn_test.exception
                )
            )
        # Handle the case that, the request contains a malformed stack.
        rank_level_test = self._maneuver_level_tester.execute(request.rank_level)
        # Send the exception chain in the permission denial.
        if rank_level_test.is_failure:
        # Send the exception chain in the result.
            return ValidationResult.failure(
                ManeuverRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestTesterException.MSG,
                    err_code=ManeuverRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=pawn_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)