# src/chess/formation/key/lookup/forward.py

"""
Module: chess.formation.key.lookup.forward
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.formation import Formation
from chess.system import ForwardLookup, GameColor, LoggingLevelRouter, SearchResult, id_emitter


class FormationLookup(ForwardLookup[Formation]):
    """
    # ROLE: Forward Lookups, Mapping 

    # RESPONSIBILITIES:
    1.  Lookup microservice API for mapping metadata values to Formation configurations.
    2.  Encapsulates integrity assurance logic for Formation lookup operations.


    # PARENT:
        *   EntityLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ForwardLookup for inherited attributes.
    """
    SERVICE_NAME = "FormationLookupService"
    
    def forward(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.lookup_id,
            context_builder: FormationBuilder = FormationBuilder(),
            enum_validator: BattleOrderValidator = BattleOrderValidator(),
            context_validator: FormationValidator = FormationValidator(),
    ):
        super().forward(
            id=id, 
            name=name,
            enum_validator=enum_validator,
            context_builder=context_builder, 
            context_validator=context_validator
        )
    
    @property
    def order_validator(self) -> BattleOrderValidator:
        """Return an BattleOrderValidator."""
        return cast(BattleOrderValidator, self.enum_validator)
    
    @property
    def order_context_builder(self) -> FormationBuilder:
        """Return an FormationBuilder."""
        return cast(FormationBuilder, self.context_builder)
    
    @property
    def order_context_validator(self) -> FormationValidator:
        """Return an FormationValidator."""
        return cast(FormationValidator, self.context_validator)
    
    @property
    def allowed_names(self) -> List[str]:
        """Returns a list of all permissible schema names in upper case."""
        return [order.name.upper() for order in BattleOrder]
    
    @property
    def allowed_colors(self) -> List[GameColor]:
        """Returns a list of all permissible order colors."""
        return [member.color for member in BattleOrder]
    
    @property
    def allowed_designations(self) -> List[str]:
        """Returns a list of all permissible order designations in upper case."""
        return [member.designation.upper() for member in BattleOrder]
    
    @property
    def allowed_squares(self) -> List[str]:
        """Returns the names of squares Pieces make their opening move from."""
        return [member.square.upper() for member in BattleOrder]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def lookup(
            cls, 
            context: Formation, 
            context_validator: FormationValidator = FormationValidator()
    ) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Certify the provided map with the class method's validator param.
        2.  If the map validation fails return the exception in a validation result. Otherwise, return
            the configuration entries which matched the map.

        # Parameters:
            *   map: Formation
            *   context_validator: FormationValidator

        # Returns:
        SearchResult[List[Formation]] containing either:
            - On finding a match: List[Formation] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   FormationLookupFailedException
            *   FormationLookupException
        """
        method = "FormationLookup.find"
        try:
            # certify the map is safe.
            validation = context_validator.validate(candidate=context)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            # After map is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by designation value.
            if context.designation is not None:
                return cls._lookup_by_designation(designation=context.designation)
            # Entry point into searching by square_name value.
            if context.square is not None:
                return cls._lookup_by_square(square=context.square)
            # Entry point into searching by color value.
            if context.color is not None:
                return cls._lookup_by_color(color=context.color)
        
            # Failsafe if any map cases was missed
            return SearchResult.failure(
                OrderLookupFailedException(f"{method}: {OrderLookupFailedException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a FormationLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                FormationLookupException(ex=ex, message=f"{method}: {FormationLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_designation(cls, designation: str) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get any Formation which matches the target designation.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Formation]] containing either:
            - On finding a match: List[Formation] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   OrderDesignationBoundsException
            *   FormationLookupFailedException
        """
        method = "FormationLookup._find_by_designation"
        try:
            matches = [order for order in BattleOrder if order.designation.upper() == designation.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no order has that designation.
            return SearchResult.failure(
                FormationLookupByColorException(f"{method}: {DesignationBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a FormationLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                FormationLookupException(ex=ex, message=f"{method}: {FormationLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_square(cls, name: str) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get anyBattleOrder which matches the square_name's name.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Formation]] containing either:
            - On finding a match: List[Formation] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   FormationLookupBySquareException
            *   FormationLookupFailedException
        """
        method = "FormationLookup._find_by_square"
        try:
            matches = [order for order in BattleOrder if order.square.upper() == name.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no order has that square_name.
            return SearchResult.failure(
                FormationLookupByColorException(f"{method}: {FormationLookupBySquareException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a FormationLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                FormationLookupException(ex=ex, message=f"{method}: {FormationLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_color(cls, color: GameColor) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get any Formation which matches the target color.

        # Parameters:
            *   color (BattleOrderColor)

        # Returns:
        SearchResult[List[Formation]] containing either:
            - On finding a match: List[Formation] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   FormationLookupByColorException
            *   FormationLookupFailedException
        """
        method = "FormationLookup._find_by_color"
        try:
            matches = [order for order in BattleOrder if order.color == color]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no order has that color.
            return SearchResult.failure(
                FormationLookupByColorException(f"{method}: {FormationLookupByColorException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a FormationLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                FormationLookupException(ex=ex, message=f"{method}: {FormationLookupException.DEFAULT_MESSAGE}")
            )
