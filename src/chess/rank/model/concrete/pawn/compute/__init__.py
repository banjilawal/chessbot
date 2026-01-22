# src/chess/rank/model/concrete/pawn/compute/__init__.py

"""
Module: chess.rank.model.concrete.pawn.compute.__init__
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

# =========== RANK.MODEL.CONCRETE.PAWN.COMPUTE PACKAGE CONTENTS ===========#

# Packages
from .opening import *
from .attack import *

# Modules
from .pawn import Pawn
from .exception import PawnSpanComputationFailedException