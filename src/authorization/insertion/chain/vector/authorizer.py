# src/authorization/insertion/node/authorization.py

"""
Module: authorization.insertion.node.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import AddNodeRequestAuthorizer
from collection import VectorChain
from domain.structure.node import VectorNode
from report import AuthorizationDecision
from domain.exchange.request import AddVectorNodeRequest
from operation.toolkit import AddVectorNodeRequestToolkit
from util import LoggingLevelRouter



class AddVectorNodeRequestAuthorizer(AddNodeRequestAuthorizer[VectorNode]):
    
    def __init__(
            self,
            ruleset: Optional[AddVectorNodeRequestToolkit] | None = None,
    ):
        """
        Args:
            ruleset: Optional[AddVectorNodeRequestToolkit]
        """
        super().__init__(ruleset=ruleset or AddVectorNodeRequestToolkit())
        
    @property
    def ruleset(self) -> AddVectorNodeRequestToolkit:
        return cast(AddVectorNodeRequestToolkit, super().ruleset)
    

    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: AddVectorNodeRequest) -> AuthorizationDecision:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is null or the wrong type
        bootstrap = self.ruleset.priming_validator.execute(
            candidate=candidate,
            target_model=self.ruleset.request_type,
            null_exception=self.ruleset.request_null_exception,
        )
        if bootstrap.is_failure:
            # Send an exception chain in the authorization denial.
            return AuthorizationDecision.deny(
                AddVectorNodeRequestAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeRequestAuthorizerException.MSG,
                    err_code=AddVectorNodeRequestAuthorizerException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        request = cast(AddVectorNodeRequest, bootstrap.payload)
        
        # Handle the case that, the collection is not the proper chain.
        chain_validation = self.ruleset.priming_validator.execute(
            candidate=request.chain,
            target_model=self.ruleset.collection_type,
            null_exception=self.ruleset.collection_null_exception,
        )
        if chain_validation.is_failure:
            # Send an exception chain in the authorization denial.
            return AuthorizationDecision.deny(
                AddVectorNodeRequestAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeRequestAuthorizerException.MSG,
                    err_code=AddVectorNodeRequestAuthorizerException.ERR_CODE,
                    ex=chain_validation.exception,
                )
            )
        chain = cast(VectorChain, chain_validation.payload)
        
        # Handle the case that, the node is either null or the wrong type.
        node_validation = self.ruleset.priming_validator.execute(
            candidate=request.node,
            target_model=self.ruleset.node_type,
            null_exception=self.ruleset.node_null_exception,
        )
        if node_validation.is_failure:
            # Send an exception chain in the authorization denial.
            return AuthorizationDecision.deny(
                AddVectorNodeRequestAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeRequestAuthorizerException.MSG,
                    err_code=AddVectorNodeRequestAuthorizerException.ERR_CODE,
                    ex=node_validation.exception,
                )
            )
        
        node = cast(VectorNode, node_validation.payload)
        vector_validation = self.ruleset.vector_validator.execute(node.payload)
        if vector_validation.is_failure:
            return AuthorizationDecision.deny(vector_validation.exception)
        
        return AuthorizationDecision.grant(request)
        
        
        
        
        
        
        
        
        
    
    