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
from domain.structure.searchable.node import VectorNode
from artifcat.report import AuthorizationDecision
from domain.exchange.request import AddVectorNodeRequest
from operation.utility import AddVectorNodePermissionUtility
from util import LoggingLevelRouter



class AddVectorNodeRequestAuthorizer(AddNodeRequestAuthorizer[VectorNode]):
    
    def __init__(
            self,
            utility: Optional[AddVectorNodePermissionUtility] | None = None,
    ):
        """
        Args:
            utility: Optional[AddVectorNodePermissionUtility]
        """
        super().__init__(utility=utility or AddVectorNodePermissionUtility())
        
    @property
    def utility(self) -> AddVectorNodePermissionUtility:
        return cast(AddVectorNodePermissionUtility, super().utility)
    

    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: AddVectorNodeRequest) -> AuthorizationDecision:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is null or the wrong type
        bootstrap = self.utility.priming_validator.execute(
            candidate=candidate,
            target_model=self.utility.request_type,
            null_exception=self.utility.request_null_exception,
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
        chain_validation = self.utility.priming_validator.execute(
            candidate=request.chain,
            target_model=self.utility.collection_type,
            null_exception=self.utility.collection_null_exception,
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
        node_validation = self.utility.priming_validator.execute(
            candidate=request.node,
            target_model=self.utility.node_type,
            null_exception=self.utility.node_null_exception,
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
        vector_validation = self.utility.vector_validator.execute(node.payload)
        if vector_validation.is_failure:
            return AuthorizationDecision.deny(vector_validation.exception)
        
        return AuthorizationDecision.grant(request)
        
        
        
        
        
        
        
        
        
    
    