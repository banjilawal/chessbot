class ArenaService(EntityService[Arena]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Arena State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Arena state by providing single entry and exit points to Arena
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   ArenaService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "ArenaService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: ArenaBuilder = ArenaBuilder(),
            validator: ArenaValidator = ArenaValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
            *   builder (ArenaFactory)
            *   validator (ArenaValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> ArenaBuilder:
        """get ArenaBuilder"""
        return cast(ArenaBuilder, self.entity_builder)
    
    @property
    def validator(self) -> ArenaValidator:
        """get ArenaValidator"""
        return cast(ArenaValidator, self.entity_validator)