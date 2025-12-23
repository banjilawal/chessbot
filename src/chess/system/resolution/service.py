# src/chess/system/resolution/service.py

"""
module: chess.system.resolution.service
author: Banji Lawal
date: 2025-11-20
version: 0.0.1
"""


from abc import ABC
from typing import Generic, TypeVar

from chess.system.service import EntityService

T = TypeVar("T")


class CollisionResolutionService(EntityService[ABC, Generic[T]]):
    """"""""
    pass

"""
Sorting
1.  if the piece.team.player.game.id != lock.game.id:
    deliver_to_game_level_resolver.(piece)
2.  if piece.team.player.id != lock.player.id:
    deliver_to_player_level_resolver.(piece)
3.  if piece.team.id != lock.team.id:
    deliver_to_team_level_resolver.(piece)
4.  If piece.id == lock.id:
    pieces.remove(piece)
5.  lock = pieces.pop(0)
 I felt ashamed
"""