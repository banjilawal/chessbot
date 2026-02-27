# src/chess/hostage/database/service.py

"""
Module: chess.hostage.database.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.hostage import (
    AddingDuplicateHostageException, CaptivityContext, CaptivityContextService, Hostage,
    HostageList, HostageService, UniqueHostageInsertionException,
    UniqueHostageSearchException
)
from chess.system import InsertionResult, LoggingLevelRouter, SearchResult, Database, id_emitter


class HostageDatabase(Database[Hostage]):
    """
    # ROLE: Unique Data Stack, Search AbstractService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by HostageList are unique.
    2.  Guarantee consistency of records in HostageList.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "HostageDatabase"
    _database_core: HostageList
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: HostageList = HostageList(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (HostageList)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._stack_service = data_service
    
    @property
    def integrity_service(self) -> HostageService:
        return self._database_core.integrity_service
    
    @property
    def context_service(self) -> CaptivityContextService:
        return self._database_core.context_service
    
    @property
    def size(self) -> int:
        return self._database_core.size
    
    @property
    def is_empty(self) -> bool:
        return self._database_core.is_empty
    
    @LoggingLevelRouter.monitor
    def add_unique(self, manifest: Hostage) -> InsertionResult[Hostage]:
        """
        # ACTION:
            1.  If the hostage fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the hostage either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _hostage_database_core.insert_hostage fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   hostage (Hostage)
        # RETURN:
            *   InsertionResult[Hostage] containing either:
                    - On failure: An exception.
                    - On success: Hostage in payload.
        # RAISES:
            *   HostageDatabase
            *   UniqueHostageInsertionException
            *   HostageDatabase
        """
        method = "HostageDatabase.add_unique_hostage"
        
        # --- To assure uniqueness the member_service has to conduct a search. The hostage should be validated first. ---#
        
        # Handle the case that, the hostage is not certified safe.
        validation = self.integrity_service.validator.validate(candidate=manifest)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabaseException(
                    msg=f"ServiceId:{self.id}, {method}: {HostageDatabaseException.ERR_CODE}",
                    ex=UniqueHostageInsertionException(
                        msg=f"{method}: {UniqueHostageInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Check if the hostage is already in the dataset before adding it. ---#
        search_result = self.search_hostages(context=CaptivityContext(id=manifest.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabaseException(
                    msg=f"ServiceId:{self.id}, {method}: {HostageDatabaseException.ERR_CODE}",
                    ex=UniqueHostageInsertionException(
                        msg=f"{method}: {UniqueHostageInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the hostage is already in the dataset.
        if search_result.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabaseDatabaseException(
                    msg=f"ServiceId:{self.id}, {method}: {HostageDatabase.ERR_CODE}",
                    ex=UniqueHostageInsertionException(
                        msg=f"{method}: {UniqueHostageInsertionException.ERR_CODE}",
                        ex=AddingDuplicateHostageException(
                            f"{method}: {AddingDuplicateHostageException.MSG}"
                        )
                    )
                )
            )
        # --- Use _database_core.insert because order does not matter for the manifest access. ---#
        insertion_result = self._database_core.insert(manifest=manifest)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabase(
                    msg=(
                        f"ServiceId:{self.id}, {method}: {HostageDatabase.ERR_CODE}"
                    ),
                    ex=UniqueHostageInsertionException(
                        msg=f"{method}: {UniqueHostageInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def searchs(self, context: CaptivityContext) -> SearchResult[List[Hostage]]:
        """
        # ACTION:
            1.  Get the result of calling _hostage_database_core.delete_hostage_by_id for method.
                If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Hostage] containing either:
                    - On failure: An exception.
                    - On success: Hostage in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   HostageDatabase
            *   ExhaustiveHostageDeletionException
        """
        method = "HostageDatabase.searchnanifests"
        
        # --- Handoff the search responsibility to _hostage_database_core. ---#
        search_result = self._database_core.context_service.finder.find(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageDatabase(
                    msg=f"ServiceID:{self.id} {method}: {HostageDatabase.ERR_CODE}",
                    ex=UniqueHostageSearchException(
                        msg=f"{method}: {UniqueHostageSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result