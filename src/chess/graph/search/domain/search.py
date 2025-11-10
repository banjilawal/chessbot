# src/chess/graph/search/domain/search

"""
Module: chess.graph.search.domain.search
Author: Banji Lawal
Created: 2025-11-09
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.piece import Piece
from chess.graph import Graph, GraphDomainFilter, graph
from chess.system import LoggingLevelRouter, Search, SearchResult
from chess.domain import (
    Domain, DomainValidator, GraphSearchContext, GraphSearchContextValidator, ResidentSearchCoordCollisionException,
    ResidentSearchIdCollisionException, ResidentSearchNameCollisionException
)


class GraphDomainSearch(Search[Graph, Domain]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def search(cls, data_owner: Graph, search_context: GraphDomainFilter) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch.search"
        
        try:
            graph_validator = GraphValidator.validate(data_owner)
            if graph_validation.is_failure():
                return SearchResult.failure(graph_validation.exception)
            
            filter_validation = GraphSearchContextValidator.validate(search_context)
            if filter_validation.is_failure():
                return SearchResult.failure(filter_validation.exception)
            
            if search_context.id is not None:
                return cls._id_search(graph=data_owner, id=search_context.id)
            
            if search_context.name is not None:
                return cls._name_search(graph=data_owner, name=search_context.name)
            
            if search_context.root is not None:
                return cls._root_search(graph=data_owner, coord=search_context.root)
            
            if search_context.previous_root is not None:
                return cls._previous_root_search(graph=data_owner, coord=search_context.previous_root)
            
            if search_context.point is not None:
                return cls._point_search(graph=data_owner, coord=search_context.point)
            
            if search_context.rank_name is not None:
                return cls._rank_name_search(graph=data_owner, name=search_context.rank_name)
            
            if search_context.ransom is not None:
                return cls._ransom_search(graph=data_owner, ransom=search_context.point)
            
            if search_context.team_id is not None:
                return cls._team_id_search(graph=data_owner, id=search_context.team_id)
            
            if search_context.team_name is not None:
                return cls._team_name_search(graph=data_owner, name=search_context.team_name)
            
            if search_context.resident:
                return cls._resident_search(graph=data_owner, piece=search_context.resident)
        
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _id_search(cls, graph: Graph, id: int) -> SearchResult[List[Domain]]
        """"""
        method = "GraphDomainSearch._id_search"
    
        try:
            matches = [domain for domain in graph.domains if domain.owner.id == id]
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) == 1:
                return SearchResult.success(matches)
            else:
                return cls._resolve_duplicate_ids(graph=graph, duplicates=matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _name_search(cls, graph: Graph, name: str) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._name_search"
    
        try:
            matches = [domain for domain in graph.domains if domain.owner.name.upper == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) == 1:
                return SearchResult.success(matches)
            else:
                return cls._resolve_duplicate_names(graph=graph, duplicates=matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _root_search(cls, graph: Graph, coord: Coord) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._root_search"
    
        try:
            matches = [domain for domain in graph.domains if domain.tree_root == coord]
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) == 1:
                return SearchResult.success(matches)
            else:
                return cls._resolve_duplicate_coords(graph=graph, duplicates=matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _previous_root_search(cls, graph: Graph, coord: Coord) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._previous_root_search"
        
        try:
            matches = [domain for domain in graph.domains if domain.previous_tree_root == coord]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)

        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _rank_name_search(cls, graph: Graph, name: str) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._rank_name_search"
    
        try:
            matches = [domain for domain in graph.domains if domain.ownerr.rank.name.upper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _ransom_search(cls, graph: Graph, ransom: int) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._ransom_search"
    
        try:
            matches = [domain for domain in graph.domains if domain.owner.rank.ransom == ransom]
            if len(matches) == 0:
                return SearchResult.empty()
            
            elif len(matches) >= 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _team_id_search(cls, graph: Graph, id: int) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._team_id_search"
    
        try:
            matches = [domain for domain in graph.domains if domain.downer.team.id == id]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)
        
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _team_name_search(cls, graph: Graph, name: str) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._team_name_search"
    
        try:
            matches = [domain for domain in graph.domains if domain.owner.team.name.uppper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resident_search(cls, graph: Graph, piece: Piece) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._resident_search"
        
        try:
            matches = [domain for domain in graph.domains if piece in domain.residents]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _point_search(cls, graph: Graph, coord: Coord) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._point_search"
        
        try:
            matches = [domain for domain in graph.domains if coord in domain.tree]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)
        except Exception as e:
            return SearchResult.failure(e)

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_duplicate_ids(cls, graph: Graph, duplicates: List[Domain]) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._resolve_duplicate_ids"
            
        try:
            # Pop the first one to compare to all the others.
            target = duplicates.pop()
            
            # Each piece should have a different id, name, and current_position. Stripping all the misses from
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
                    graph=graph,
                    duplicates=duplicates,
                    target=target,
                    num_of_runs=num_of_runs
                )
                return SearchResult.success(striped_list)
        
        except ResidentSearchIdCollisionException as e:
            return SearchResult.failure(e(f"{method}: {e.DEFAULT_MESSAGE}"))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_duplicate_names(cls, graph: Graph, duplicates: List[Domain]) -> SearchResult[List[Domain]]:
        """"""
        method = "GraphDomainSearch._resolve_duplicate_names"
    
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
                    graph=graph,
                    duplicates=duplicates,
                    target=target,
                    num_of_runs=num_of_runs
                )
                return SearchResult.success(striped_list)
        
        except ResidentSearchNameCollisionException as e:
            return SearchResult.failure(e(f"{method}: {e.DEFAULT_MESSAGE}"))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_duplicate_coords(cls, graph: Graph, duplicates: List[Coord]) -> SearchResult[List[Domain]]:
        """"""                                                                                      
        method = "GraphDomainSearch._resolve_duplicate_coords"
        
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
                    graph=graph,
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
            duplicates: List[Domain],
            target: Piece,
            run_number: int
    ) -> (Domain, List[Domain]):
        """"""
        method = "GraphDomainPieceSearch._duplicate_remover"
        
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
