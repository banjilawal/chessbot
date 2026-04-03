from __future__ import annotations

from logic.coord import MultiplyCoordTransaction, CoordAdditionTransaction, ConvertVectorToCoordTransaction
from logic.coord.service.operation.arithmetic.distance.compute import EuclideanDistance


class CoordArithmeticController:
    """
    Role:
        - Controller

    Responsibilities:
        1.  Provide a single entry point for Coord arithmetic operations.

    Attributes:
        distance: EuclideanDistance
        addition: CoordAdditionTransaction
        multiplication: MultiplyCoordTransaction
        conversion: ConvertVectorToCoordTransaction

    Provides:
    Super Class:
    """
    _distance: EuclideanDistance
    _addition: CoordAdditionTransaction
    _multiplication: MultiplyCoordTransaction
    _conversion: ConvertVectorToCoordTransaction

    def __init__(
            self,
            distance: EuclideanDistance = EuclideanDistance(),
            addition: CoordAdditionTransaction = CoordAdditionTransaction(),
            multiplication: MultiplyCoordTransaction = MultiplyCoordTransaction(),
            conversion: ConvertVectorToCoordTransaction = ConvertVectorToCoordTransaction(),
    ):
        """
        Args:
            distance: EuclideanDistance
            addition: CoordAdditionTransaction
            multiplication: MultiplyCoordTransaction
            conversion: ConvertVectorToCoordTransaction
        """
        self._addition = addition
        self._distance = distance
        self._conversion = conversion
        self._multiplication = multiplication

    
    @property
    def conversion(self) -> ConvertVectorToCoordTransaction:
        return self._conversion
    
    @property
    def addition(self) -> CoordAdditionTransaction:
        return self._addition
    
    @property
    def multiplication(self) -> MultiplyCoordTransaction:
        return self._multiplication
    
    @property
    def distance(self) -> EuclideanDistance:
        return self._distance