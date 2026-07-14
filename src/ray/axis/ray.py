# src/ray/axis/ray.py

"""
Module: ray.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast


from model import Coord, Vector
from ray import Ray
from register import VectorRegister
from result import ComputationResult
from space import Axis


class AxisRay(Ray):
   
    
    def __init__(self, space: Axis):
        super().__init__(space=space)
        
    @property
    def space(self) -> Axis:
        return cast(Axis, self.space)
    
    
    def vector_ray(self,) -> ComputationResult:
        method = f"{self.__class__.__name__}.vector_ray"
        
        cursor = self.space.delta_bound.origin
        terminus = self.space.delta_bound.terminus
        vectors: List[Vector] = []
        
        while cursor != terminus:
            vectors.append(cursor)
            addition = self.math.add_vector.execute(
                VectorRegister(u=cursor, v=self.space.delta_bound.delta)
            )
            if addition.is_failure:
                # Send the exception chain in the result.
                return ComputationResult.failure(
                    addition.exception
                )
            cursor = cast(Vector, addition.payload)
            # cursor = Vector(
            #     x=self.space.delta_bound.delta.x + cursor.x,
            #     y=self.space.delta_bound.delta.y + cursor.y
        return ComputationResult.success(vectors)
        
    def coord_ray(self) -> ComputationResult:
        method = f"{self.__class__.__name__}.coord_ray"
        
        coords: List[Coord] = []
        computation = self.vector_ray()
        if computation.is_failure:
            # Send the exception chain on the failure.
            return ComputationResult.failure(
                computation.exception
            )
        vectors = cast(List[Vector], computation.payload)
        for vector in vectors:
            build = self.math.coord.builder.execute(row=vector.x, column=vector.y)
            if build.is_failure:
                # Send the exception chain on failure.
                return ComputationResult.failure(
                    build.exception
                )
            coords.append(cast(Coord, build.payload))
        return ComputationResult.success(coords)