# src/authorization/reviewer/role/maneuver/path/reviewer.py

"""
Module: authorization.reviewer.role.maneuver.path.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ManeuverDecision
from authorization import ManeuverRoleReviewer
from domain import Elevateable
from exchange import ManeuverRequest
from util import LoggingLevelRouter


class ManeuverPathReviewer(ManeuverRoleReviewer[Elevateable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        checker: ManeuverPathChecker

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        ManeuverRoleReviewer
    """

    def __init__(self):
        super().__init__()
       
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.checker.execute(request)
        if decision.is_denial:
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverPathReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPathReviewerException.MSG,
                    err_code=ManeuverPathReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        grant = decision.request
        approval = ManeuverRequest(
            id=grant.id,
            activity=grant.activity,
            applicant=grant.applicant,
        )
        return ManeuverDecision.grant(approval)
        