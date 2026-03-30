from __future__ import annotations

from logic.zone import MultiplyZoneTransaction, ZoneAdditionTransaction, ConvertVectorToZoneTransaction
from logic.zone.service.operation.arithmetic.distance.compute import EuclideanDistance


class ZoneArithmeticController:
    """
    Role:
        - Controller

    Responsibilities:
        1.  Provide a single entry point for Zone arithmetic operations.

    Attributes:
        distance: EuclideanDistance
        addition: ZoneAdditionTransaction
        multiplication: MultiplyZoneTransaction
        conversion: ConvertVectorToZoneTransaction

    Provides:
    Super Class:
    """
    _distance: EuclideanDistance
    _addition: ZoneAdditionTransaction
    _multiplication: MultiplyZoneTransaction
    _conversion: ConvertVectorToZoneTransaction

    def __init__(
            self,
            distance: EuclideanDistance = EuclideanDistance(),
            addition: ZoneAdditionTransaction = ZoneAdditionTransaction(),
            multiplication: MultiplyZoneTransaction = MultiplyZoneTransaction(),
            conversion: ConvertVectorToZoneTransaction = ConvertVectorToZoneTransaction(),
    ):
        """
        Args:
            distance: EuclideanDistance
            addition: ZoneAdditionTransaction
            multiplication: MultiplyZoneTransaction
            conversion: ConvertVectorToZoneTransaction
        """
        self._addition = addition
        self._distance = distance
        self._conversion = conversion
        self._multiplication = multiplication

    
    @property
    def conversion(self) -> ConvertVectorToZoneTransaction:
        return self._conversion
    
    @property
    def addition(self) -> ZoneAdditionTransaction:
        return self._addition
    
    @property
    def multiplication(self) -> MultiplyZoneTransaction:
        return self._multiplication
    
    @property
    def distance(self) -> EuclideanDistance:
        return self._distance