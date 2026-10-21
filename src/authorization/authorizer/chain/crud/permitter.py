# src/authorization/authorizer/chain/crud/authorizer.py

"""
Module: authorization.authorizer.chain.crud.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod

from authorization.authorizer.chain import ChainOperationAuthorizer
from artifcat.report import CrudApprovalReport
from client.exchange import CrudRequest
from util import LoggingLevelRouter


class CrudAuthorizer(ChainOperationAuthorizer):
    """
    Role:
        - Analysis Worker
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Checks if an object satisfies the conditions to perform an operation.

    Attributes:

    Provides:
        -   def execute(cls, requestor: T, *args, **kwargs) -> AnalysisResult

    Super Class:
        Authorizer
    """
    def __init__(self):
        super().__init__()
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CrudRequest, ) -> CrudApprovalReport:
        pass