# src/authorization/insertion/node/authorization.py

"""
Module: authorization.insertion.node.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from authorization import AddNodeRequestAuthorizer
from node import VectorNode
from report import AuthorizationDecision
from request import AddVectorNodeRequest
from toolkit import AddVectorNodeRequestToolkit
from util import LoggingLevelRouter



class AddVectorNodeRequestAuthorizer(AddNodeRequestAuthorizer[VectorNode]):
    
    def __init__(self, toolkit: AddVectorNodeRequestToolkit):
        """
        Args:
            toolkit: AddVectorNodeRequestToolkit
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> AddVectorNodeRequestToolkit:
        return cast(AddVectorNodeRequestToolkit, super().toolkit)
    

    
    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorNodeRequest) -> AuthorizationDecision:
        method = f"{self.__class__.__name__}.execute"
        
        
        
        
    
    