# src/logic/token/service/handler/promotion/exception/debug/__init__.py

"""
Module: logic.token.service.handler.promotion.exception.debug.__init__
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

# =========== TOKEN.SERVICE.HANDLER.PROMOTION.EXCEPTION.DEBUG PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .route import PawnPromotionRouteException
from .pawn import NewRankCannotBePawnException
from .double import PawnAlreadyPromotedException
from .king import CannotPromotePawnToKingException