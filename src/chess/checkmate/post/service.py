# src/chess/checkmate/post/service.py

"""
Module: chess.checkmate.post.service
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""
from chess.system import LoggingLevelRouter


class KingCheckDeliveryService:
    
    @staticmethod
    @LoggingLevelRouter.monitor
    def receive_record(record: KingCheckRecord) -> SubmissionReceipt:
        pass
    
    @staticmethod
    @LoggingLevelRouter.monitor
    def post_record(record_table: KingCheckRecordTable, poster: Piece, record: KingCheckRecord) -> Result[KingCheckPosting]:
        pass