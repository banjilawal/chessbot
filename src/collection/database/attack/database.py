# src/collection/database/attack/database.py

"""
Module: database.attack.database
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection.database import Database


class AttackDatabase(Database[Attack]):
    """
    Role:
        _   Frontend
        -  Interface
        -  Data Protection

    Responsibilities:
        1.  Encapsulates StackService.
        2.  Protects data from direct access.

    Attributes:
        id: int
        size: int
        name: str
        iterator: iter
        is_empty: bool
        current_item: Optional[T]
        integrity_service: Microservice[T]

    Provides:
        -  iterator() ->: iter
        -  insert(item: T) -> InsertionResult:
        -  delete_by_id(id: int) -> DeletionResult[T]:
        -  search(context: Context[T]) -> SearchResult[List[T]]

    Role:Unique Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Ensure all bag in managed by AttackStackService are unique.
    2.  Guarantee consistency of records in AttackStackService.

    Super Class:
        *   Database

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "AttackDatabase"
    _attack_database_core: AttackStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: AttackStackService = AttackStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   member_service (AttackStackService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._attack_stack_service = data_service
    
    @property
    def microservice(self) -> AttackService:
        return self._attack_database_core.attack_service
    
    @property
    def context_service(self) -> AttackQueryService:
        return self._attack_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._attack_database_core.rule_count
    
    @property
    def is_empty(self) -> bool:
        return self._attack_database_core.no_recurrences_exist
    
    @LoggingLevelRouter.monitor
    def add_unique_attack(self, attack: Attack) -> InsertionResult[Attack]:
        """
        # ACTION:
            1.  If the attack fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the attack either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _attack_database_core.insert_attack fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   attack (Attack)
        # RETURN:
            *   InsertionResult[Attack] containing either:
                    - On failure: An exception.
                    - On success: Attack in payload.
        Raises:
            *   AttackDatabaseException
            *   UniqueAttackInsertionException
            *   AttackDatabaseException
        """
        method = "AttackDatabase.add_unique_attack"
        
        # --- To assure uniqueness the member_service has to conduct a search. The attack should be validated first. ---#
        
        # Handle the case that, the attackis not safe.
        validation = self.microservice.execute.execute(candidate=attack)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueAttackDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueAttackDataServiceException.ERR_CODE}",
                    ex=UniqueAttackInsertionException(
                        msg=f"{method}: {UniqueAttackInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if the attack is already in the collider_candidates before adding it. ---#
        search_result = self.search_attacks(context=AttackContext(id=attack.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueAttackDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueAttackDataServiceException.ERR_CODE}",
                    ex=UniqueAttackInsertionException(
                        msg=f"{method}: {UniqueAttackInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the attack is already in the collider_candidates.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueAttackDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueAttackDataServiceException.ERR_CODE}",
                    ex=UniqueAttackInsertionException(
                        msg=f"{method}: {UniqueAttackInsertionException.ERR_CODE}",
                        ex=AddingDuplicateAttackException(f"{method}: {AddingDuplicateAttackException.MSG}")
                    )
                )
            )
        # --- Use _attack_database_core.insert_attack because order does not matter for the attack access. ---#
        insertion_result = self._attack_database_core.insert_attack(attack=attack)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueAttackDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueAttackDataServiceException.ERR_CODE}",
                    ex=UniqueAttackInsertionException(
                        msg=f"{method}: {UniqueAttackInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_attacks(self, context: AttackContext) -> SearchResult[List[Attack]]:
        """
        # ACTION:
            1.  Get the result of calling _attack_database_core.delete_attack_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Attack] containing either:
                    - On failure: An exception.
                    - On success: Attack in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   AttackDatabaseException
            *   ExhaustiveAttackDeletionException
        """
        method = "AttackDatabase.search_attacks"
        
        # --- Handoff the search responsibility to _attack_database_core. ---#
        search_result = self._attack_database_core.attack_context_service.finder.route(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                UniqueAttackDataServiceException(
                    msg=f"ServiceID:{self.id} {method}: {UniqueAttackDataServiceException.ERR_CODE}",
                    ex=UniqueAttackSearchException(
                        msg=f"{method}: {UniqueAttackSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result