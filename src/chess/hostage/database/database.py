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
    AddingDuplicateHostageManifestException, CaptivityContext, CaptivityContextService, HostageManifest,
    HostageManifestList, HostageManifestService, UniqueHostageManifestInsertionException,
    UniqueHostageManifestSearchException
)
from chess.system import InsertionResult, LoggingLevelRouter, SearchResult, Database, id_emitter


class HostageDatabase(Database[HostageManifest]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by HostageManifestList are unique.
    2.  Guarantee consistency of records in HostageManifestList.

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
    _database_core: HostageManifestList
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: HostageManifestList = HostageManifestList(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (HostageManifestList)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._stack_service = data_service
    
    @property
    def integrity_service(self) -> HostageManifestService:
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
    def add_unique_manifest(self, manifest: HostageManifest) -> InsertionResult[HostageManifest]:
        """
        # ACTION:
            1.  If the hostageManifest fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the hostageManifest either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _hostageManifest_database_core.insert_hostageManifest fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   hostageManifest (HostageManifest)
        # RETURN:
            *   InsertionResult[HostageManifest] containing either:
                    - On failure: An exception.
                    - On success: HostageManifest in payload.
        # RAISES:
            *   HostageDatabase
            *   UniqueHostageManifestInsertionException
            *   HostageDatabase
        """
        method = "HostageDatabase.add_unique_hostageManifest"
        
        # --- To assure uniqueness the member_service has to conduct a search. The hostageManifest should be validated first. ---#
        
        # Handle the case that the hostageManifest is not certified safe.
        validation = self.integrity_service.validator.validate(candidate=manifest)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {HostageDatabaseException.ERROR_CODE}",
                    ex=UniqueHostageManifestInsertionException(
                        message=f"{method}: {UniqueHostageManifestInsertionException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Check if the hostageManifest is already in the dataset before adding it. ---#
        search_result = self.search_hostageManifests(context=CaptivityContext(id=manifest.id))
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {HostageDatabaseException.ERROR_CODE}",
                    ex=UniqueHostageManifestInsertionException(
                        message=f"{method}: {UniqueHostageManifestInsertionException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that the hostageManifest is already in the dataset.
        if search_result.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabaseDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {HostageDatabase.ERROR_CODE}",
                    ex=UniqueHostageManifestInsertionException(
                        message=f"{method}: {UniqueHostageManifestInsertionException.ERROR_CODE}",
                        ex=AddingDuplicateHostageManifestException(
                            f"{method}: {AddingDuplicateHostageManifestException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Use _database_core.insert_manifest because order does not matter for the manifest access. ---#
        insertion_result = self._database_core.insert_manifest(manifest=manifest)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDatabase(
                    message=(
                        f"ServiceId:{self.id}, {method}: {HostageDatabase.ERROR_CODE}"
                    ),
                    ex=UniqueHostageManifestInsertionException(
                        message=f"{method}: {UniqueHostageManifestInsertionException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_manifests(self, context: CaptivityContext) -> SearchResult[List[HostageManifest]]:
        """
        # ACTION:
            1.  Get the result of calling _hostageManifest_database_core.delete_hostageManifest_by_id for method.
                If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[HostageManifest] containing either:
                    - On failure: An exception.
                    - On success: HostageManifest in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   HostageDatabase
            *   ExhaustiveHostageManifestDeletionException
        """
        method = "HostageDatabase.searchnanifests"
        
        # --- Handoff the search responsibility to _hostageManifest_database_core. ---#
        search_result = self._database_core.context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageDatabase(
                    message=f"ServiceID:{self.id} {method}: {HostageDatabase.ERROR_CODE}",
                    ex=UniqueHostageManifestSearchException(
                        message=f"{method}: {UniqueHostageManifestSearchException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result