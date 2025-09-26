"""
chess.builder Package

PURPOSE:
    Validated entity builder

CORE CLASSES:
    Commander
    HumanCommander
    CyberneticCompetitor

    CommanderBuilderException
    CoordBuilderException
    PieceBuilderException
    ScalarBuilderException
    VectorBuilderException

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji L
"""

from .exception import *

from chess.commander.commander_builder import CommanderBuilder
from chess.coord.coord_builder import CoordBuilder
from chess.piece.coord_stack_builder import CoordinateStackBuilder
from chess.piece.piece_builder import PieceBuilder
from chess.scalar.scalar_builder import ScalarBuilder
from chess.square.square_builder import SquareBuilder
from chess.team.team_builder import TeamBuilder
from chess.vector.vector_builder import VectorBuilder

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.builder"

__all__ = [
    # Core classes
    "CommanderBuilder",
    "CoordBuilder",
    "CoordinateStackBuilder",
    "PieceBuilder",
    "ScalarBuilder",
    "SquareBuilder",
    "TeamBuilder",
    "VectorBuilder",

    *exception.__all__,

    "__version__",
    "__author__",
    "package_info"
]

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }