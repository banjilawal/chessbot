# src/chess/catalog/lookup/lookup.py

"""
Module: chess.catalog.lookup.lookup
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from typing import List, Optional, cast

from chess.catalog import (
    Catalog, CatalogContext, CatalogContextBuilder, CatalogContextValidator,
    CatalogDesignationBoundsException, CatalogLookupException, CatalogLookupFailedException,
    CatalogNameBoundsException, CatalogQuotaBoundsException, CatalogRansomBoundsException, CatalogValidator
)
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from chess.system import EnumLookup, LoggingLevelRouter, SearchResult, id_emitter


class CatalogLookup(EnumLookup[CatalogContext]):
    """
    # ROLE: EnumLookup, Utility

    # RESPONSIBILITIES:
    1.  Lookup microservice API for mapping metadata values to Catalog configurations.
    2.  Encapsulates integrity assurance logic for Catalog lookup operations.
    3.  Provide mapping between Catalogs and the Ranks.

    # PARENT:
        *   EntityLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EnumLookup for inherited attributes.
    """
    SERVICE_NAME = "CatalogLookupService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.lookup_id,
            enum_validator: CatalogValidator = CatalogValidator(),
            context_builder: CatalogContextBuilder = CatalogContextBuilder(),
            context_validator: CatalogContextValidator = CatalogContextValidator(),
    ):
        super().__init__(
            id=id,
            name=name,
            enum_validator=enum_validator,
            context_builder=context_builder,
            context_validator=context_validator
        )
    
    @property
    def catalog_validator(self) -> CatalogValidator:
        """Return an CatalogValidator."""
        return cast(CatalogValidator, self.enum_validator)
    
    @property
    def catalog_context_builder(self) -> CatalogContextBuilder:
        """Return an CatalogContextBuilder."""
        return cast(CatalogContextBuilder, self.context_builder)
    
    @property
    def catalog_context_validator(self) -> CatalogContextValidator:
        """Return an CatalogContextValidator."""
        return cast(CatalogContextValidator, self.context_validator)
    
    @property
    def allowed_names(self) -> List[str]:
        """Returns a list of all permissible schema names in upper case."""
        return [catalog.name.upper() for catalog in Catalog]
    
    @property
    def allowed_designations(self) -> List[str]:
        """Returns a list of all permissible catalog designations in upper case."""
        return [entry.designation.upper() for entry in Catalog]
    
    @property
    def allowed_quotas(self) -> List[int]:
        """Returns a list of all the unique team_quotas in the catalog."""
        return [entry.quota for entry in Catalog]
    
    @property
    def allowed_ransoms(self) -> List[int]:
        """Returns a list of all the unique ransoms in the catalog."""
        return [entry.ransom for entry in Catalog]
    
    @classmethod
    def rank_from_catalog(cls, entry: Catalog) -> Optional[Rank]:
        """Get the Rank which the catalog entry builds."""
        if entry == Catalog.KING: return King()
        if entry == Catalog.PAWN: return Pawn()
        if entry == Catalog.KNIGHT: return Knight()
        if entry == Catalog.BISHOP: return Bishop()
        if entry == Catalog.ROOK: return Rook()
        if entry == Catalog.QUEEN: return Queen()
        return None
    
    @classmethod
    def catalog_from_rank(cls, rank: Rank) -> Optional[Catalog]:
        """Get the Catalog from its corresponding Rank."""
        if isinstance(rank, King): return Catalog.KING
        if isinstance(rank, Pawn): return Catalog.PAWN
        if isinstance(rank, Knight): return Catalog.KNIGHT
        if isinstance(rank, Bishop): return Catalog.BISHOP
        if isinstance(rank, Rook): return Catalog.ROOK
        if isinstance(rank, Queen): return Catalog.QUEEN
        return None
    
    @classmethod
    @LoggingLevelRouter.monitor
    def lookup(
            cls,
            context: CatalogContext,
            context_validator: CatalogContextValidator = CatalogContextValidator()
    ) -> SearchResult[List[Catalog]]:
        """
        # Action:
        1.  Certify the provided context with the class method's number_bounds_validator param.
        2.  If the context validation fails return the exception in a validation result. Otherwise, return
            the configuration entries which matched the context.

        # Parameters:
            *   context: CatalogContext
            *   context_validator: CatalogContextValidator

        # Returns:
        SearchResult[List[Catalog]] containing either:
            - On finding a match: List[Catalog] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   CatalogLookupFailedException
            *   CatalogLookupException
        """
        method = "CatalogLookup.find"
        try:
            # certify the context is safe.
            validation = context_validator.validate(candidate=context)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            # After context is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by name value.
            if context.name is not None:
                return cls._lookup_by_designation(designation=context.name)
            # Entry point into searching by designation value.
            if context.designation is not None:
                return cls._lookup_by_designation(designation=context.designation)
            # Entry point into searching by ransom value.
            if context.ransom is not None:
                return cls._lookup_by_ransom(ransom=context.ransom)
            # Entry point into searching by quota value.
            if context.quota is not None:
                return cls._lookup_by_quota(quota=context.quota)
            
            # Failsafe if any context cases was missed
            return SearchResult.failure(
                CatalogLookupFailedException(f"{method}: {CatalogLookupFailedException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a CatalogLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                CatalogLookupException(ex=ex, message=f"{method}: {CatalogLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_name(cls, name: str) -> SearchResult[List[Catalog]]:
        """
        # Action:
        1.  Get any Catalog which matches the target name.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Catalog]] containing either:
            - On finding a match: List[Catalog] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   CatalogDesignationBoundsException
            *   CatalogLookupFailedException
        """
        method = "CatalogLookup._lookup_by_name"
        try:
            matches = [catalog for catalog in Catalog if catalog.name.upper() == name.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no catalog has that designation.
            return SearchResult.failure(
                CatalogNameBoundsException(f"{method}: {CatalogNameBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a CatalogLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                CatalogLookupException(ex=ex, message=f"{method}: {CatalogLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_designation(cls, designation: str) -> SearchResult[List[Catalog]]:
        """
        # Action:
        1.  Get any Catalog which matches the target designation.

        # Parameters:
            *   designation (str)

        # Returns:
        SearchResult[List[Catalog]] containing either:
            - On finding a match: List[Catalog] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   CatalogDesignationBoundsException
            *   CatalogLookupFailedException
        """
        method = "CatalogLookup._lookup_by_designation"
        try:
            matches = [catalog for catalog in Catalog if catalog.designation.upper() == designation.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no catalog has that designation.
            return SearchResult.failure(
                CatalogDesignationBoundsException(f"{method}: {CatalogDesignationBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a CatalogLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                CatalogLookupException(ex=ex, message=f"{method}: {CatalogLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_quota(cls, quota: int) -> SearchResult[List[Catalog]]:
        """
        # Action:
        1.  Get anyCatalog which matches the ransom's name.

        # Parameters:
            *   quota (int)

        # Returns:
        SearchResult[List[Catalog]] containing either:
            - On finding a match: List[Catalog] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   CatalogRansomBoundsException
            *   CatalogLookupFailedException
        """
        method = "CatalogLookup._lookup_by_quota"
        try:
            matches = [catalog for catalog in Catalog if catalog.quota == quota]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no catalog has that ransom.
            return SearchResult.failure(
                CatalogQuotaBoundsException(f"{method}: {CatalogQuotaBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a CatalogLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                CatalogLookupException(ex=ex, message=f"{method}: {CatalogLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_ransom(cls, ransom: int) -> SearchResult[List[Catalog]]:
        """
        # Action:
        1.  Get any Catalog which matches the target quota.

        # Parameters:
            *   ransom (int)

        # Returns:
        SearchResult[List[Catalog]] containing either:
            - On finding a match: List[Catalog] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   CatalogQuotaBoundsException
            *   CatalogLookupFailedException
        """
        method = "CatalogLookup._lookup_by_ransom"
        try:
            matches = [catalog for catalog in Catalog if catalog.ransom == ransom]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no catalog has that quota.
            return SearchResult.failure(
                CatalogRansomBoundsException(f"{method}: {CatalogRansomBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a CatalogLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                CatalogLookupException(ex=ex, message=f"{method}: {CatalogLookupException.DEFAULT_MESSAGE}")
            )
