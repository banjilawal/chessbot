# src/logic/pair/listing/service/service.py

"""
Module: logic.pair.listing.service.service
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from logic.node import Node
from logic.pair import PairList, PairListBuilder, PairListValidationProcess, PairService
from logic.pair.listing.service import PairListServiceException
from logic.system import IdFactory, IntegrityService, LoggingLevelRouter, SearchResult


class PairListService(IntegrityService[PairList]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing PairList microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for PairList state by providing
        single entry and exit points to PairList lifecycle.

    Super Class:
        *   IntegrityService

    Provides:

    # LOCAL ATTRIBUTES:
        *   pair_service:   PairService

    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "PairListService"
    _pair_service: PairService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            pair_service: PairService = PairService(),
            builder: PairListBuilder = PairListBuilder(),
            validator: PairListValidationProcess = PairListValidationProcess(),
            id: int = IdFactory.next_id(class_name="PairListService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: PairListBuilder
            pair_service: PairService
            validator: PairListValidationProcess
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._pair_service = pair_service
    
    @property
    def builder(self) -> PairListBuilder:
        return cast(PairListBuilder, self.entity_builder)
    
    @property
    def validator(self) -> PairListValidationProcess:
        return cast(PairListValidationProcess, self.entity_validator)
    
    @property
    def pair_service(self) -> PairService:
        return self._pair_service

    @LoggingLevelRouter.monitor
    def unique_nodes(self, pair_list: PairList) -> SearchResult[List[Node]]:
        """
        Action:
            1.  Put topmost head into the list
            2.  Put tail of each couple into the list if it's not present.
            3.  Return the list of unique nodes.
            
        Args:
            pair_list: PairList
            
        Returns:
            SearchResult[List[Node]]
            
        Raises:
            None
        """
        method = f"{self.__class__.__name__}.unique_nodes"
        
        # Handle the case that, the pair_list is not certified as safe.
        validation_result = self.validator.validate(pair_list)
        if validation_result.is_failure:
            return SearchResult.failure(
                PairListServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PairListServiceException.MSG,
                    err_code=PairListServiceException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the pair_list is empty.
        if pair_list.is_empty:
            return SearchResult.empty()
        
        # --- Create the return target then, prime it with the first node's head.---#
        unique_nodes: List[Node] = [pair_list.couples[0].head]
        
        # --- Process each couple's unique tail. ---#
        for couple in pair_list.couples:
            if couple.tail not in unique_nodes:
                unique_nodes.append(couple.tail)
                
        # --- Send work product. ---#
        return SearchResult.success(unique_nodes)
    
    @LoggingLevelRouter.monitor
    def find_couples_by_node(self, node: Node, pair_list: PairList) -> SearchResult[List[Node]]:
        method = f"{self.__class__.__name__}.find_couples_by_node"
        
        matches = [
            couple for  couple in pair_list.couples if couple.head == node or couple.tail == node
        ]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(matches)