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
from toolkit import AddVectorNodeRequestToolkit
from util import LoggingLevelRouter



class AddVectorNodeRequestAuthorizer(AddNodeRequestAuthorizer[VectorNode]):
    
    def __init__(
            self,
            toolkit: Optional[AddVectorNodeRequestToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AddVectorNodeRequestToolkit]
        """
        super().__init__(toolkit=toolkit or AddVectorNodeRequestToolkit())
        
    @property
    def toolkit(self) -> AddVectorNodeRequestToolkit:
        return cast(AddVectorNodeRequestToolkit, super().toolkit)
    

    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: AddVectorNodeRequest) -> AuthorizationDecision:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is null or the wrong type
        bootstrap = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.request_type,
            null_exception=self.toolkit.request_null_exception,
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
        chain_validation = self.toolkit.priming_validator.execute(
            candidate=request.chain,
            target_model=self.toolkit.collection_type,
            null_exception=self.toolkit.collection_null_exception,
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
        node_validation = self.toolkit.priming_validator.execute(
            candidate=request.node,
            target_model=self.toolkit.node_type,
            null_exception=self.toolkit.node_null_exception,
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
        vector_validation = self.toolkit.vector_validator.execute(node.payload)
        if vector_validation.is_failure:
            return AuthorizationDecision.deny(vector_validation.exception)
        
        return AuthorizationDecision.grant(request)
        
        
        
        
        
        
        
        
        
    
    