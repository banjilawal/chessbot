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
from result import ComputationResult
from space import AxisSpace


class AxisRayComputer(RayComputer):
   
    
    def __init__(self, space: AxisSpace):
        super().__init__(space=space)
        
    @property
    def space(self) -> AxisSpace:
        return cast(AxisSpace, self.space)
    
    
    def vector_ray(self,) -> ComputationResult[List[Vector]]:
        """
        Get the series of Vectors from the origin of the axis till its end.

        Action:
            1.  Send an exception chain in the ComputationResult if the stepper does not finish its
                work before the loop invariant hits.
            2.  Otherwise, append the stepper's payload to the array and advance the cursor.
        Args:
        Returns:
            ComputationResult[List[Vector]]
        Raises:
             AxisRayComputerException
        """
        method = f"{self.__class__.__name__}.vector_ray"
        
        # --- Set up for the loop ---#
        cursor = self.space.origin
        terminus = self.space.terminus
        vectors: List[Vector] = []
        
        
        # Less than is not a good choice for iterating through vectors.
        while cursor != terminus:
            vectors.append(cursor)
            # --- Request the vector from the space. ---#
            computation = self.space.stepper.next(current=cursor)
            
            # Handle the case that, request is not granted..
            if computation.is_failure:
                # Send the exception chain in the result.
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
            # Advance the cursor.
            cursor = cast(Vector, computation.payload)
            
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(vectors)
        
    def coord_ray(self) -> ComputationResult[List[Coord]]:
        """
        Get the series of Coords from the space's origin to its terminus.

        Action:
            1.  Send an exception chain in the ComputationResult if the list cannot be generated.
            2.  Otherwise, send the success result.
        Args:
        Returns:
            ComputationResult[List[Coord]]
        Raises:
             AxisRayComputerException
        """
        method = f"{self.__class__.__name__}.coord_ray"
        
        coords: List[Coord] = []
        
        # --- Get the Vector ray. ---#
        computation = self.vector_ray()
        
        # Handle the case that, the vector ray was not produced
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
        # --- Extract and cast the vector list. ---#
        vectors = cast(List[Vector], computation.payload)
        
        # Loop through the vectors to process them into Coords
        for vector in vectors:
            
            build = self.math.coord.builder.execute(row=vector.x, column=vector.y)
            # Handle the case that, a Coord could not be created from the Vector
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
            # Add to the list.
            coords.append(cast(Coord, build.payload))
            
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(coords)