# src/toolkit/model/rank/toolkit.py

"""
Module: toolkit.model.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import RankBlueprint
from carrier import RankCarrier
from err import RankBlueprintNullException, RankCarrierNullException, RankNullException
from model import Rank
from toolkit import ModelToolkit
from validator import NumberValidator


@dataclass
class RankToolkit(ModelToolkit[Rank]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Rank tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[Rank]
        carrier_model: Type[RankCarrier]
        blueprint_model: Type[RankBlueprint]
        
        null_exception: RankNullException
        carrier_null_exception: RankCarrierNullException
        blueprint_null_exception: RankBlueprintNullException

    Provides:

    Super Class:
       ModelToolkit
    """
    model: Type[Rank] = Rank
    carrier_model: Type[RankCarrier] = RankCarrier
    blueprint_model: Type[RankBlueprint] = RankBlueprint
    
    null_exception: RankNullException = RankNullException()
    carrier_null_exception: RankCarrierNullException = RankCarrierNullException()
    blueprint_null_exception: RankBlueprintNullException = RankBlueprintNullException()

    