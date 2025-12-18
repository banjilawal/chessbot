# src/chess/catalog/lookup/context/builder/builder.py

"""
Module: chess.catalog.lookup.context.builder
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Optional

from chess.catalog import (
    CatalogContext, CatalogContextBuildFailedException, NoCatalogContextFlagException,
    TooManyCatalogContextFlagsException
)
from chess.system import BuildResult, Builder, IdentityService, LoggingLevelRouter, NumberValidator


class CatalogContextBuilder(Builder[CatalogContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce CatalogContext instances whose integrity is always guaranteed.
     2.  Manage construction of CatalogContext instances that can be used safely by the client.
     3.  Ensure params for CatalogContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
     None

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            quota: Optional[int] = None,
            ransom: Optional[int] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[CatalogContext]:
        """
        # Action:
            1.  Confirm that only one in the (designation, quota, ransom) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service or validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an CatalogContext and return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   quota (Optional[str])
            *   designation (Optional[str])
            *   ransom (Optional[GameRansom])

        These Parameters must be provided:
            *   number_validator (NumberValidator)
            *   identity_service (IdentityService)

        # Returns:
        BuildResult[CatalogContext] containing either:
            - On success: CatalogContext in the payload.
            - On failure: Exception.

        # Raises:
            *   NoCatalogContextFlagException
            *   TooManyCatalogContextFlagsException
            *   CatalogContextBuildFailedException
        """
        method = "CatalogContextBuilder.build"
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [designation, quota, ransom]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a BattleCatalog object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoCatalogContextFlagException(f"{method}: {NoCatalogContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one property-value pair is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyCatalogContextFlagsException(f"{method}: {TooManyCatalogContextFlagsException}")
                )
            # After the verifying the correct number of flags are set follow the appropriate BattleCatalog build flow.
            
            # designation flag enabled, build flow.
            if designation is not None:
                validation = identity_service.validate_name(candidate=designation)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_BattleCatalog_context in the BuildResult.
                return BuildResult.success(CatalogContext(designation=designation))
            
            # quota flag enabled, build flow.
            if quota is not None:
                validation = number_validator.validate(candidate=quota)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_BattleCatalog_context in the BuildResult.
                return BuildResult.success(CatalogContext(quota=quota))
            
            # GameRansom flag enabled, build flow.
            if ransom is not None:
                validation = number_validator.validate(candidate=ransom)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an GameRansom_BattleCatalog_context in the BuildResult.
                return BuildResult.success(CatalogContext(ransom=ransom))
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception in a
        # CatalogContextBuildFailedException then, send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                CatalogContextBuildFailedException(
                    ex=ex, message=f"{method}: {CatalogContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )