# src/authorization/adjudicator/chain/search/vector/adjudicator.py

"""
Module: authorization.adjudicator.chain.search.vector.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, TypeVar

from assurance import PrimingValidator
from artifcat.report import AuthorizationDecision
from util import LoggingLevelRouter

T = TypeVar("T", bound="ChainSearchRequest")


class VectorNodeSearchRequestAdjudicator(ChainSearchRequestAdjudicator[VectorNodeSearchRequest]):
    """
    Role:
        -   Permission Authorization
        -   Checklist Runner
        -   Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a VectorChainSearchRequest.

    Attributes:
        node_validator: Optional[VectorNodeValidator]
        priming_validator: Optional[PrimingValidator]

    Provides:
        -    def execute(self, candidate: Any) -> RequestDecision

    Super Class:
        ChainSearchRequestAdjudicator
    """
    
    def __init__(
            self,
            node_validator: Optional[VectorNodeValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            node_validator: Optional[VectorNodeValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(node_validator=node_validator, priming_validator=priming_validator)
        
    @property
    def node_validator(self) -> VectorNodeValidator:
        return cast(VectorNodeValidator, super().node_validator)
        

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AuthorizationDecision:
        method = f"{self.__class__.__name__}.execute"
        
        bootstrap = self.priming_validator.execute(
            candidate=candidate,
            target_model=VectorNodeSearchRequest,
            null_exception=VectorNodeSearchRequestNullException,
        )
        if bootstrap.is_failure:
            return AuthorizationDecision.is_denied(
                exception=VectorNodeSearchRequestException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchRequestException.MSG,
                    err_code=VectorNodeSearchRequestException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        request = cast(VectorNodeSearchRequest, candidate)
        
        node_validation = self.node_validator.execute(request.target)
        if node_validation.is_failure:
            return AuthorizationDecision.is_denied(
                exception=VectorNodeSearchRequestException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchRequestException.MSG,
                    err_code=VectorNodeSearchRequestException.ERR_CODE,
                    ex=node_validation.exception,
                )
            )
        
        


class VectorNodeSearchRequest(ChainSearchRequest[VectorNode]):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry information to find a VectorNode in the a VectorChain.

    Attributes:
        id: int
        target: VectorNode
        chain: VectorChain

    Provides:

    Super Class:
        ChainSearchRequest
    """
    
    def __init__(self, id: int, target: VectorNode, chain: VectorChain,):
        """
        Args:
            id: int
            target: VectorNode
            chain: VectorChain
        """
        super().__init__(id=id, target=target, chain=chain,)
        
    @property
    def target(self) -> VectorNode:
        return cast(VectorNode, super().target)
    
    @property
    def chain(self) -> VectorChain:
        return cast(VectorChain, super().chain)
        