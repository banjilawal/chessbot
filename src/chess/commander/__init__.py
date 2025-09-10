"""
Commander Package

PURPOSE:
    Competotrs who play a team

CORE CLASSES:
    Commander
    HumanCommander
    CyberneticCompettor

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji L
"""


from .commander import Commander
from .human import HumanCompetitor
from .cybernetic import CyberneticCompetitor

Human = HumanCompetitor
Machine = CyberneticCompetitor



# Class Aliases

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "competitor_pkg"


# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }


__all__ = [
    # Core Packages
    "Commander",
    "HumanCompetitor",
    "CyberneticCompetitor",

    # Aliases
    "Human",
    "Machine",

    "__version__",
    "__author__",
    "package_info"
]