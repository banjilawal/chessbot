# src/chess/system/lookup/metadata.py

"""
Module: chess.system.lookup.metadata
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from abc import ABC
from typing import List


class Metadata(ABC):
    """
    # ROLE: Configuration Table, Metadata

    # RESPONSIBILITIES:
    1.  Provides a set of static values assigned to strategy-using subclasses for inherited or common attributes.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @property
    def allowed_names(self) -> List[str]:
        """List of names associated with each subclass according to the metadata set."""
        pass