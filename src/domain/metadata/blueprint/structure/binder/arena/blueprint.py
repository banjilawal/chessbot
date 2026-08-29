# src/domain/metadata/blueprint/structure/toggle/arena/blueprint.py

"""
Module: domain.metadata.blueprint.structure.toggle.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

@dataclass
class ArenaPlayerColorBinderBlueprint(StructureBlueprint[ArenaPlayerColorBinder]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating an ArenaPlayerColorBinderBlueprint object.

    Attributes:
        id: Optional[int]
        arena: Arena
        schema: Schema
        player_service: PlayerService
        domain_null_exception: AreaBinderNullException
        model_type: AreaBinder
        
    Provides:

    Super Class:
        Blueprint
    """
    arena: Arena
    schema: Schema
    id: Optional[int] | None = None
    player_service: PlayerService | None = PlayerService()
    domain_null_exception: AreaBinderNullException = AreaBinderNullException()
    model_type: AreaBinder = AreaBinder
    

