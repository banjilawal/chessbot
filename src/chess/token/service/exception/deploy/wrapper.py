from chess.system import OperationFailedException
from chess.token import TokenException


class TokenDeploymentFailedException(TokenException, OperationFailedException):
    pass