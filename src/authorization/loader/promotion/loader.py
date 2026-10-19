# src/authorization/loader/promotion/loader.py

"""
Module: authorization.loader.promotion.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional

from authorization import AuthorizationLoader
from exchange import PromotionRequest, TokenValidationService
from util import LoggingLevelRouter


class PromotionAuthorizationLoader(AuthorizationLoader[PromotionRequest]):
    _validator: TokenValidationService
    
    def __init__(self, validator: Optional[TokenValidationService] | None = None):
        """
        Args:
            validator: Optional[TokenValidationService]
        """
        super().__init__()
        self._validator = validator or TokenValidationService()
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> Decision[Promotion]:
        pass