# src/microservice/game/microservice.py

"""
Module: microservice.game.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class GameService(Microservice[Game]):
    """
    Role:Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Game microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Game state by providing single entry and exit points to Game
        lifecycle.

    Super Class:
        *   Microservice

    # PROVIDES:
        *   build: --> GameBuilder
        *   validation: --> GameValidator


    # INHERITED ATTRIBUTES:
        *   See Microservice for inherited attributes.
    """
    DEFAULT_NAME = "GameService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: GameBuilder = GameBuilder(),
            validator: GameValidator = GameValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   schema (str)
            *   build (GameFactory)
            *   validation (GameValidator)

        # RETURNS:
        None

        Raises:
        """
        method = "GameService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> GameBuilder:
        """get GameBuilder"""
        return cast(GameBuilder, self.entity_builder)
    
    @property
    def validator(self) -> GameValidator:
        """get GameValidator"""
        return cast(GameValidator, self.entity_validator)
    
    
    