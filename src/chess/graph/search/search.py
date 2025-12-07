# src/chess/domain/searcher/service.py

"""
Module: chess.domain.searcher.searcher
Author: Banji Lawal
Created: 2025-11-09
version: 1.0.0
"""


from typing import List

from chess.coord import Coord
from chess.piece import Piece
from chess.system import LoggingLevelRouter, Finder, SearchResult
from chess.domain import (
    Domain, DomainValidator, VisitorSearchContext, VisitorSearchContextValidator, ResidentSearchCoordCollisionException,
    ResidentSearchIdCollisionException, ResidentSearchNameCollisionException
)


class DomainVisitorFinder(Finder[Domain, Piece]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def search(cls, data_owner: Domain, search_context: VisitorSearchContext) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder.searcher"
        
        try:
            domain_validation = DomainValidator.validate(data_owner)
            if domain_validation.is_failure():
                return SearchResult.failure(domain_validation.exception)
            
            search_context_validation = VisitorSearchContextValidator.validate(search_context)
            if search_context_validation.is_failure():
                return SearchResult.failure(search_context_validation.exception)
            
            if search_context.visitor_id is not None:
                return cls._id_search(domain=data_owner, id=search_context.visitor_id)
            
            if search_context.visitor_name is not None:
                return cls._name_search(domain=data_owner, name=search_context.visitor_name)
            
            if search_context.point is not None:
                return cls._coord_search(domain=data_owner, coord=search_context.point)
            
            if search_context.visitor_rank is not None:
                return cls._rank_name_search(domain=data_owner, coord=search_context.point)
            
            if search_context.visitor_ransom is not None:
                return cls._ransom_search(domain=data_owner, coord=search_context.point)
            
            if search_context.team_id is not None:
                return cls._team_id_search(domain=data_owner, coord=search_context.point)
            
            if search_context.visitor_team is not None:
                return cls._team_name_search(domain=data_owner, coord=search_context.point)
        
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _id_search(cls, domain: Domain, id: int) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._id_search"
        
        try:
            matches = [visitor for visitor in domain.residents if visitor.id == id]
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) == 1:
                return SearchResult.success(matches)
            else:
                return cls._resolve_duplicate_ids(duplicates=matches, domain=domain)
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _name_search(cls, domain: Domain, name: str) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._name_search"
        
        try:
            matches = [visitor for visitor in domain.residents if visitor.name.upper == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) == 1:
                return SearchResult.success(matches)
            else:
                return cls._resolve_duplicate_names(duplicates=matches, domain=domain)
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _coord_search(cls, domain: Domain, coord: Coord) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._coord_search"
        
        try:
            matches = [visitor for visitor in domain.visitor if visitor.current_position == coord]
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) == 1:
                return SearchResult.success(matches)
            else:
                return cls._resolve_duplicate_coords(matches=matches, domain=domain)
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _rank_name_search(cls, domain: Domain, rank_name: str) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._rank_name_search"
        
        try:
            matches = [visitor for visitor in domain.residents if visitor.rank.name.upper() == rank_name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) == 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _ransom_search(cls, domain: Domain, ransom: int) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._ransom_search"
        
        try:
            matches = [visitor for visitor in domain.residents if visitor.rank.ransom == ransom]
            if len(matches) == 0:
                return SearchResult.empty()
            
            elif len(matches) == 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _team_id_search(cls, domain: Domain, id: int) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._team_id_search"
        
        try:
            matches = [visitor for visitor in domain.visitor if visitor.team_name.visitor_id == id]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) == 1:
                return SearchResult.success(matches)
        
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _team_name_search(cls, domain: Domain, name: str) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._team_name_search"
        
        try:
            matches = [visitor for visitor in domain.visitor if visitor.team_name.visitor_name.uppper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) == 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_duplicate_ids(cls, domain: Domain, duplicates: List[Piece]) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._resolve_duplicate_ids"
        
        try:
            # Pop the first one to compare to all the others.
            target = duplicates.pop()
            
            # Each piece should have a different visitor_id, visitor_name, and current_position. Stripping all the misses from
            # the target should only leave duplicates
            uniques = [
                piece for piece in duplicates if piece.id == target.id and (
                        piece.name.upper() != target.name.upper() or piece.current_position != target.current_position
                )
            ]
            
            # If everything was a match remove all the duplicates and send the SearchResult to the client.
            if len(uniques) == 0:
                # Get the number of times the duplicate removal loop has to run to leave only one value in
                # The recursive implementation is the best one not iterative
                num_of_runs = len(duplicates) - 1
                striped_list = cls._duplicate_remover(
                    domain=domain,
                    duplicates=duplicates,
                    target=target,
                    num_of_runs=num_of_runs
                )
                return SearchResult.success(striped_list)
        
        except ResidentSearchIdCollisionException as e:
            return SearchResult.failure(e(f"{method}: {e.DEFAULT_MESSAGE}"))
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_duplicate_names(cls, domain: Domain, duplicates: List[Piece]) -> SearchResult[List[Piece]]:
        """"""
        method = "DomainResidentFinder._resolve_duplicate_names"
        
        try:
            target = duplicates.pop()
            uniques = [
                piece for piece in duplicates if piece.name.upper() == target.name.upper() and (
                        piece.id != target.id or piece.current_position != target.current_position
                )
            ]
            
            if len(uniques) == 0:
                # Get the number of times the duplicate removal loop has to run to leave only one value in
                # The recursive implementation is the best one not iterative
                num_of_runs = len(duplicates) - 1
                striped_list = cls._duplicate_remover(
                    domain=domain,
                    duplicates=duplicates,
                    target=target,
                    num_of_runs=num_of_runs
                )
                return SearchResult.success(striped_list)
        
        except ResidentSearchNameCollisionException as e:
            return SearchResult.failure(e(f"{method}: {e.DEFAULT_MESSAGE}"))
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_duplicate_coords(cls, domain: Domain, duplicates: List[Coord]) -> SearchResult[List[Piece]]:
        method = "DomainPiceSearch._resolve_duplicate_coords"
        try:
            target = duplicates.pop()
            uniques = [
                piece for piece in duplicates if piece.current_position == target.current_position and (
                        piece.name.upper() != target.name.upper() or piece.id != target.id
                )
            ]
            
            if len(uniques) == 0:
                # Get the number of times the duplicate removal loop has to run to leave only one value in
                # The recursive implementation is the best one not iterative
                num_of_runs = len(duplicates) - 1
                striped_list = cls._duplicate_remover(
                    domain=domain,
                    duplicates=duplicates,
                    target=target,
                    num_of_runs=num_of_runs
                )
                return SearchResult.success(striped_list)
        except ResidentSearchCoordCollisionException as e:
            return SearchResult.failure(e(f"{method}: {e.DEFAULT_MESSAGE}"))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _duplicate_remover(
            cls,
            domain: Domain,
            duplicates: List[Piece],
            target: Piece,
            run_number: int
    ) -> (Domain, List[Piece]):
        """"""
        method = "DomainVisitorPieceSearch._duplicate_remover"
        
        if run_number == 0:
            return duplicates
        
        if run_number > 0:
            for visitor in domain.residents:
                if (
                        visitor.id == target.id and
                        visitor.name.upper() == target.name.upper() and
                        visitor.current_position == target.current_position
                ):
                    domain.residents.remove(visitor)
                    duplicates.remove(visitor)
                    return cls._duplicate_remover(domain, duplicates, target, run_number - 1)
        return
