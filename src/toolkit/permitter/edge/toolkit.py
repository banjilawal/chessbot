# src/toolkit/permitter/edge/toolkit.py

"""
Module: toolkit.permitter.edge.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import IdentityService
from microservice.edge import Edge, EdgeToolkitException
from microservice.node import NodeService
from system import Toolkit, ToolkitResult, LoggingLevelRouter, NumberValidator


class EdgeToolkit(PermitterToolkit[Edge]):
    """
     Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        node_service NodeService
        identity_service IdentityService
        
    Provides:

     Super Class:
         Toolkit
     """
    _node_service: NodeService
    _identity_service: IdentityService

    def __init__(
            self,
            node_service: NodeService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            node_service NodeService
            identity_service IdentityService
        """
        self._node_service = node_service or NodeService()
        self._identity_service = identity_service or IdentityService()
        
    @property
    def node_service(self) -> NodeService:
        return self._node_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service