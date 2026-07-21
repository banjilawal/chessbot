# src/logic/board/database/kernel/exception/deletion/__init__.py

"""
Module: logic.board.database.kernel.exception.deletion.__init__
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

# =========== ERR.BOARD.DATABASE.CORE.EXCEPTION.DELETION PACKAGE ===========#

# Packages


# Modules
from .work import BoardDeletionException
from. emptty import PoppingEmptyBoardStackException
from .unfound import BoardDoesNotExistForRemovalException