# src/chess/persona/key/lookup/lookup.py

"""
Module: chess.persona.key.lookup.lookup
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from typing import List

from chess.persona import (
    
    Persona, PersonaDesignationBoundsException, PersonaLookupRouteException, PersonaNameBoundsException,
    PersonaQuotaBoundsException, PersonaRansomBoundsException, PersonaSuperKey, PersonaSuperKeyValidator
)
from chess.persona.key.lookup.exception.wrapper import PersonaLookupFailedException

from chess.system import ForwardLookup, LoggingLevelRouter, SearchResult, id_emitter


class PersonaLookup(ForwardLookup[PersonaSuperKey]):
    """
    # ROLE: Forward Lookups

    # RESPONSIBILITIES:
    1.  Run forward lookups on the Persona hashtable to find a Rank's metadata.
    2.  Indicate there is no metadata for a given key-value pair by returning an exception to the caller.
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
        # ACTION:
            1.  If super_key fails validation send the exception chain in the SearchResult. Else, route to the
                search method by the attribute portion of the SuperKey.
            2.  If the value portion of the SuperKey is not in the permitted attribute values send the exception
                chain in the SearchResult. Else, send Personas whose targeted attribute values match.
        # PARAMETERS:
            *   key: PersonaSuperKey
            *   key_validator: PersonaSuperKeyValidator
        # RETURNS:
            *   SearchResult[List[Persona]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Persona] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *  PersonaLookupFailedException
        """
        method = "PersonaLookup.query"
        
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
        # Entry point into forward lookups by ransom.
        if super_key.ransom is not None:
            return cls._by_ransom(ransom=super_key.ransom)
        # Entry point into forward lookups by name.
        if super_key.quota is not None:
            return cls._by_quota(quota=super_key.quota)
        
        # For other entry points return the exception chain.
        return SearchResult.failure(
            PersonaLookupFailedException(
                message=f"{method}: {PersonaLookupFailedException.ERROR_CODE}",
                ex=PersonaLookupRouteException(f"{method}: {PersonaLookupRouteException.DEFAULT_MESSAGE}")
            )
        )

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_name(cls, name: str) -> SearchResult[List[Persona]]:
        """
        # ACTION:
            1.  Get any Persona entry whose name matches the target value.
        # PARAMETERS:
            *   name (str)
        # RETURNS:
            *   SearchResult[List[Persona]] containing either:
                    - On error: Exception
                    - On finding a match: List[Persona] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *  PersonaNameBoundsException
            *  PersonaLookupFailedException
        """
        method = "PersonaLookup._by_name"
        
        matches = [entry for entry in Persona if entry.name.upper() == name.upper()]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        
        # The default path is a failure.
        return SearchResult.failure(
           PersonaLookupFailedException(
                message=f"{method}: {PersonaLookupFailedException.ERROR_CODE}",
                ex=PersonaNameBoundsException(f"{method}: {PersonaNameBoundsException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_designation(cls, designation: str) -> SearchResult[List[Persona]]:
        """
        # ACTION:
            1.  Get any Persona entry whose name matches the target value.
        # PARAMETERS:
            *   designation (str)
        # RETURNS:
            *   SearchResult[List[Persona]] containing either:
                    - On error: Exception
                    - On finding a match: List[Persona] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *  PersonaNameBoundsException
            *  PersonaLookupFailedException
        """
        method = "PersonaLookup._by_designation"
        
        matches = [entry for entry in Persona if entry.designation.upper() == designation.upper()]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        
        # The default path is a failure.
        return SearchResult.failure(
            PersonaLookupFailedException(
                message=f"{method}: {PersonaLookupFailedException.ERROR_CODE}",
                ex=PersonaDesignationBoundsException(f"{method}: {PersonaDesignationBoundsException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_quota(cls, quota: int) -> SearchResult[List[Persona]]:
        """
        # ACTION:
            1.  Get any Persona entry whose name matches the target value.
        # PARAMETERS:
            *   quota (int)
        # RETURNS:
            *   SearchResult[List[Persona]] containing either:
                    - On error: Exception
                    - On finding a match: List[Persona] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *  PersonaNameBoundsException
            *  PersonaLookupFailedException
        """
        method = "PersonaLookup._by_quota"
        
        matches = [entry for entry in Persona if entry.quota == quota]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        
        # The default path is a failure.
        return SearchResult.failure(
            PersonaLookupFailedException(
                message=f"{method}: {PersonaLookupFailedException.ERROR_CODE}",
                ex=PersonaQuotaBoundsException(f"{method}: {PersonaQuotaBoundsException.DEFAULT_MESSAGE}")
            )
        )
  
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_ransom(cls, ransom: int) -> SearchResult[List[Persona]]:
        """
        # ACTION:
            1.  Get any Persona entry whose name matches the target value.
        # PARAMETERS:
            *   ransom (int)
        # RETURNS:
            *   SearchResult[List[Persona]] containing either:
                    - On error: Exception
                    - On finding a match: List[Persona] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *  PersonaNameBoundsException
            *  PersonaLookupFailedException
        """
        method = "PersonaLookup._by_ransom"
        
        matches = [entry for entry in Persona if entry.ransom == ransom]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        
        # The default path is a failure.
        return SearchResult.failure(
            PersonaLookupFailedException(
                message=f"{method}: {PersonaLookupFailedException.ERROR_CODE}",
                ex=PersonaRansomBoundsException(f"{method}: {PersonaRansomBoundsException.DEFAULT_MESSAGE}")
            )
        )
