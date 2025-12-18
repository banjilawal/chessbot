# src/chess/order/order/lookup/lookup.py

"""
Module: chess.order.order.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.formation import (
    OrderColorBoundsException, OrderContext, OrderContextBuilder, OrderContextValidator, BattleOrderLookupException,
    BattleOrderValidator, BattleOrder, OrderLookupFailedException, OrderNameBoundsException, OrderSquareBoundsException
)
from chess.system import EnumLookup, GameColor, LoggingLevelRouter, SearchResult, id_emitter


class BattleOrderLookup(EnumLookup[OrderContext]):
    """
    # ROLE: EnumLookup, Utility

    # RESPONSIBILITIES:
    1.  Lookup microservice API for mapping metadata values to BattleOrder configurations.
    2.  Encapsulates integrity assurance logic for lookup contexts and metadata enums in an extendable, maintainable
        module,
    3.  Authoritative single source of truth for permissible BattleOrder configurations.

    # PARENT:
        *   EntityLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EnumLookup for inherited attributes.
    """
    DEFAULT_NAME = "BattleOrderLookup"
    _order_validator: BattleOrderValidator
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.lookup_id,
            context_builder: OrderContextBuilder = OrderContextBuilder(),
            enum_validator: BattleOrderValidator = BattleOrderValidator(),
            context_validator: OrderContextValidator = OrderContextValidator(),
    ):
        super().__init__(
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
    def order_context_builder(self) -> OrderContextBuilder:
        """Return an OrderContextBuilder."""
        return cast(OrderContextBuilder, self.context_builder)
    
    @property
    def order_context_validator(self) -> OrderContextValidator:
        """Return an OrderContextValidator."""
        return cast(OrderContextValidator, self.context_validator)
    
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
            context: OrderContext, 
            context_validator: OrderContextValidator = OrderContextValidator()
    ) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  BattleOrder is an Enum to follow the EnumLookup contract a default dataset of List[BattleOrder] has been set.
            It's not used anywhere. even if a dataset argument is passed.
        2.  Use context_validator to certify the provided context.
        3.  Context attribute routes the search. Attribute value is the search target.
        4.  The outcome of the search is sent back to the caller in a SearchResult object.

        # Parameters:
            *   dataset (List[BattleOrder]):
            *   context: OrderContext
            *   context_validator: OrderContextValidator

        # Returns:
        SearchResult[List[BattleOrder]] containing either:
            - On finding a match: List[BattleOrder] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   BattleOrderLookupException
        """
        method = "BattleOrderLookup.find"
        try:
            # certify the context is safe.
            validation = context_validator.validate(candidate=context)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            # After context is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by designation value.
            if context.designation is not None:
                return cls._lookup_by_designation(designation=context.designation)
            # Entry point into searching by square value.
            if context.square is not None:
                return cls._lookup_by_square(square=context.square)
            # Entry point into searching by color value.
            if context.color is not None:
                return cls._lookup_by_color(color=context.color)
        
            # Failsafe if any context cases was missed
            return SearchResult.failure(
                OrderLookupFailedException(f"{method}: {OrderLookupFailedException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a BattleOrderLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderLookupException(ex=ex, message=f"{method}: {BattleOrderLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_designation(cls, designation: str) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get the BattleOrder which matches the target designation.

        # Parameters:
            *   designation (str)

        # Returns:
        SearchResult[List[BattleOrder]] containing either:
            - On finding a match: List[BattleOrder] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   OrderDesignationBoundsException
            *   BattleOrderLookupFailedException
        """
        method = "BattleOrderLookup._find_by_designation"
        try:
            matches = [order for order in BattleOrder if order.designation.upper() == designation.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no order has that designation.
            return SearchResult.failure(
                OrderColorBoundsException(f"{method}: {OrderNameBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a BattleOrderLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderLookupException(ex=ex, message=f"{method}: {BattleOrderLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_square(cls, name: str) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get the BattleOrder which matches the target designation.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[BattleOrder]] containing either:
            - On finding a match: List[BattleOrder] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   OrderDesignationBoundsException
            *   BattleOrderLookupFailedException
        """
        method = "BattleOrderLookup._find_by_square"
        try:
            matches = [order for order in BattleOrder if order.square.upper() == name.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no order has that square.
            return SearchResult.failure(
                OrderColorBoundsException(f"{method}: {OrderSquareBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a BattleOrderLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderLookupException(ex=ex, message=f"{method}: {BattleOrderLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_color(cls, color: GameColor) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get the BattleOrder which matches the target color.

        # Parameters:
            *   color (BattleOrderColor)

        # Returns:
        SearchResult[List[BattleOrder]] containing either:
            - On finding a match: List[BattleOrder] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   OrderColorBoundsException
            *   BattleOrderLookupFailedException
        """
        method = "BattleOrderLookup._find_by_color"
        try:
            matches = [order for order in BattleOrder if order.color == color]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            # If a match is not found return an exception. It's important to know if no order has that color.
            return SearchResult.failure(
                OrderColorBoundsException(f"{method}: {OrderColorBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a BattleOrderLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderLookupException(ex=ex, message=f"{method}: {BattleOrderLookupException.DEFAULT_MESSAGE}")
            )
