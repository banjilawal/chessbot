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
from logic.pair import PairList, PairListBuilder, PairListValidator
from logic.system import IdFactory, IntegrityService, LoggingLevelRouter, SearchResult


class PairListService(IntegrityService[PairList]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing PairList microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for PairList state by providing
        single entry and exit points to PairList lifecycle.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "PairListService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: PairListBuilder = PairListBuilder(),
            validator: PairListValidator = PairListValidator(),
            id: int = IdFactory.next_id(class_name="PairListService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: PairListBuilder
            validator: PairListValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> PairListBuilder:
        return cast(PairListBuilder, self.entity_builder)
    
    @property
    def validator(self) -> PairListValidator:
        return cast(PairListValidator, self.entity_validator)

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
        # Put the head of first couple in the lis
        nodes: List[Node] = []
        
        # Handle the case that pair_list is empty.
        if pair_list.is_empty:
            return SearchResult.empty()
        # prime unique_nodes list
        nodes.append(pair_list.couples[0].head)
        
        # Process the rest of the couples.
        for couple in pair_list.couples:
            if couple.tail not in nodes:
                nodes.append(couple.tail)
        if len(nodes) == 0:
            return SearchResult.empty()
        return SearchResult.success(nodes)
    
    @LoggingLevelRouter.monitor
    def find_couples_by_node(self, node: Node, pair_list: PairList) -> SearchResult[List[Node]]:
        method = f"{self.__class__.__name__}.find_couples_by_node"
        
        matches = [
            couple for  couple in pair_list.couples if couple.head == node or couple.tail == node
        ]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(matches)