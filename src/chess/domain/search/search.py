# src/chess/piece/search/search.py

"""
Module: chess.search.search
Author: Banji Lawal
Created: 2025-10-18
version: 1.0.0
"""


from typing import List

from chess.coord import Coord
from chess.system import LoggingLevelRouter, Search, SearchResult
from chess.piece import (
    Piece, PieceValidator, Discovery, DiscoverySearchContext, DiscoverySearchContextValidator,
    DiscoverySearchCoordCollisionException, DiscoverySearchIdCollisionException, DiscoverySearchNameCollisionException,
)


class DiscoverySearch(Search[Piece, Discovery]):
    """
      # ROLE: Builder implementation

      # RESPONSIBILITIES:
      1. Process and validate parameters for creating `Checker` instances.
      2. Create new `Checker` objects if parameters meet specifications.
      2. Report errors and return `BuildResult` with error details.

      # PROVIDES:
      `BuildResult`: Return type containing the built `Checker` or error information.

      # ATTRIBUTES:
      None
      """

    @classmethod
    @LoggingLevelRouter.monitor
    def search(cls, data_owner: Piece, search_context: DiscoverySearchContext, *args, **kwargs) -> SearchResult[List[Discovery]]:
        """"""
        method = "DiscoverySearch.search"

        owner_validation = PieceValidator.validate(data_owner)
        if not owner_validation.is_failure():
          return SearchResult(exception=owner_validation.exception)

        search_context_validation = DiscoverySearchContextValidator.validate(search_context)
        if not search_context_validation.is_success():
          return SearchResult(exception=search_context_validation.exception)
          
        if search_context.piece_id is not None:
            return DiscoverySearch._piece_id_search(piece=data_owner, piece_idid=search_context.piece_id)
        
        if search_context.name is not None:
            return DiscoverySearch._name_search(piece=data_owner, name=search_context.name)
        
        if search_context.rank_name is not None:
            return DiscoverySearch._rank_search(piece=data_owner, rank_name=search_context.rank_name)
        
        if search_context.discovery_id is not None:
            return DiscoverySearch._discovery_id_search(piece=data_owner, discovery_id=search_context.discovery_id)
        
        if search_context.discovery_name is not None:
            return DiscoverySearch._discovery_name_search(piece=data_owner, discovery_name=search_context.discovery_name)
        
        if search_context.current_position is not None:
            return DiscoverySearch._position_search(piece=data_owner, ransom=search_context.current_position)
        
        return SearchResult()

    @classmethod
    @LoggingLevelRouter.monitor
    def _piece_id_search(cls, piece: Piece, piece_id: int) -> SearchResult[List[Discovery]]:
        """"""
        method = "DiscoverySearch._piece_id_search"
        try:
            matches = [discovery for discovery in piece.discoveries if discovery.id == piece_id]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return DiscoverySearch._resolve_matching_ids(matches=matches, piece=piece)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _name_search(cls, piece: Piece, name: str) -> SearchResult[List[Discovery]]:
        """"""
        method = "DiscoverySearch._name_search"
        try:
            matches = [discovery for discovery in piece.discoveries if discovery.name.upper == name.upper()]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return DiscoverySearch._resolve_matching_names(piece=piece, matches=matches)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _ransom_search(cls, piece: Piece, ransom: int) -> SearchResult[List[Discovery]]:
        """"""
        method = "DiscoverySearch._ransom_search"
        try:
            matches = [discovery for discovery in piece.discoveries if discovery.ransom == ransom]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return DiscoverySearch._resolve_matching_ids(matches=matches, piece=piece)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _discovery_id_search(cls, piece: Piece, discovery_id: int) -> SearchResult[List[Discovery]]:
        """"""
        method = "DiscoverySearch._discovery_id_search"
        try:
            matches = [discovery for discovery in piece.discoveries if discovery.discovery_id == discovery_id]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return DiscoverySearch._resolve_matching_ids(matches=matches, piece=piece)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _discovery_name_search(cls, piece: Piece, discovery_name: str) -> SearchResult[List[Discovery]]:
        """"""
        method = "DiscoverySearch._piece_discovery_name_search"
        try:
            matches = [discovery for discovery in piece.discoveries if discovery.discovery_name.upper() == discovery_name.upper()]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return DiscoverySearch._resolve_matching_ids(matches=matches, piece=piece)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _rank_name_search(cls, piece: Piece, rank_name: str) -> SearchResult[List[Discovery]]:
        """"""
        method = "DiscoverySearch._rank_name_search"
        try:
            matches = [discovery for discovery in piece.discoveries if discovery.rank_name.upper() == rank_name.upper()]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return DiscoverySearch._resolve_matching_names(piece=piece, matches=matches)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _position_search(cls, piece: Piece, position: Coord) -> SearchResult[List[Discovery]]:
        method = "DiscoverySearch._position_search"
        try:
            matches = [discovery for discovery in piece.discoveries if discovery.position == position]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return DiscoverySearch._resolve_matching_positions(piece=piece, matches=matches)
        except Exception as e:
            return SearchResult(exception=e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_ids(cls, piece: Piece, matches: List[Discovery]) -> SearchResult[List[Discovery]]:
        method = "DiscoverySearch._resolve_matching_ids"
        target = matches.pop()
        misses = [discovery for discovery in matches if discovery.id == target.id and (
            discovery.name.upper() != target.name.upper() or
            discovery.position != target.position or
            discovery.discovery_id != target.discovery_id or
            discovery.discovery_name.upper() != target.discovery_name.upper() or
            discovery.rank_name != target.rank_name.upper() or
            discovery.ransom != target.ransom
        )
                  ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for discovery in matches:
                if (
                    discovery.id == target.id and
                    piece.name.upper() == target.name.upper() and
                    discovery.position == target.position and
                    discovery.discovery_id == target.discovery_id and
                    discovery.discovery_name.upper() == target.discovery_name.upper() and
                    discovery.rank_name == target.rank_name.upper() and
                    discovery.ransom == target.ransom
                ):
                    piece.discoveries.remove(discovery)
                    matches.remove(discovery)
            return SearchResult(payload=matches)
        return SearchResult(
            exception=DiscoverySearchIdCollisionException(
                f"{method}: {DiscoverySearchIdCollisionException.DEFAULT_MESSAGE}"
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_names(cls, piece: Piece, matches: List[Discovery]) -> SearchResult[List[Discovery]]:
        method = "DiscoverySearch._resolve_matching_names"
        target = matches.pop()
        misses = [discovery for discovery in matches if discovery.name.upper() == target.name.upper() and (
            discovery.id != target.id or
            discovery.position != target.position or
            discovery.discovery_id != target.discovery_id or
            discovery.discovery_name.upper() != target.discovery_name.upper() or
            discovery.rank_name != target.rank_name.upper() or
            discovery.ransom != target.ransom
        )]

        if len(misses) == 0:
            DiscoverySearch._remove_duplicates(piece=piece, target=target, number_of_duplicates=len(piece.discoveries))
            return SearchResult(payload=[target])
        return SearchResult(
            exception=DiscoverySearchNameCollisionException(
            f"{method}: {DiscoverySearchNameCollisionException.DEFAULT_MESSAGE}"
        ))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_positions(cls, piece: Piece, matches: List[Discovery]) -> SearchResult[List[Discovery]]:
        method = "DiscoverySearch._resolve_matching_positions"
        target = matches.pop()
        misses = [discovery for discovery in matches if discovery.position == target.position and (
            discovery.id != target.id or
            discovery.name.upper() != target.name.upper() or
            discovery.discovery_id != target.discovery_id or
            discovery.discovery_name.upper() != target.discovery_name.upper() or
            discovery.rank_name != target.rank_name.upper() or
            discovery.ransom != target.ransom
        )]

        if len(misses) == 0:
            DiscoverySearch._remove_duplicates(piece=piece, target=target, number_of_duplicates=len(piece.discoveries))
            return SearchResult(payload=[target])
        return SearchResult(exception=DiscoverySearchCoordCollisionException(
            f"{method}: {DiscoverySearchCoordCollisionException.DEFAULT_MESSAGE}"
        ))
    
    @classmethod
    def _remove_duplicates(cls, piece: Piece, target: Discovery, number_of_duplicates):
        for i in range (number_of_duplicates):
            piece.discoveries.remove(target)
        piece.discoveries.append(target)