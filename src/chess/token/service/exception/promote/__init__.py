# src/chess/token/service/exception/promote/__init__.py

"""
Module: chess.token.service.exception.promote.__init__
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

# =========== TOKEN.SERVICE.EXCEPTION.PROMOTE PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .route import PawnPromotionRouteException
from .double import PawnAlreadyPromotedException
from .wrapper import PawnPromotionFailedException
from .king import CannotPromotePawnToKingException
from .same import NewRankSameAsCurrentRankException