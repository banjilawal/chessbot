# src/chess/formation/key/lookup/lookup.py

"""
Module: chess.formation.key.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.formation import (
    Formation, FormationColorBoundsException, FormationDesignationBoundsException, FormationLookupFailedException,
    FormationLookupRouteException, FormationPersonaBoundsException, FormationSquareBoundsException, FormationKey,
    FormationKeyValidator
)
from chess.persona import Persona
from chess.system import GameColor, HashLookup, LoggingLevelRouter, SearchResult


class FormationLookup(HashLookup[Formation]):
    """
     # ROLE: Forward Lookups

     # RESPONSIBILITIES:
     1.  Run forward lookups on the Formation hashtable to find a Team's play_directive_metadata for a game.
     2.  Indicate there is no play_directive for a given key-value pair by returning an exception to the caller.
     3.  Verifies correctness of key-value key before running lookup.

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
    @LoggingLevelRouter.monitor
    def query(
            cls, 
            super_key: FormationKey,
            super_key_validator: FormationKeyValidator = FormationKeyValidator()
    ) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            1.  Certify the provided key with the validator.
            2.  If the key validation fails return the exception in a validation result. Otherwise, return
                the formation entries with the targeted key-values.
        # PARAMETERS:
            *   key: FormationKey
            *   key_validator: FormationKeyValidator
        # RETURNS:
            *   SearchResult[List[Formation]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Formation] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   FormationLookupFailedException
        """
        method = "FormationLookup.find"

        # Handle the case that the SuperKey fails validation.
        validation = super_key_validator.validate(candidate=super_key)
        if validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                FormationLookupFailedException(
                    message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                    ex=validation.exception
                )
            )
        
        # --- Route to the lookup method which matches the super_key attribute. ---#
        
        # Entry point into forward lookups by designation.
        if super_key.designation is not None:
            return cls._by_designation(designation=super_key.designation)
        # Entry point into forward lookups by square_name.
        if super_key.square_name is not None:
            return cls._by_square_name(square=super_key.square_name)
        # Entry point into forward lookups by color.
        if super_key.color is not None:
            return cls._by_color(color=super_key.color)
        # Entry point into forward lookups by persona.
        if super_key.persona is not None:
            return cls._by_persona(persona=super_key.persona)
        
        # The default path is only reached when a super_key.attribute does not have a lookup route. Return
        # the exception chain.
        return SearchResult.failure(
            FormationLookupFailedException(
                message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                ex=FormationLookupRouteException(f"{method}: {FormationLookupRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_designation(cls, designation: str) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            1.  Get any Formation entry whose designation matches the target value.
        # PARAMETERS:
            *   designation (str)
        # RETURNS:
            *   SearchResult[List[Formation]] containing either:
                    - On error: Exception
                    - On finding a match: List[Formation] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   FormationDesignationBoundsException
            *   FormationLookupFailedException
        """
        method = "FormationLookup._find_by_designation"
        matches = [entry for entry in Formation if entry.designation.upper() == designation.upper()]
        
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        # An empty lookup result is a failure. Return the exception chain.
        return SearchResult.failure(
            FormationLookupFailedException(
                message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                ex=FormationDesignationBoundsException(f"{method}: {FormationDesignationBoundsException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_square_name(cls, square_name: str) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            1.  Get any Formation entry whose designation matches the target value.
        # PARAMETERS:
            *   square_name (str)
        # RETURNS:
            *   SearchResult[List[Formation]] containing either:
                    - On error: Exception
                    - On finding a match: List[Formation] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   FormationSquareNameBoundsException
            *   FormationLookupFailedException
        """
        method = "FormationLookup._query_b_square_name"
        matches = [entry for entry in Formation if entry.square_name.upper() == square_name.upper()]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
            # An empty lookup result is a failure. Return the exception chain.
        return SearchResult.failure(
            FormationLookupFailedException(
                message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                ex=FormationSquareBoundsException(f"{method}: {FormationSquareBoundsException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_color(cls, color: GameColor) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            1.  Get any Formation entry whose designation matches the target value.
        # PARAMETERS:
            *   color (GameColor)
        # RETURNS:
            *   SearchResult[List[Formation]] containing either:
                    - On error: Exception
                    - On finding a match: List[Formation] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   FormationColorBoundsException
            *   FormationLookupFailedException
        """
        method = "FormationLookup._by_color"
        matches = [entry for entry in Formation if entry.color == color]
        
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
            # An empty lookup result is a failure. Return the exception chain.
        return SearchResult.failure(
            FormationLookupFailedException(
                message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                ex=FormationColorBoundsException(f"{method}: {FormationColorBoundsException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _by_persona(cls, persona: Persona) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            1.  Get any Formation entry whose designation matches the target value.
        # PARAMETERS:
            *   persona (Persona)
        # RETURNS:
            *   SearchResult[List[Formation]] containing either:
                    - On error: Exception
                    - On finding a match: List[Formation] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   FormationColorBoundsException
            *   FormationLookupFailedException
        """
        method = "FormationLookup._by_color"
        matches = [entry for entry in Formation if entry.persona == persona]
        
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
            # An empty lookup result is a failure. Return the exception chain.
        return SearchResult.failure(
            FormationLookupFailedException(
                message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                ex=FormationPersonaBoundsException(f"{method}: {FormationPersonaBoundsException.DEFAULT_MESSAGE}")
            )
        )