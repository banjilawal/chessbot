# src/logic/pair/stack/stack.py

"""
Module: logic.pair.stack.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional

from logic.system import (
     SearchResult, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, IdFactory
)
from logic.pair import (
    PoppingEmptyPairStackException, Pair, PairContext, PairService, PairStackException, PairContextService,
    PoppingPairException, PushingPairException, PairStackFullException, PairStackState, PairStackUtil,
)
from logic.system.collection.stack.stack import T


class PairStack(StackService[Pair]):
    """
    Role:Data Stack, SearchRouter IntegrityMicroservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing Pair objects and their lifecycles.
    3.  Ensure integrity of Pair data stack
    4.  Stack data structure for Pair objects with no guarantee of uniqueness.
    
    Super Class:
        *   StackService[Pair]

    Provides:

    
    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME: str = "PairStack"
    
    _stack: List[Pair]
    _service: PairService
    _context_service: PairContextService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            service: PairService = PairService(),
            id: int = IdFactory.next_id(class_name="Pair"),
            context_service: PairContextService = PairContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   service (PairService)
            *   context_service (PairContextService)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "PairService.__init__"
        super().__init__(id=id, name=name,)
        self.stack = []
        
        self._service = service
        self._context_service = context_service
        
        self._state = PairStackState.EMPTY

    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def current_pair(self) -> Optional[Pair]:
        return self._stack[-1] if self._stack else None
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def current_item(self) -> Optional[Pair]:
        return self._stack[-1] if self._stack else None
        
    @property
    def integrity_service(self) -> PairService:
        return self._service
    
    @property
    def context_service(self) -> PairContextService:
        return self._context_service
    
    @LoggingLevelRouter.monitor
    def push(self, item: Pair) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the occupant is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   occupant (Pair)
        # RETURNS:
            *   InsertionResult[Pair] containing either:
                    - On failure: Exception.
                    - On success: Pair in the payload.
        Raises:
            *   PairStackException
        """
        method = "PairStack.push"
        
        # Handle the case that, the list is full.
        if self.is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PairStackException(
                    msg=f"ServiceId:{self.id}, {method}: {PairStackException.ERR_CODE}",
                    ex=PushingPairException(
                        msg=f"{method}: {PushingPairException.ERR_CODE}",
                        ex=PairStackFullException(f"{method}: {PairStackFullException.ERR_CODE}")
                    )
                )
            )
        # --- Handoff validation, id, designation or opening_square collision detection. ---#
        collision_report = self.integrity_service.collision_detector.query(
            target=item,
            collider_candidates=self._stack,
        )
        # Handle the case that, the collision analysis is not completed.
        if collision_report.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PairStackException(
                    msg=f"ServiceId:{self.id}, {method}: {PairStackException.ERR_CODE}",
                    ex=PushingPairException(
                        msg=f"{method}: {PushingPairException.ERR_CODE}",
                        ex=collision_report.exception
                    )
                )
            )
        # --- Find out how many openings the rank has. ---#
        openings_count_result = self.utils.rank_quota_analyzer.count_openings_for_rank(
            rank=item.rank,
            pair_stack=self
        )
        # Handle the case that, the analyzer doesn't give a count of open slots.
        if openings_count_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PairStackException(
                    msg=f"ServiceId:{self.id}, {method}: {PairStackException.ERR_CODE}",
                    ex=PushingPairException(
                        msg=f"{method}: {PushingPairException.ERR_CODE}",
                        ex=openings_count_result.exception
                    )
                )
            )
        # --- Capacity, collision and opening check are completed. Push the pair onto the stack ---#
        self._stack.append(item)
        
        # --- Perform cleanup and integrity maintenance tasks. ---#
        if self.size == self.capacity:
            self._state = PairStackState.FILLED_READY_TO_DEPLOY
            
        # --- Send the success result to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Pair]:
        """
        # ACTION:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                pair at the top of the stack and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Pair] containing either:
                    - On failure: Exception.
                    - On success: Pair in the payload.
        Raises:
            *   PairStackException
            *   PoppingEmptyPairStackException
        """
        method = "PairStack.pop"
        
        # Handle the case that, there are no pairs in the stack.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                PairStackException(
                    msg=f"ServiceId:{self.id}, {method}: {PairStackException.ERR_CODE}",
                    ex=PoppingPairException(
                        msg=f"{method}: {PoppingPairException.ERR_CODE}",
                        ex=PoppingEmptyPairStackException(
                            f"{method}: {PoppingEmptyPairStackException.MSG}"
                        )
                    )
                )
            )
        # --- Pop the non-empty pair stack. ---#
        pair = self._stack.pop(-1)
        # --- Perform cleanup and integrity maintenance tasks. ---#
        if self.is_empty:
            self._state = PairStackState.EMPTY
            
        # --- Send the success result to the caller. ---#
        return DeletionResult.success(pair)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Pair]:
        """
        # ACTION:
            1.  If the id is not certified safe send an exception in the DeletionResult.
            2.  Create a temp variable for storing a pair before it's deleted.
            3.  Iterate through the pairs.
                    *   If a pair's id matches the target record the pair in a temp variable before deleting
                        it from the list.
            4.  After the loop is finishes, if the temp variable is not None send it in the deletion success result.
                Else, send the nothing to delete result instead.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   DeletionResult[Pair]
        Raises:
            *   PairStackException
            *   PoppingPairException
            *   PoppingEmptyPairStackException
        """
        method = "PairStack.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                PairStackException(
                    msg=f"StackId:{self.id}, {method}: {PairStackException.ERR_CODE}",
                    ex=PoppingPairException(
                        msg=f"{method}: {PoppingPairException.ERR_CODE}",
                        ex=PoppingEmptyPairStackException(
                            f"{method}: {PoppingEmptyPairStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                PairStackException(
                    msg=f"StackId:{self.id}, {method}: {PairStackException.ERR_CODE}",
                    ex=PoppingPairException(
                        msg=f"{method}: {PoppingPairException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for pair in self._stack:
            if pair.id == id:
                # Record a hit before pulling it from the stack.
                target = pair
                self._stack.remove(pair)
        # --- Perform cleanup and integrity maintenance tasks after the purging loop finishes. ---#
        if self.is_empty:
            self._state = PairStackState.EMPTY
        # --- Handle the possible return cases. ---#
        
        # At least one pair was removed.
        if target is not None:
            return DeletionResult.success(payload=target)
        # Default case: no pairs were removed.
        return DeletionResult.nothing_to_delete()
    
    @LoggingLevelRouter.monitor
    def query(self, context: PairContext) -> SearchResult[List[Pair]]:
        """
        # ACTION:
            1.  Pass the query param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a PairStackException which is
                sent inside a SearchResult.
            3.  If the search completes successfully return the result directly because its a SearchResult instance.
        # PARAMETERS:
            *   query (PairContext)
        # RETURN:
            *   SearchResult[List[Pair]] containing either:
                    - On failure: An exception.
                    - On success: List[Pair].
                    - On Empty: payload null, exception null.
        Raises:
            *   PairStackException
        """
        method = "PairStack.query"
        
        # --- Handoff the search responsibility to _context_service. ---#
        query_result = self._context_service.finder.route(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                PairStackException(
                    msg=f"ServiceID:{self.id} {method}: {PairStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result