from chess.token import TokenManifestBuilder, TokenManifestValidator


class TokenManifestService:
    _builder: TokenManifestBuilder
    _validator: TokenManifestValidator
    
    def __init__(
            self,
            builder: TokenManifestBuilder = TokenManifestBuilder(),
            validator: TokenManifestValidator = TokenManifestValidator(),
    ):
        self._builder = builder
        self._validator = validator
        
    @property
    def builder(self) -> TokenManifestBuilder:
        return self._builder
    
    @property
    def validator(self) -> TokenManifestValidator:
        return self._validator