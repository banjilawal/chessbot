# src/microservice/stack/hostage/microservice.py

"""
Module: microservice.stack.hostage.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class HostageStackServiceStackService[Hostage]):
    """
    Role:Data Stack, SearchRouter Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing Hostage objects and their lifecycles.
    3.  Ensure integrity of Hostage data schema
    4.  Stack data structure for Hostage objects with no guarantee of uniqueness.

    Super Class:
        *   StackService[Hostage]

    Provides:


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
            context_service: HostageQueryService = HostageQueryService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   bag (List[Team])
            *   service (TeamService)
            *   context_service (TeamQueryService)
        # RETURNS:
            None
        Raises:
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
    def captivity_context_service(self) -> HostageQueryService:
        return cast(HostageQueryService, self.context_service)
    
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
        Raises:
            *   HostageDataListException
        """
        method = "HostageList.add_hostage"
        
        # Handle the case that, the hostage is unsafe.
        validation = self.service.validator.validate(candidate=manifest)
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

        # --- Hostage order is not required. Direct insertion into the collider_candidates is simpler that a push. ---#
        self.items.append(manifest)
        
        # Handle the case that, the hostage was not appended to the collider_candidates.
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
    
    
