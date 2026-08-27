# src/authorization/permitter/chain/crud/permitter.py

"""
Module: authorization.permitter.chain.crud.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod

from authorization.permitter.chain import ChainOperationPermitter
from artifcat.report import CrudApprovalReport
from domain.exchange.request import CrudRequest
from util import LoggingLevelRouter


class CrudPermitter(ChainOperationPermitter):
    """
    Role:
        - Analysis Worker
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Checks if an object satisfies the conditions to perform an operation.

    Attributes:

    Provides:
        - def execute(cls, requestor: T, *args, **kwargs) -> AnalysisResult

    Super Class:
        Permitter
    """
    def __init__(self):
        super().__init__()
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CrudRequest, ) -> CrudApprovalReport:
        pass