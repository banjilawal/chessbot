# src/chess/piece/finder/finder.py

"""
Module: chess.piece.finder.finder
Author: Banji Lawal
Created: 2025-10-18
version: 1.0.0
"""

from typing import List

from chess.team import Team
from chess.rank import Rank
from chess.system import LoggingLevelRouter, Finder, SearchFailedException, SearchResult
from chess.piece import Piece, PieceContext, PieceContextValidator, PieceFinderException


class PieceFinder(Finder[Piece]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search Piece collections for items which match the attribute target specified in the PieceContext parameter.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT
        *   Finder

    # PROVIDES:
        *   find: -> SearchResult[List[Piece]]

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            dataset: List[Piece],
            context: PieceContext,
            context_validator: PieceContextValidator = PieceContextValidator()
    ) -> SearchResult[List[Piece]]:
        """
        # Action:
        1.  Verify the dataset is not null and contains only Piece objects,
        2.  Use context_validator to certify the provided map.
        3.  Context attribute routes the search. Attribute value is the search target.
        4.  The outcome of the search is sent back to the caller in a SearchResult object.

        # Parameters:
            *   dataset (List[Piece]):
            *   map: PieceContext
            *   context_validator: PieceContextValidator

        # Returns:
        SearchResult[List[Piece]] containing either:
            - On success: List[piece] in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   PieceNullDatasetException
            *   PieceFinderException
        """
        method = "PieceFinder.find"
        try:
            # Don't want to run a search if the dataset is null.
            if dataset is None:
                return SearchResult.failure(
                    PieceNullDatasetException(f"{method}: {PieceNullDatasetException.DEFAULT_MESSAGE}")
                )
            # certify the map is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure:
                return SearchResult.failure(validation_result.exception)
            # After map is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by piece.id.
            if context.id is not None:
                return cls._find_by_id(dataset=dataset, id=context.id)
            # Entry point into searching by piece.designation.
            if context.name is not None:
                return cls._find_by_name(dataset=dataset, name=context.name)
            # Entry point into searching by piece.team.
            if context.team is not None:
                return cls._find_by_team(dataset=dataset, team=context.team)
            # Entry point into searching by piece.rank.
            if context.rank is not None:
                return cls._find_by_rank(dataset=dataset, team=context.rank)
            # Entry point into searching by piece's ransom.
            if context.ransom is not None:
                return cls._find_by_ransom(dataset=dataset, ransom=context.ransom)
            
            # As a failsafe send a buildResult failure if a map path was missed.
            SearchResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        
        # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )

    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Piece], id: int) -> SearchResult[List[Piece]]:
        """
        # Action:
        1.  Get the Piece with the desired id.
        2.  An id search should produce either no hits or one hit only.
        3.  Multiple unique pieces in the result indicates a problem.

        # Parameters:
            *   id (int)
            *   dataset (List[Piece])

        # Returns:
        SearchResult[List[Piece]] containing either:
            - On success: List[piece] in the payload.
            - On failure: Exception.

        # Raises:
            *   PieceFinderException
        """
        method = "PieceFinder._find_by_id"
        try:
            # IDs are unique the search should either produce no result or one unique.
            matches = [piece for piece in dataset if piece.id == id]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits. The restriction that: if match_count > 1 ==> Error is relaxed.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, dataset: List[Piece], name: str) -> SearchResult[List[Piece]]:
        """
        # Action:
        1.  Get the Piece with the desired designation.
        2.  A designation search should produce either no hits or one hit only.
        3.  Multiple unique pieces in the result indicates a problem.

        # Parameters:
            *   designation (str)
            *   dataset (List[Piece])

        # Returns:
        SearchResult[List[Piece]] containing either:
            - On success: List[piece] in the payload.
            - On failure: Exception.

        # Raises:
            *   PieceFinderException
        """
        method = "PieceFinder._find_by_name"
        try:
            # Names are unique the search should either produce no result or one unique.
            matches = [ piece for piece in dataset if piece.name.upper() == name.upper()]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits. The restriction that: if match_count > 1 ==> Error is relaxed.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
                
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(cls, dataset: List[Piece], team: Team) -> SearchResult[List[Piece]]:
        """
        # Action:
        1.  Get Pieces on the desired team.

        # Parameters:
            *   team (Team)
            *   dataset (List[Piece])

        # Returns:
        SearchResult[List[Piece]] containing either:
            - On success: List[piece] in the payload.
            - On failure: Exception.

        # Raises:
            *   PieceFinderException
        """
        method = "PieceFinder._find_by_team"
        try:
            matches = [piece for piece in dataset if piece.team == team]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_rank(cls, dataset: List[Piece], rank: Rank) -> SearchResult[List[Piece]]:
        """
        # Action:
        1.  Get Pieces of the desired rank.

        # Parameters:
            *   rank (Rank)
            *   dataset (List[Piece])

        # Returns:
        SearchResult[List[Piece]] containing either:
            - On success: List[piece] in the payload.
            - On failure: Exception.

        # Raises:
            *   PieceFinderException
        """
        method = "PieceFinder._find_by_rank"
        try:
            matches = [piece for piece in dataset if piece.rank == rank]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_ransom(cls, dataset: List[Piece], ransom: int) -> SearchResult[List[Piece]]:
        """
        # Action:
        1.  Get Pieces with the desired ransom.

        # Parameters:
            *   ransom (int)
            *   dataset (List[Piece])

        # Returns:
        SearchResult[List[Piece]] containing either:
            - On success: List[piece] in the payload.
            - On failure: Exception.

        # Raises:
            *   PieceFinderException
        """
        method = "PieceFinder._find_by_rank"
        try:
            matches = [piece for piece in dataset if piece.rank.ransom == ransom]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )