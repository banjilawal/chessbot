
from logic.system import IntegrityService, id_emitter
from logic.domain import DomainOrigin, DomainOriginBuilder, DomainOriginValidator

class DomainOriginService(IntegrityService[DomainOrigin]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing DomainOrigin microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for DomainOrigin state by providing single entry and exit points to DomainOrigin
        lifecycle.

    Super Class:
        *   IntegrityService

    # PROVIDES:
        *   DomainOriginService


    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
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
            *   name (str)
            *   build (DomainOriginFactory)
            *   validation (DomainOriginValidator)

        # RETURNS:
        None

        Raises:
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> DomainOriginBuilder:
        """get DomainOriginBuilder"""
        return cast(DomainOriginBuilder, self.entity_builder)
    
    @property
    def validation(self) -> DomainOriginValidator:
        """get DomainOriginValidator"""
        return cast(DomainOriginValidator, self.entity_validator)