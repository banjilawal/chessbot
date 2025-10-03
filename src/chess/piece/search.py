
from chess.coord import Coord, CoordValidator
from chess.piece import Piece, PieceValidator, Discovery
from chess.system import SearchResult, IdValidator, NameValidator

class PieceSearch:
    """
    Static methods for entities and operations that need to search a Piece for discoveries. `CoordStack` does not
    need searching because only the current coord is used in operations.

    PieceSearch provides consistent search interface and return types across all search operations.
    Validates input parameters before searching to ensure safe operations.Returns SearchResult objects
    encapsulating either the found entity or exception information.

    Usage:
        ```python
        from chess.piece import Piece, PieceSearch
        from chess.piece import Piece
        ```
    Note:
        DO NOT USE ANY OTHER METHODS TO SEARCH A PIECE's DISCOVERIES. USE ONLY THE METHODS IN THIS CLASS.

    See Also:
        `Piece`: Object owning `discovery`.
        `Coord`: The coordinate being searched for
        `Discovery`: A discovery a `piece` recorded in its blocked square history
        `Discoveries`: The list of discoveries made by a `piece`
        `SearchResult`: The return type for all search operations
    """

    @staticmethod
    def discovery_id(discovery_id: int, piece: Piece) -> SearchResult['Discovery']:
        """
        Find a `discovery`` within the given `piece`. `Discovery_id` is the `id` of
            * Friendly piece blocking `Square`
            * Enemy `KingPiece` that cannot be captured only checked or checkmated.
        Args:
          `discovery_id` (`id`): A valid id
          `piece` (`Piece`): a valid piece

        Returns:
              SearchResult[Discovery]: A `SearchResult` containing either:
                  - On success: The validated Team instance in the payload
                  - On not found: An empty `SearchResult` (payload is None, exception is None)
                  - On failure: Error information and exception details
        Raises:
            `InvalidIdException`
            `InvalidPieceException`
        """
        method = "PieceSearch.discovery_id"

        try:
            id_validation = IdValidator.validate(discovery_id)

            if not id_validation.is_success():
                return SearchResult(exception=id_validation.exception)

            piece_validation = PieceValidator.validate(piece)
            if not piece_validation.is_success():
                return SearchResult(exception=piece_validation.exception)

            hit = next((discovery for discovery in piece.discoveries if discovery.id == discovery_id), None)
            if hit is not None:
                return SearchResult(payload=hit)

           # returns empty search result
            return SearchResult()

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def discovery_name(name: str, piece: Piece) -> SearchResult['Discovery']:
        """
        Find a `discovery`` within the given `piece` by a name. Multiple pieces may have
        marked the same item in their history.
        Args:
          `name` (`str`): A valid name
          `piece` (`Piece`): a valid piece

        Returns:
              SearchResult[Discovery]: A `SearchResult` containing either:
                  - On success: The validated Team instance in the payload
                  - On not found: An empty `SearchResult` (payload is None, exception is None)
                  - On failure: Error information and exception details
        Raises:
            `InvalidNameException`
            `InvalidPieceException`
        """
        method = "PieceSearch.discovery_name"

        try:
            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                return SearchResult(exception=name_validation.exception)

            piece_validation = PieceValidator.validate(piece)
            if not piece_validation.is_success():
                return SearchResult(exception=piece_validation.exception)

            hit = next((discovery for discovery in piece.discoveries if discovery.name.upper() == name), None)
            if hit is not None:
                return SearchResult(payload=hit)

            # Return empty search result
            return  SearchResult()

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def discovery_by_coord(coord: Coord, piece: Piece) -> SearchResult['Discovery']:
        """
        Find a `discovery` within the given `piece` by a `Coord``. Multiple pieces may have
        marked the same item in their history. `Piece.dicoveries` is cleared at each term so search by coord
        always gives a unique result or none at a turn.

        Args:
          `coord` (`Coord`): A valid `Coord`
          `piece` (`Piece`): a valid piece

        Returns:
              SearchResult[Team]: A `SearchResult` containing either:
                  - On success: The validated Team instance in the payload
                  - On not found: An empty `SearchResult` (payload is None, exception is None)
                  - On failure: Error information and exception details
        Raises:
            `InvalidIdException`
            `InvalidTeamException`
        """
        method = "PieceSearch.by_coord"
        try:
            coord_validation = CoordValidator.validate(coord)
            if not coord_validation.is_success():
                return SearchResult(exception=coord_validation.exception)

            piece_validation = PieceValidator.validate(piece)
            if not piece_validation.is_success():
                return SearchResult(exception=piece_validation.exception)

            hit = next((discovery for discovery in piece.discoveries if discovery.coord == coord), None)
            if hit is not None:
                return SearchResult(payload=hit)

            # Return empty search result
            return SearchResult()

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)
