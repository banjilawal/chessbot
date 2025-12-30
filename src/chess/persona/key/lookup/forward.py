# src/chess/persona/lookup/lookup.py

"""
Module: chess.persona.lookup.lookup
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from typing import List, Optional, cast

from chess.persona import (
    
    PersonaSuperKey
)
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from chess.system import ForwardLookup, LoggingLevelRouter, SearchResult, id_emitter


class PersonaLookup(ForwardLookup[PersonaSuperKey]):
    """
    # ROLE: Forward Lookups, Mapping 

    # RESPONSIBILITIES:
    1.  Lookup microservice API for mapping metadata values to Persona configurations.
    2.  Encapsulates integrity assurance logic for Persona lookup operations.
    3.  Provide mapping between Personas and the Ranks.

    # PARENT:
        *   EntityLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ForwardLookup for inherited attributes.
    """
    SERVICE_NAME = "PersonaLookupService"
    
    def lookup(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.lookup_id,
            enum_validator: PersonaValidator = PersonaValidator(),
            context_builder: PersonaSuperKeyBuilder = PersonaSuperKeyBuilder(),
            context_validator: PersonaSuperKeyValidator = PersonaSuperKeyValidator(),
    ):
        super().lookup(
            id=id,
            name=name,
            enum_validator=enum_validator,
            context_builder=context_builder,
            context_validator=context_validator
        )
    
    @property
    def persona_validator(self) -> PersonaValidator:
        """Return an PersonaValidator."""
        return cast(PersonaValidator, self.enum_validator)
    
    @property
    def persona_context_builder(self) -> PersonaSuperKeyBuilder:
        """Return an PersonaSuperKeyBuilder."""
        return cast(PersonaSuperKeyBuilder, self.context_builder)
    
    @property
    def persona_context_validator(self) -> PersonaSuperKeyValidator:
        """Return an PersonaSuperKeyValidator."""
        return cast(PersonaSuperKeyValidator, self.context_validator)
    
    @property
    def allowed_names(self) -> List[str]:
        """Returns a list of all permissible schema names in upper case."""
        return [persona.name.upper() for persona in Persona]
    
    @property
    def allowed_designations(self) -> List[str]:
        """Returns a list of all permissible persona designations in upper case."""
        return [entry.designation.upper() for entry in Persona]
    
    @property
    def allowed_quotas(self) -> List[int]:
        """Returns a list of all the unique team_quotas in the persona."""
        return [entry.quota for entry in Persona]
    
    @property
    def allowed_ransoms(self) -> List[int]:
        """Returns a list of all the unique ransoms in the persona."""
        return [entry.ransom for entry in Persona]
    
    @classmethod
    def rank_from_persona(cls, entry: Persona) -> Optional[Rank]:
        """Get the Rank which the persona entry builds."""
        if entry == Persona.KING: return King()
        if entry == Persona.PAWN: return Pawn()
        if entry == Persona.KNIGHT: return Knight()
        if entry == Persona.BISHOP: return Bishop()
        if entry == Persona.ROOK: return Rook()
        if entry == Persona.QUEEN: return Queen()
        return None
    
    @classmethod
    def persona_from_rank(cls, rank: Rank) -> Optional[Persona]:
        """Get the Persona from its corresponding Rank."""
        if isinstance(rank, King): return Persona.KING
        if isinstance(rank, Pawn): return Persona.PAWN
        if isinstance(rank, Knight): return Persona.KNIGHT
        if isinstance(rank, Bishop): return Persona.BISHOP
        if isinstance(rank, Rook): return Persona.ROOK
        if isinstance(rank, Queen): return Persona.QUEEN
        return None
    
    @classmethod
    @LoggingLevelRouter.monitor
    def lookup(
            cls,
            context: PersonaSuperKey,
            context_validator: PersonaSuperKeyValidator = PersonaSuperKeyValidator()
    ) -> SearchResult[List[Persona]]:
        """
        # Action:
        1.  Certify the provided map with the class method's validator param.
        2.  If the map validation fails return the exception in a validation result. Otherwise, return
            the configuration entries which matched the map.

        # Parameters:
            *   map: PersonaSuperKey
            *   context_validator: PersonaSuperKeyValidator

        # Returns:
        SearchResult[List[Persona]] containing either:
            - On finding a match: List[Persona] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   PersonaLookupException
            *   PersonaLookupException
        """
        method = "PersonaLookup.find"
        try:
            # certify the map is safe.
            validation = context_validator.validate(candidate=context)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            # After map is verified select the search method based on the which flag is enabled.
            
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
            
            # Failsafe if any map cases was missed
            return SearchResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a PersonaLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                PersonaLookupException(ex=ex, message=f"{method}: {PersonaLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_name(cls, name: str) -> SearchResult[List[Persona]]:
        """
        # Action:
        1.  Get any Persona which matches the target name.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Persona]] containing either:
            - On finding a match: List[Persona] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   PersonaDesignationBoundsException
            *   PersonaLookupException
        """
        method = "PersonaLookup._lookup_by_name"
        try:
            matches = [persona for persona in Persona if persona.name.upper() == name.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no persona has that designation.
            return SearchResult.failure(
                PersonaNameBoundsException(f"{method}: {PersonaNameBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a PersonaLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                PersonaLookupException(ex=ex, message=f"{method}: {PersonaLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_designation(cls, designation: str) -> SearchResult[List[Persona]]:
        """
        # Action:
        1.  Get any Persona which matches the target designation.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Persona]] containing either:
            - On finding a match: List[Persona] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   PersonaDesignationBoundsException
            *   PersonaLookupException
        """
        method = "PersonaLookup._lookup_by_designation"
        try:
            matches = [persona for persona in Persona if persona.designation.upper() == designation.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no persona has that designation.
            return SearchResult.failure(
                PersonaDesignationBoundsException(f"{method}: {PersonaDesignationBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a PersonaLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                PersonaLookupException(ex=ex, message=f"{method}: {PersonaLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_quota(cls, quota: int) -> SearchResult[List[Persona]]:
        """
        # Action:
        1.  Get anyPersona which matches the ransom's name.

        # Parameters:
            *   quota (int)

        # Returns:
        SearchResult[List[Persona]] containing either:
            - On finding a match: List[Persona] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   PersonaRansomBoundsException
            *   PersonaLookupException
        """
        method = "PersonaLookup._lookup_by_quota"
        try:
            matches = [persona for persona in Persona if persona.quota == quota]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no persona has that ransom.
            return SearchResult.failure(
                PersonaQuotaBoundsException(f"{method}: {PersonaQuotaBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a PersonaLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                PersonaLookupException(ex=ex, message=f"{method}: {PersonaLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_ransom(cls, ransom: int) -> SearchResult[List[Persona]]:
        """
        # Action:
        1.  Get any Persona which matches the target quota.

        # Parameters:
            *   ransom (int)

        # Returns:
        SearchResult[List[Persona]] containing either:
            - On finding a match: List[Persona] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   PersonaQuotaBoundsException
            *   PersonaLookupException
        """
        method = "PersonaLookup._lookup_by_ransom"
        try:
            matches = [persona for persona in Persona if persona.ransom == ransom]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no persona has that quota.
            return SearchResult.failure(
                PersonaRansomBoundsException(f"{method}: {PersonaRansomBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a PersonaLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                PersonaLookupException(ex=ex, message=f"{method}: {PersonaLookupException.DEFAULT_MESSAGE}")
            )
