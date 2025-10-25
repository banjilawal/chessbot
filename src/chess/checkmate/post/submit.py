# src/chess/checkmate/post/submit.py

"""
Module: chess.checkmate.post.submit
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""
from chess.checkmate import CheckRecord
from chess.piece import Piece
from chess.system import LoggingLevelRouter


class SubmitKingCheckRecord:
    
    @staticmethod
    @LoggingLevelRouter.monitor
    def submit_record(submitter: Piece, record: CheckRecord):
        pass
