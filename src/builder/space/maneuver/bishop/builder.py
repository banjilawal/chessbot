# src/builder/space/maneuver/bishop.py

"""
Module: builder.space.maneuver.bishop
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast

from blueprint import SoutheastQuadrantBlueprint
from builder import ManeuverBuilder
from factory import QuadrantSpaceFactory
from model import TargetVectorSet, Vector

from result import BuildResult
from schema import QuadrantOrientation
from space import BishopManeuverVectors, NortheastQuadrant, NorthwestQuadrant, SoutheastQuadrant, SouthwestQuadrant
from toggle import OrientationToggle
from util import LoggingLevelRouter
from validator import VectorValidator


class BishopManeuverBuilder(ManeuverBuilder[BishopManeuverVectors]):
    _vector_validator: Optional[VectorValidator]
    _ne_quadrant: NortheastQuadrant
    _nw_quadrant: NorthwestQuadrant
    se_quadrant: SoutheastQuadrant
    sw_quadrant: SouthwestQuadrant
    
    def __init__(
            self,
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
            _quadrant_factory: Optional[QuadrantSpaceFactory] | None = QuadrantSpaceFactory(),
    ):
        """
        Args:
            quadrant_factory: Optional[QuadrantSpaceFactory]            
        """
        super().__init__()
        self._vector_validator = vector_validator
        self._quadrant_factory = _quadrant_factory
    
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector, ) -> BuildResult[BishopManeuverVectors]:
        method = f"{self.__class__.__name__}.execute"
        
        targets: List[TargetVectorSet] = []
        
        quadrant = self._quadrant_factory.execute(
            oring=origin,
            toggle=OrientationToggle(quadrant=QuadrantOrientation.NORTHEAST)
        )
        ne_quad = cast(NortheastQuadrant, quadrant.payload)
        ne_targets = ne_quad.target_vectors()
        
        quadrant = self._quadrant_factory.execute(
            oring=origin,
            toggle=OrientationToggle(quadrant=QuadrantOrientation.NORTHWEST)
        )
        nw_quad = cast(NorthwestQuadrant, quadrant.payload)
        nw_targets = nw_quad.target_vectors()
        
        quadrant = self._quadrant_factory.execute(
            oring=origin,
            toggle=OrientationToggle(quadrant=QuadrantOrientation.SOUTHEAST)
        )
        se_quad = cast(SoutheastQuadrant, quadrant.payload)
        se_targets = ne_quad.target_vectors()
        
        quadrant = self._quadrant_factory.execute(
            oring=origin,
            toggle=OrientationToggle(quadrant=QuadrantOrientation.SOUTHWEST)
        )
        sw_quad = cast(NorthwestQuadrant, quadrant.payload)
        sw_targets = nw_quad.target_vectors()
        
        targets.append(cast(TargetVectorSet, ne_targets.payload))
        targets.append(cast(TargetVectorSet, nw_targets.payload))
        targets.append(cast(TargetVectorSet, se_targets.payload))
        targets.append(cast(TargetVectorSet, sw_targets.payload))
        
        return BuildResult.success(targets)
        