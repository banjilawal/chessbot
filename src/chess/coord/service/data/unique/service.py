# src/chess/coord/service/data/unique/service.py

"""
Module: chess.coord.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from chess.coord import AddingDuplicateCoordException, Coord, CoordDataService, UniqueCoordDataServiceException
from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService, id_emitter


class UniqueCoordDataService(UniqueDataService[Coord]):
    """"""
    
    DEFAULT_NAME = "UniqueSquareDataService"
    _id: int
    _data_service: CoordDataService
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            data_service: CoordDataService = CoordDataService(),
    ):
        super().__init__(id=id, name=name, data_service=data_service)
    
    @LoggingLevelRouter.monitor
    def push(self, item: Coord) -> InsertionResult[Coord]:
        method = "UniqueSquareDataService.push"
        try:
            validation = self._data_service.validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            
            if item in self._data_service.items:
                return InsertionResult.failure(
                    AddingDuplicateCoordException(
                        f"{method}: "
                        f"{AddingDuplicateCoordException.DEFAULT_MESSAGE}"
                    )
                )
            self._data_service.items.append(item)
            return InsertionResult.success(item)
        except Exception as ex:
            return InsertionResult.failure(
                UniqueCoordDataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{UniqueCoordDataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
