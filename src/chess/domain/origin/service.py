
from chess.system import EntityService, id_emitter
from chess.domain import DomainOrigin, DomainOriginBuilder, DomainOriginValidator

class DomainOriginService(EntityService[DomainOrigin]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing DomainOrigin microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for DomainOrigin state by providing single entry and exit points to DomainOrigin
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   DomainOriginService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "DomainOriginService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: DomainOriginBuilder = DomainOriginBuilder(),
            validator: DomainOriginValidator = DomainOriginValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
            *   builder (DomainOriginFactory)
            *   validator (DomainOriginValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> DomainOriginBuilder:
        """get DomainOriginBuilder"""
        return cast(DomainOriginBuilder, self.entity_builder)
    
    @property
    def validator(self) -> DomainOriginValidator:
        """get DomainOriginValidator"""
        return cast(DomainOriginValidator, self.entity_validator)