# src/space/factory/quadrant/space.py

"""
Module: space.factory.quadrant.space
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from container import QuadrantSet
from model import Vector
from result import ComputationResult
from ruleset import NorthwestQuadrantVectorSpec
from space import NortheastQuadrant, NorthwestQuadrant, QuadrantSpace, SoutheastQuadrant, SouthwestQuadrant


class QuadrantFactory:
    
    def generate(origin: Vector) -> ComputationResult[QuadrantSet]:
        
        quadrants: List[QuadrantSpace] = []
        
        nw = NorthwestQuadrant(origin=origin)
        nw_spec = NorthwestQuadrantVectorSpec(nw)
        ne = NortheastQuadrant(origin=origin)
        ne_spec()
        se = SoutheastQuadrant(origin=origin)
        sq = SouthwestQuadrant(origin=origin)
        
        quadrants = [nw, ne, se, sw]