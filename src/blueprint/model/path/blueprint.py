# src/blueprint/model/path/blueprint.py

"""
Module: blueprint.model.path.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from blueprint import ModelBlueprint
from err import PathNullException
from model import Square, Path


@dataclass
class PathBlueprint(ModelBlueprint[Path]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Path object.

    Attributes:
        origin: Square
        destination: Square
        id: Optional[int]
        null_exception: PathNullException
        model_type: Path
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    origin: Square
    destination: Square
    id: Optional[int] | None = None
    null_exception: PathNullException = PathNullException()
    model_type: Path = Path
