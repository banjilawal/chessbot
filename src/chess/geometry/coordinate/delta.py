from chess.exception.negative_id_exception import NullChessObjectException


class Delta:
    _row_delta: int
    _column_delta: int

    """
    Delta is an immutable class is used for shifting a Coordinate by a delta. The
    Delta is just a vector added to a Coordinate vector. 

    Attributes:
        _row_delta (int): Amount added to target coordinate's row
        _column_delta (int): Amount added to target coordinate's column
    """


    def __init__(self, row_delta: int, column_delta: int):
        method = f"Delta__init__"

        """
        Constructs a Delta instance.
        
        Args:
            row_delta (int): value for _row_delta
            column_delta (int): value fpr column_delta
            
        Raises:
            NollChessObjectException: if either row_delta or column_delta are null.
        """

        if row_delta is None:
            raise NullChessObjectException(
                f"{method}: row_delta cannot be null. Delta instantiation failed"
            )
        if column_delta is None:
            raise NullChessObjectException(
                f"{method}: column_delta cannot be null. Delta instantiation failed"
            )

        self._row_delta = row_delta
        self._column_delta = column_delta


    @property
    def row_delta(self) -> int:
        return self._row_delta


    @property
    def column_delta(self) -> int:
        return self._column_delta


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Delta):
            return False

        return (
            self._column_delta == other.column_delta and
            self._row_delta == other.row_delta
        )


    def __mul__(self, scalar: int) -> 'Delta':
        method = f"Delta.__mul__"

        """
        Multiplies the Delta by scalar value.
        
        Args:
            scalar (int): Amount to multiply the delta's dimensions by.
            
        Returns: 
            Delta:
            
        Raises:
            NollChessObjectException: If scalar is None
        """

        if scalar is None:
            raise NullChessObjectException(
                f"{method}: cannot be executed. "
                f"Cannot multiply Delta object {self.__str__} "
                f"by null scalar"
            )

        new_column_delta = self.column_delta * scalar
        new_row_delta = self.row_delta * scalar

        return Delta(row_delta=new_row_delta, column_delta=new_column_delta)


    def __str__(self):
        return f"Delta(row_delta={self._row_delta}, column_delta={self._column_delta})"