# src/chess/formation/key/lookup/forward.py

"""
Module: chess.formation.key.lookup.forward
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.formation import Formation, FormationSuperKey, FormationSuperKeyValidator
from chess.formation.key.lookup.exception.wrapper import FormationLookupFailedException
from chess.system import ForwardLookup, GameColor, LoggingLevelRouter, SearchResult, id_emitter


class FormationLookup(ForwardLookup[Formation]):
    """
     # ROLE: Forward Lookups

     # RESPONSIBILITIES:
     1.  Run forward lookups on the Formation hashtable to find a Team's play_directive_metadata for a game.
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
    def forward(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.lookup_id,
            super_key_builder: FormationBuilder = FormationBuilder(),
            enum_validator: FormationValidator = FormationValidator(),
            super_key_validator: FormationValidator = FormationValidator(),
    ):
        super().forward(
            id=id, 
            name=name,
            enum_validator=enum_validator,
            super_key_builder=super_key_builder, 
            super_key_validator=super_key_validator
        )

    
    @property
    def allowed_names(self) -> List[str]:
        """Returns a list of all permissible formation names in upper case."""
        return [order.name.upper() for order in Formation]
    
    @property
    def allowed_colors(self) -> List[GameColor]:
        """Returns a list of all permissible order colors."""
        return [member.color for member in Formation]
    
    @property
    def allowed_designations(self) -> List[str]:
        """Returns a list of all permissible order designations in upper case."""
        return [member.designation.upper() for member in Formation]
    
    @property
    def allowed_squares(self) -> List[str]:
        """Returns the names of squares Pieces make their opening move from."""
        return [member.square.upper() for member in Formation]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def query(
            cls, 
            super_key: FormationSuperKey, 
            super_key_validator: FormationSuperKeyValidator = FormationSuperKeyValidator()
    ) -> SearchResult[List[Formation]]:
        """
        # ACTION:
            1.  Certify the provided key with the validator.
            2.  If the key validation fails return the exception in a validation result. Otherwise, return
                the formation entries with the targeted key-values.
        # PARAMETERS:
            *   key: FormationSuperKey
            *   key_validator: FormationSuperKeyValidator
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
        # After verification use the hash key to route to the appropriate lookup method.
        
        # Entry point into forward lookups by designation.
        if super_key.designation is not None:
            return cls._by_designation(designation=super_key.designation)
        # Entry point into forward lookups by square_name.
        if super_key.square_name is not None:
            return cls._by_square_name(square=super_key.square_name)
        # Entry point into forward lookups by scolor.
        if super_key.color is not None:
            return cls._by_color(color=super_key.color)
        
        # For other entry points return the exception chain.
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
        matches = [order for order in Formation if order.designation.upper() == designation.upper()]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        # Any other case is a failure.
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
        matches = [order for order in Formation if order.square_name.upper() == square_name.upper()]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
            # Any other case is a failure.
        return SearchResult.failure(
            FormationLookupFailedException(
                message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                ex=FormationSquareNameBoundsException(f"{method}: {FormationSquareNameBoundsException.DEFAULT_MESSAGE}")
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
        matches = [order for order in Formation if order.color == color]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
            # Any other case is a failure.
        return SearchResult.failure(
            FormationLookupFailedException(
                message=f"{method}: {FormationLookupFailedException.ERROR_CODE}",
                ex=FormationColorBoundsException(f"{method}: {FormationColorBoundsException.DEFAULT_MESSAGE}")
            )
        )