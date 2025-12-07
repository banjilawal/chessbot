from typing import List

from chess.checkmate.service import KingLocationRecord, KingLocationRecordBuilder
from chess.checkmate.service.location.search import KingLocationSearch
from chess.piece import KingPiece
from chess.system import LoggingLevelRouter, Result, Transaction, TransactionResult


class KingLocationPostingService(Service[KingOccupationEvent]):
    _location_table = List[KingLocationRecord]
    
    def __init__(self, location_table: List[KingLocationRecord]):
        super().__init__()
        self._location_table = location_table
        
    @@property
    def location_table(self) -> List[KingLocationRecord]:
        return self._location_table
    
    @classmethod
    @LoggingLevelRouter.monitor
    def process_request(self, request: KingOccupationEvent) -> TranactionResult[KingLocationRecord]:
        """"""
        method = "KingLocationPostingService.process_request"
        validation_result = KingOccupationEventValidator.item_validator(candidate=request)
        if validation_result.is_error():
            return TransactionResult.errored(event_update=request, exception=validation_result.exception)
        
        location_search_result = KingLocationSearch.searcher(data_owner=self._location_table, search_context=request.actor)
        if location_search_result.is_failure():
            return TransactionResult.errored(event_update=request, exception=location_search_result.exception)
           
        if location_search_result.is_success():
            return TransactionResult.errored(
                event_update=request,
                exception=CannotAddDuplicateLocationRecordException(
                    f"{method}: {CannotAddDuplicateLocationRecordException.DEFAULT_MESSAGE}"
                )
            )
        
        check_posting_search_result = CheckPostingService.find(king=request.actor, location=request.destination_square)
        if check_posting_search_result.is_failure():
            return TransactionResult.errored(event_update=request, exception=check_posting_search_result.exception)
        if check_posting_search_result.is_success():
            return TransactionResult.errored(
                event_update=request,
                exception=CannotMoveToCheckedSquareException(
                    f"{method}: {CannotMoveToCheckedSquareException.DEFAULT_MESSAGE}"
                )
            )
        
        build_result = KingLocationRecordBuilder.build(event=request)
        
        
        
        return KingLocationPostingService.add_location_record()
    
    @LoggingLevelRouter.monitor
    def add_location_record(self, record: KingLocationRecord, location_table) -> Result[KingLocationRecord]:
        
        pass