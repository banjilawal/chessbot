from __future__ import annotations

from logic.coord import MultiplyCoordTransaction, CoordAdder, ConvertVectorToCoordTransaction
from logic.coord.service.operation.arithmetic.distance.compute import EuclideanDistance


class CoordArithmeticController:
    """
    Role:
        - Controller

    Responsibilities:
        1.  Provide a single entry point for Coord arithmetic operations.

    Attributes:
        distance: EuclideanDistance
        addition: CoordAdder
        multiplication: ScalarProductWorker
        conversion: ConvertVectorToCoordTransaction

    Provides:
    Super Class:
    """
    _distance: EuclideanDistance
    _addition: CoordAdder
    _multiplication: MultiplyCoordTransaction
    _conversion: ConvertVectorToCoordTransaction

    def __init__(
            self,
            distance: EuclideanDistance = EuclideanDistance(),
            addition: CoordAdder = CoordAdder(),
            multiplication: MultiplyCoordTransaction = MultiplyCoordTransaction(),
            conversion: ConvertVectorToCoordTransaction = ConvertVectorToCoordTransaction(),
    ):
        """
        Args:
            distance: EuclideanDistance
            addition: CoordAdder
            multiplication: ScalarProductWorker
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
    def addition(self) -> CoordAdder:
        return self._addition
    
    @property
    def multiplication(self) -> MultiplyCoordTransaction:
        return self._multiplication
    
    @property
    def distance(self) -> EuclideanDistance:
        return self._distance