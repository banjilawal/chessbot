# src/controller/computation/vector/controller.py

"""
Module: controller.computation.vector.controller
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from controller import ComputationController
from microservice import (
    EuclideanDistanceMicroservice, ScalarProductMicroservice, VectorAdditionMicroservice
)



class VectorComputationController(ComputationController):
    _addition: VectorAdditionMicroservice
    _euclidean: EuclideanDistanceMicroservice
    _multiplication: ScalarProductMicroservice
    
    def __init__(
            self,
            addition: Optional[VectorAdditionMicroservice] | None = None,
            euclidean: Optional[EuclideanDistanceMicroservice] | None = None,
            multiplication: Optional[ScalarProductMicroservice] | None = None,
        ):
        """
        Args:
            addition: Optional[VectorAdditionMicroservice]
            euclidean: Optional[EuclideanDistanceMicroservice]
            multiplication: Optional[ScalarProductMicroservice]
        """
        self._addition = addition or VectorAdditionMicroservice()
        self._euclidean = euclidean or EuclideanDistanceMicroservice()
        self._multiplication = multiplication or ScalarProductMicroservice()
        
    @property
    def addition(self) -> VectorAdditionMicroservice:
        return self._addition
    
    @property
    def euclidean(self) -> EuclideanDistanceMicroservice:
        return self._euclidean
    
    @property
    def multiplication(self) -> ScalarProductMicroservice:
        return self._multiplication
        