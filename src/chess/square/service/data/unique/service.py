# src/chess/square/service/data/unique/service.py

"""
Module: chess.square.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List

from chess.square import (
    AddingDuplicateSquareException, ExhaustiveSquareDeletionFailedException, Square, SquareContext, SquareContextService,
    SquareDataService, SquareService, UniqueSquareDataServiceException, UniqueSquareInsertionFailedException,
    UniqueSquareSearchFailedException
)
from chess.system import (
    DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, SearchResult, UniqueDataService, id_emitter
)


class UniqueSquareDataService(UniqueDataService[Square]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all items in managed by SquareDataService are unique.
    2.  Guarantee consistency of records in SquareDataService.

    # PARENT:
        *   UniqueDataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UniqueDataService class for inherited attributes.
    """
    SERVICE_NAME = "UniqueSquareDataService"
    _square_data_service: SquareDataService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: SquareDataService = SquareDataService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   data_service (SquareDataService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._square_data_service = data_service
    
    @property
    def integrity_service(self) -> SquareService:
        return self._square_data_service.square_service
    
    @property
    def context_service(self) -> SquareContextService:
        return self._square_data_service.context_service
    
    @property
    def size(self) -> int:
        return self._square_data_service.size
    
    @property
    def is_empty(self) -> bool:
        return self._square_data_service.is_empty
    
    @LoggingLevelRouter.monitor
    def add_unique_square(self, square: Square) -> InsertionResult[Square]:
        """
        # ACTION:
            1.  If the square fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the square either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _square_data_service.insert_square fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   square (Square)
        # RETURN:
            *   InsertionResult[Square] containing either:
                    - On failure: An exception.
                    - On success: Square in payload.
        # RAISES:
            *   UniqueSquareDataServiceException
            *   UniqueSquareInsertionFailedException
            *   UniqueSquareDataServiceException
        """
        method = "UniqueSquareDataService.add_unique_square"
        
        # --- To assure uniqueness the data_service has to conduct a search. The square should be validated first. ---#
        
        # Handle the case that the square is not certified safe.
        validation = self.integrity_service.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueSquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueSquareDataServiceException.ERROR_CODE}",
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Check if the square is already in the dataset before adding it. ---#
        search_result = self.search_squares(context=SquareContext(id=square.id))
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueSquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueSquareDataServiceException.ERROR_CODE}",
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that the square is already in the dataset.
        if search_result.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueSquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueSquareDataServiceException.ERROR_CODE}",
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
                        ex=AddingDuplicateSquareException(f"{method}: {AddingDuplicateSquareException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Use _square_data_service.insert_square because order does not matter for the square access. ---#
        insertion_result = self._square_data_service.insert_square(square=square)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueSquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueSquareDataServiceException.ERROR_CODE}",
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_squares(self, context: SquareContext) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the result of calling _square_data_service.delete_square_by_id for method. If the deletion failed
                wrap the exception inside the appropriate UniqueDataService exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Square] containing either:
                    - On failure: An exception.
                    - On success: Square in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   UniqueSquareDataServiceException
            *   ExhaustiveSquareDeletionFailedException
        """
        method = "UniqueSquareDataService.search_squares"
        
        # --- Handoff the search responsibility to _square_data_service. ---#
        search_result = self._square_data_service.square_context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                UniqueSquareDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueSquareDataServiceException.ERROR_CODE}",
                    ex=UniqueSquareSearchFailedException(
                        message=f"{method}: {UniqueSquareSearchFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result