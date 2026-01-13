# src/chess/square/service/data/service.py

"""
Module: chess.square.service.data.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import List, cast

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
from chess.square import Square, SquareContext, SquareContextService, SquareDataServiceException, SquareService


class SquareDataService(DataService[Square]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Square objects and their lifecycles.
    3.  Ensure integrity of Square data stack
    4.  Stack data structure for Square objects with no guarantee of uniqueness.

    # PARENT:
        *   DataService[Square]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "SquareDataService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Square] = List[Square],
            service: SquareService = SquareService(),
            context_service: SquareContextService = SquareContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   items (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "SquareService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def square_service(self) -> SquareService:
        return cast(SquareService, self.entity_service)
    
    @property
    def square_context_service(self) -> SquareContextService:
        return cast(SquareContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def add_square(self, square: Square) -> InsertionResult[Square]:
        """
        # ACTION:
            1.  If the square is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   square (Square)
        # RETURNS:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareDataServiceException
        """
        method = "SquareDataService.add_square"
        
        # Handle the case that the square is unsafe.
        validation = self.square_service.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        
        search_result = self.square_context_service.finder.f
        
        push_result = self.push_item(item=square)
        # Handle the case that super().push_item fails
        if push_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=push_result.exception
                    )
                )
            )
        # On success cast the payload and return to the caller in an insertion result.
        return push_result
    
    @LoggingLevelRouter.monitor
    def delete_square_by_id(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[
        Square]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_squares_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_squares_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareDataServiceException
        """
        method = "SquareDataService.remove_square_by_id"
        
        # Handle the case of an unsafe id.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareDeletionFailedException(
                        message=f"{method}: {SquareDeletionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        for item in self.items:
            if item.id == id:
                square = cast(Square, item)
                self.items.remove(square)
                return DeletionResult.success(payload=square)
        return DeletionResult.nothing()
    #
    #
    # @LoggingLevelRouter.monitor
    # def delete_by_designation(
    #         self,
    #         designation: str,
    #         identity_service: IdentityService = IdentityService()
    # ) -> DeletionResult[Square]:
    #     """
    #     # ACTION:
    #         1.  If the designation is not certified safe send the exception in the DeletionResult. Else, call
    #             _delete_squares_by_search_result with the outcome of an id search.
    #         2.  Forward the DeletionResult from _delete_squares_by_search_result to the deletion client.
    #     # PARAMETERS:
    #                 *   designation (str)
    #                 *   identity_service (IdentityService)
    #     # RETURNS:
    #         *   InsertionResult[Square] containing either:
    #                 - On failure: Exception.
    #                 - On success: Square in the payload.
    #     # RAISES:
    #         *   SquareDataServiceException
    #     """
    #     method = "SquareDataService.remove_square_by_designation"
    #
    #     # Handle the case of an unsafe designation.
    #     validation = identity_service.validate_name(candidate=designation)
    #     if validation.is_failure:
    #         # Return the exception chain on failure.
    #         return DeletionResult.failure(
    #             SquareDataServiceException(
    #                 message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
    #                 ex=validation.exception
    #             )
    #         )
    #     # # Pass the results of a designation search to the deletion helper.
    #     search_result = self.square_context_service.finder.find(context=SquareContext(designation=designation))
    #     return self._delete_squares_by_search_result(search_result=search_result)
    #
    # @LoggingLevelRouter.monitor
    # def _delete_squares_by_search_result(self, search_result: SearchResult) -> DeletionResult[Square]:
    #     """
    #     # ACTION:
    #         1.  If the search_result param is a failure send the exception in the DeletionResult.
    #         2.  If the search_result param is empty there is nothing to delete, send the exception in the
    #             DeletionResult.
    #         3.  If the search_result was a success delete all copies of the target in from the dataset then,
    #             send the deleted item in the DeletionResult.
    #     # PARAMETERS:
    #                 *   search_result (SearchResult[Square])
    #     # RETURNS:
    #         *   DeletionResult[Square] containing either:
    #                 - On failure: Exception.
    #                 - On success: Square in the payload.
    #     # RAISES:
    #         *   SquareDataServiceException
    #         8   SquareDoesNotExistForRemovalException
    #     """
    #     method = "SquareDataService._delete_squares_by_search_result"
    #
    #     # Handle the case that the search fails
    #     if search_result.is_failure:
    #         # Return the exception chain on failure.
    #         return DeletionResult.failure(
    #             SquareDataServiceException(
    #                 message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
    #                 ex=search_result.exception
    #             )
    #         )
    #     # Handle the case that square does not exist in the dataset.
    #     if search_result.is_empty:
    #         # Return the exception chain on failure.
    #         return DeletionResult.failure(
    #             SquareDataServiceException(
    #                 message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
    #                 ex=SquareDoesNotExistForRemovalException(
    #                     f"{method}: {SquareDoesNotExistForRemovalException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         )
    #     # Cast the payload to the array of matches, Then remove all occurrences in a loop
    #     matches = cast(List[Square], search_result.payload)
    #     square_removed = matches[0]
    #     # Python remove is not exhaustive hence the loop.
    #     for square in matches:
    #         self.items.remove(square)
    #     # Send the square_removed in the DeletionResult to confirm success.
    #     return DeletionResult.success(payload=square_removed)