# src/chess/square/database/core/exception/insertion/__init__.py

"""
Module: chess.square.database.core.exception.insertion.__init__
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

# =========== SQUARE.DATABASE.CORE.EXCEPTION.INSERTION PACKAGE CONTENTS ===========#

# Packages
from .collision import *

# Modules
from .full import FullSquareStackException
from .wrapper import SquareInsertionFailedException
from .direct import AppendingSquareDirectlyIntoItemsFailedException