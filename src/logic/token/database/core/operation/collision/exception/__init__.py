# src/logic/token/database/core/operation/collision/exception/__init__.py

"""
Module: logic.token.database.core.operation.collision.exception.__init__
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

# =========== TOKEN.DATABASE.CORE.OPERATION.COLLISION.EXCEPTION PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .id import TokenIdCollisionException
from .square import TokenOpeningSquareCollisionException
from .detector import TokenCollisionDetectorFailureException
from .designation import TokenDesignationCollisionException