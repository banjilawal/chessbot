# src/chess/persona/lookup/lookup.py

"""
Module: chess.persona.lookup.lookup
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from typing import List

from chess.persona import (
    
    Persona, PersonaSuperKey, PersonaSuperKeyValidator
)
from chess.persona.key.lookup.exception.wrapper import PersonaLookupFailedException

from chess.system import ForwardLookup, LoggingLevelRouter, SearchResult, id_emitter


class PersonaLookup(ForwardLookup[PersonaSuperKey]):
    """
    # ROLE: Forward Lookups

    # RESPONSIBILITIES:
    1.  Run forward lookups on the Persona hashtable to find a Team's play_directive_metadata for a game.
    2.  Indicate there is no play_directive for a given key-value pair by returning an exception to the caller.
    3.  Verifies correctness of key-value key before running the forward lookup.

    # PARENT:
        *   ForwardLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    def query(
            cls,
            super_key: PersonaSuperKey,
            super_key_validator: PersonaSuperKeyValidator = PersonaSuperKeyValidator()
    ) -> SearchResult[List[Persona]]:
        """
        # Action:
            1.  If super_key fails validation send the exception chain in the SearchResult. Else, route to the
                search method by the attribute portion of the SuperKey.
            2.  If the value portion of the SuperKey is not in the permitted attribute values send the exception
                chain in the SearchResult. Else, send Personas whose targeted attribute values match.
        # Parameters:
            *   key: SchemaSuperKey
            *   key_validator: SchemaSuperKeyValidator
        # Returns:
            *   SearchResult[List[Schema]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Schema] in the payload.
                    - On no matches found: Exception null, payload null
        # Raises:
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup.query"
        
        # Handle the case that the SuperKey fails validation.
        validation = super_key_validator.validate(candidate=super_key)
        if validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                PersonaLookupFailedException(
                    message=f"{method}: {PersonaLookupFailedException.ERROR_CODE}",
                    ex=validation.exception
                )
            )
        # After verification use the hash key to route to the appropriate lookup method.
        
        # Entry point into forward lookups by name.
        if super_key.name is not None:
            return cls._by_name(designation=super_key.name)
        # Entry point into forward lookups by designation.
        if super_key.designation is not None:
            return cls._by_designation(designation=super_key.designation)
        # Entry point into forward lookups by ranson.
        if super_key.ransom is not None:
            return cls._by_ransom(ransom=super_key.ransom)
        # Entry point into forward lookups by name.
        if super_key.quota is not None:
            return cls._by_quota(quota=super_key.quota)
        
        # For other entry points return the exception chain.
        return SearchResult.failure(
            PersonaLookupFailedException(
                message=f"{method}: {PersonaLookupFailedException.ERROR_CODE}",
                ex=
            )
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
