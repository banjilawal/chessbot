# src/logic/mate/post/requestor.py

"""
Module: logic.mate.post.requestor
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from abc import abstractmethod

from logic.piece import KingPiece, Piece
from system import LoggingLevelRouter, Result
from logic.checkmate import CheckPostalService, CheckRecord


class CheckRequestor:
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def submit_check_request(service: CheckPostalService, submitter: Piece, enemy_king: KingPiece) -> Result[CheckRecord]:
        return service.post_record()
