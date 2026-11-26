# src/bootstrap/authorization/projectionloader.py

"""
Module: bootstrap.authorization.projection.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from artifcat import ProjectionDecision
from bootstrap import ComputationAuthorizationLoader
from microservice import VectorNodeValidationService
from request import ProjectionPermissionRequest

from util import LoggingLevelRouter

T = TypeVar("T", bound="ProjectionPermissionRequest")

class ProjectionAuthorizationLoader(
    ComputationAuthorizationLoader[T], ABC, Generic[T]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ComputationAuthorization module.

    Attributes:
        node_validation_service: VectorNodeValidationService

    Provides:
        -   def execute(candidate: Any) -> ProjectionDecision

    Super Class:
        ComputationAuthorizationLoader
    """
    _node_validation_service: VectorNodeValidationService
    
    def __init__(
            self,
            node_validation_service: Optional[VectorNodeValidationService] | None = None,
    ):
        """
        Args:
            node_validation_service: Optional[VectorNodeValidationService]
        """
        super().__init__()
        self._node_validation_service = node_validation_service or VectorNodeValidationService()
        
    @property
    def node_validation_service(self) -> VectorNodeValidationService:
        return self._node_validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ProjectionDecision[T]:
        """
        Validates and type checks the candidate and its contents for the ComputationPermitter.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           ComputationDecision
        Raises:
            ProjectionAuthorizationLoaderException
        """
        pass