# src/ray/axis/ray.py

"""
Module: ray.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast

from err import AxisRayComputerException
from model import Coord, Vector
from ray import RayComputer
from register import VectorRegister
from result import ComputationResult
from space import Axis


class AxisRayComputer(RayComputer):
   
    
    def __init__(self, space: Axis):
        super().__init__(space=space)
        
    @property
    def space(self) -> Axis:
        return cast(Axis, self.space)
    
    
    def vector_ray(self,) -> ComputationResult:
        method = f"{self.__class__.__name__}.vector_ray"
        
        cursor = self.space.origin
        terminus = self.space.terminus
        vectors: List[Vector] = []
        
        while cursor != terminus:
            vectors.append(cursor)
            
            result = self.space.next(current=cursor)
            if result.is_failure:
                # Send the exception chain in the result.
                return ComputationResult.failure(
                    AxisRayComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AxisRayComputerException.MSG,
                        err_code=AxisRayComputerException.ERR_CODE,
                        mthd_rslt_type=AxisRayComputerException.MTHD_RSLT_TYPE,
                        ex=result.exception,
                    )
                )
            cursor = cast(Vector, result.payload)
        return ComputationResult.success(vectors)
        
    def coord_ray(self) -> ComputationResult:
        method = f"{self.__class__.__name__}.coord_ray"
        
        coords: List[Coord] = []
        computation = self.vector_ray()
        if computation.is_failure:
            # Send the exception chain on the failure.
            return ComputationResult.failure(
                AxisRayComputerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisRayComputerException.MSG,
                    err_code=AxisRayComputerException.ERR_CODE,
                    mthd_rslt_type=AxisRayComputerException.MTHD_RSLT_TYPE,
                    ex=computation.exception,
                )
            )
        vectors = cast(List[Vector], computation.payload)
        for vector in vectors:
            build = self.math.coord.builder.execute(row=vector.x, column=vector.y)
            if build.is_failure:
                # Send the exception chain on failure.
                return ComputationResult.failure(
                    AxisRayComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AxisRayComputerException.MSG,
                        err_code=AxisRayComputerException.ERR_CODE,
                        mthd_rslt_type=AxisRayComputerException.MTHD_RSLT_TYPE,
                        ex=build.exception,
                    )
                )
            coords.append(cast(Coord, build.payload))
        return ComputationResult.success(coords)