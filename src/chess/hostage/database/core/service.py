# src/chess/hostage/databse/coreservice_.py

"""
Module: chess.hostage.database.core.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.hostage import (
    AppendingHostageManifestDirectlyIntoItemsFailedException, CaptivityContextService, HostageManifest,
    HostageManifestDataListException, HostageManifestInsertionFailedException, HostageManifestService
)
from chess.system import DataService, InsertionResult, LoggingLevelRouter, id_emitter


class HostageManifestList(DataService[HostageManifest]):
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing HostageManifest objects and their lifecycles.
    3.  Ensure integrity of HostageManifest data stack
    4.  Stack data structure for HostageManifest objects with no guarantee of uniqueness.

    # PARENT:
        *   DataService[HostageManifest]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "HostageManifestList"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[HostageManifest] = List[HostageManifest],
            service: HostageManifestService = HostageManifestService(),
            context_service: CaptivityContextService = CaptivityContextService(),
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
        method = "HostageManifestService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def integrity_service(self) -> HostageManifestService:
        return cast(HostageManifestService, self.entity_service)
    
    @property
    def captivity_context_service(self) -> CaptivityContextService:
        return cast(CaptivityContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def insert_manifest(self, manifest: HostageManifest) -> InsertionResult[HostageManifest]:
        """
        # ACTION:
            1.  If the hostageManifest is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   hostageManifest (HostageManifest)
        # RETURNS:
            *   InsertionResult[HostageManifest] containing either:
                    - On failure: Exception.
                    - On success: HostageManifest in the payload.
        # RAISES:
            *   HostageManifestDataListException
        """
        method = "HostageManifestList.add_hostageManifest"
        
        # Handle the case that the hostageManifest is unsafe.
        validation = self.integrity_service.validator.validate(candidate=manifest)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageManifestDataListException(
                    message=f"ServiceId:{self.id}, {method}: {HostageManifestDataListException.ERROR_CODE}",
                    ex=HostageManifestInsertionFailedException(
                        message=f"{method}: {HostageManifestInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )

        # --- HostageManifest order is not required. Direct insertion into the dataset is simpler that a push. ---#
        self.items.append(manifest)
        
        # Handle the case that the hostageManifest was not appended to the dataset.
        if manifest not in self.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageManifestDataListException(
                    message=f"ServiceId:{self.id}, {method}: {HostageManifestDataListException.ERROR_CODE}",
                    ex=HostageManifestInsertionFailedException(
                        message=f"{method}: {HostageManifestInsertionFailedException.ERROR_CODE}",
                        ex=AppendingHostageManifestDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingHostageManifestDirectlyIntoItemsFailedException.ERROR_CODE}"
                        )
                    )
                )
            )
        # On success return the hostageManifest in the InsertionResult
        return InsertionResult.success(payload=manifest)
    
    
