# src/logic/hostage/databse/coreservice_.py

"""
Module: logic.hostage.database.core.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from logic.hostage import (
    AppendingHostageDirectlyIntoItemsFailedException, CaptivityContextService, Hostage,
    HostageDataListException, HostageInsertionException, HostageService
)
from logic.system import StackService, InsertionResult, LoggingLevelRouter, id_emitter


class HostageList(StackService[Hostage]):
    """
    # ROLE: Data Stack, SearchWorker IntegrityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Hostage objects and their lifecycles.
    3.  Ensure integrity of Hostage data stack
    4.  Stack data structure for Hostage objects with no guarantee of uniqueness.

    # PARENT:
        *   StackService[Hostage]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "HostageList"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Hostage] = List[Hostage],
            service: HostageService = HostageService(),
            context_service: CaptivityContextService = CaptivityContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   bag (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "HostageService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def integrity_service(self) -> HostageService:
        return cast(HostageService, self.entity_service)
    
    @property
    def captivity_context_service(self) -> CaptivityContextService:
        return cast(CaptivityContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def insert(self, manifest: Hostage) -> InsertionResult[Hostage]:
        """
        # ACTION:
            1.  If the hostage is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   hostage (Hostage)
        # RETURNS:
            *   InsertionResult[Hostage] containing either:
                    - On failure: Exception.
                    - On success: Hostage in the payload.
        # RAISES:
            *   HostageDataListException
        """
        method = "HostageList.add_hostage"
        
        # Handle the case that, the hostage is unsafe.
        validation = self.integrity_service.validator.validate(candidate=manifest)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDataListException(
                    msg=f"ServiceId:{self.id}, {method}: {HostageDataListException.ERR_CODE}",
                    ex=HostageInsertionException(
                        msg=f"{method}: {HostageInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )

        # --- Hostage order is not required. Direct insertion into the dataset is simpler that a push. ---#
        self.items.append(manifest)
        
        # Handle the case that, the hostage was not appended to the dataset.
        if manifest not in self.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                HostageDataListException(
                    msg=f"ServiceId:{self.id}, {method}: {HostageDataListException.ERR_CODE}",
                    ex=HostageInsertionException(
                        msg=f"{method}: {HostageInsertionException.ERR_CODE}",
                        ex=AppendingHostageDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingHostageDirectlyIntoItemsFailedException.ERR_CODE}"
                        )
                    )
                )
            )
        # On success return the hostage in the InsertionResult
        return InsertionResult.success(payload=manifest)
    
    
