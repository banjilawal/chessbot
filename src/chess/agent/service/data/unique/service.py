# src/chess/agent/service/data/unique/service_.py

"""
Module: chess.agent.service.data.unique.entity_service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService
from chess.agent import AddingDuplicateAgentException, Agent, AgentDataService, UniqueAgentDataServiceException



class UniqueAgentDataService(UniqueDataService[Agent]):
    DEFAULT_NAME = "UniqueAgentDataService"
    _data_service = AgentDataService
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            data_service: AgentDataService =AgentDataService()
    ):
        super().__init__(id=id, name=name, data_service=data_service)
    
    # @LoggingLevelRouter.monitor
    # def push_unique_item(self, item: Agent) -> InsertionResult[Agent]:
    #     method = "UniqueAgentDataService.push_unique"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #
    #         context_validation = self._data_service.context_service.item_builder.build(id=item.id)
    #         if context_validation.is_failure():
    #             return InsertionResult.failure(context_validation.exception)
    #
    #         search_result = self._data_service.search(context=context_validation.payload)
    #         if search_result.is_failure():
    #             return InsertionResult.failure(search_result.exception)
    #
    #         if search_result.is_success():
    #             return InsertionResult.failure(
    #                 AddingDuplicateAgentException(
    #                     f"{method}: {AddingDuplicateAgentException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         return self._data_service.push_item(item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             UniqueAgentDataServiceException(
    #                 ex=ex,
    #                 message=(
    #                     f"{method}: "
    #                     f"{UniqueAgentDataServiceException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         )
