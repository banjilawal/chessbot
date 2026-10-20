# src/authorization/approver/approver.py

"""
Module: authorization.approver.approver
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from util import LoggingLevelRouter

T = TypeVar("T", model="AuthorizationRequest")

class Reviewer(ABC, Generic[T]):
    """
    Role:
        - Permission Authorization
        - Checklist Runner
        - Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a .

    Attributes:
        priming_validator: PrimingValidator
        permit_approver: PermitApprover[T]
        applicant_approver: ApplicantApprover[T]

    Provides:

    Super Class:
    """
    
    _priming_validator: PrimingValidator
    _permit_approver: PermitApprover[T]
    _applicant_approver: ApplicantApprover[T]

    
    def __init__(
            self,
            permit_approver: PermitApprover[T],
            applicant_approver: ApplicantApprover[T],
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            priming_validator: PrimingValidator
            validation_service: ValidationService[T]
        """
        self._priming_validator = priming_validator or PrimingValidator()
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def validation_service(self) -> ValidationService[T]:
        return self._validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> ValidationResult[T]:
        pass
        