# src/chess/domain/search/context/builder.py

"""
Module: chess.domain.search.context.builder
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Optional

from chess.system import Builder, BuildResult
from chess.graph import GraphSearchContext, ZeroGraphSearchParamsException


class DomainSearchContextBuilder(Builder[DomainSearchContext]):
    """"""

    @classmethod
    def build (
        cls,
        name: Optional[str] = None,
        ransom: Optional[int] = None,
        piece_id: Optional[int] = None,
        team_id: Optional[id] = None,
        team_name: Optional[str] = None,
        rank_name: Optional[Rank] = None,
        position: Optional[Coord] = None,
    ) -> BuildResult[GraphSearchContext]:
        """"""
        method = "GraphSearchContextBuilder.build"

        try:
            params = [name, ransom, piece_id, team_id, team_name, rank_name, position]
            param_count = sum(bool(p) for p in params)

            if param_count == 0:
                return BuildResult(exception=ZeroGraphSearchParamsException(
                    f"{method}: {ZeroGraphSearchParamsException.DEFAULT_MESSAGE}"
                ))

            if param_count > 1:
                return BuildResult(exception=TooManyDiscoverySearchParamsException(
                    f"{method}: {TooManyDiscoverySearchParamsException.DEFAULT_MESSAGE}"
                ))

            if piece_id is not None:
                id_validation = IdValidator.validate(piece_id)
                if not id_validation.is_failure():
                    return BuildResult(exception=id_validation.exception)

            if name is not None:
                piece_name_validation = NameValidator.validate(name)
                if piece_name_validation.is_failure():
                    return BuildResult(exception=piece_name_validation.exception)

            if team_id is not None:
                team_id_validation = IdValidator.validate(team_id)
                if team_id_validation.is_failure():
                    return BuildResult(exception=team_id_validation.exception)

            if team_name is not None:
                team_name_validation = NameValidator.validate(team_name)
                if team_name_validation.is_failure():
                    return BuildResult(exception=team_name_validation.exception)

            if (rank_name is not None and
                rank_name not in [King.name, Queen.name, Rook.name, Bishop.name, Knight.name, Pawn.name]
            ):
                return BuildResult(exception=DiscoveryInvalidRankNameParamException(
                    f"{method}: {DiscoveryInvalidRankNameParamException.DEFAULT_MESSAGE}"
                ))

            if ransom not in range[Queen.ransom]:
                return BuildResult(exception=DiscoveryInvalidRankNameParamException(
                        f"{method}: {DiscoveryInvalidRankNameParamException.DEFAULT_MESSAGE}"
                ))

            if position is not None:
                position_validation = CoordValidator.validate(position)
                if position_validation.is_failure():
                    return BuildResult(exception=position_validation.exception)

            return BuildResult(payload=DiscoverySearchContext(
                name=name,
                ransom=ransom,
                piece_id=piece_id,
                team_id=team_id,
                team_name=team_name,
                rank_name=rank_name,
                position=position
            ))
        except Exception as e:
            return BuildResult(exception=e)