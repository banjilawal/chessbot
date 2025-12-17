# src/chess/system/metadata/metadata.py

"""
Module: chess.system.metadata.metadata
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from abc import ABC
from typing import List


class Metadata(ABC):
    
    @property
    def allowed_names(self) -> List[str]:
        pass