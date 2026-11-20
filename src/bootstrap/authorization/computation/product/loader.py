# src/bootstrap/authorization/computation/product/loader.py

"""
Module: bootstrap.authorization.computation.product.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from bootstrap import ComputationAuthorizationLoader
from exchange import ScalarProductPermissionRequest
from util import LoggingLevelRouter


class ScalarProductAuthorizationLoader(
    ComputationAuthorizationLoader[ScalarProductPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ComputationAuthorization module.
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> ProductDecision

    Super Class:
        ComputationAuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ProductDecision:
        """
        Checks if the Request is the right type.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           ProductDecision
        Raises:
            ProductAuthorizationLoaderException
        """
        pass