from __future__ import annotations

from logic.coord import CoordScalarProduct, CoordAdditionTransaction, ConvertVectorToCoordTransaction
from logic.coord.service.operation.arithmetic.distance.compute import EuclideanDistance


class CoordArithmeticController:
    """
    Role:
        - Controller

    Responsibilities:
        1.  Provide a single entry point for Coord arithmetic operations.

    Attributes:
        converter: ConvertVectorToCoordTransaction
        scalar_product: CoordScalarProduct
        vector_addition: CoordAdditionTransaction
        euclidean_distance: EuclideanDistance

    Provides:
    Super Class:
    """
    _scalar_product: CoordScalarProduct
    _conversion: ConvertVectorToCoordTransaction
    _vector_addition: CoordAdditionTransaction
    _euclidean_distance: EuclideanDistance
    
    def __init__(
            self,
            scalar_product: CoordScalarProduct = CoordScalarProduct(),
            euclidean_distance: EuclideanDistance = EuclideanDistance(),
            vector_addition: CoordAdditionTransaction = CoordAdditionTransaction(),
            converter: ConvertVectorToCoordTransaction = ConvertVectorToCoordTransaction(),
    ):
        """
        Args:
            converter: ConvertVectorToCoordTransaction
            scalar_product: CoordScalarProduct
            vector_addition: CoordAdditionTransaction
            euclidean_distance: EuclideanDistance
        """
        self._converter = converter
        self._vector_addition = vector_addition
        self._scalar_product = scalar_product
        self._euclidean_distance = euclidean_distance
    
    @property
    def convert_vector_to_coord(self) -> ConvertVectorToCoordTransaction:
        return self._converter
    
    @property
    def add_vector_to_coord(self) -> CoordAdditionTransaction:
        return self._vector_addition
    
    @property
    def scalar_product(self) -> CoordScalarProduct:
        return self._scalar_product
    
    @property
    def euclidean_distance(self) -> EuclideanDistance:
        return self._euclidean_distance