from chess.attack import Attack, AttackingFriendlySquareException
from chess.square import Square, SquareService
from chess.system import LoggingLevelRouter
from chess.token import ReadinessState, Token, TokenService


class Move:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            destination: Square,
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
    ):
        method = "Move.execute"
        
        readiness_analysis_result = token_service.readiness_analyzer.analyze(token=token)
        if readiness_analysis_result.is_failure:
            return MoveResult.failure(
                MoveFailedException(
                    f"{method}: {MoveFailedException.DEFAULT_MESSAGE}",
                    ex=readiness_analysis_result.exception,
                )
            )
        if not readiness_analysis_result.primary != ReadinessState.FREE:
            return MoveResult.failure(
                MoveFailedException(
                    f"{method}: {MoveFailedException.DEFAULT_MESSAGE}",
                    ex=InactiveTokenCannotMoveException(
                        f"{method}: {InactiveTokenCannotMoveException.DEFAULT_MESSAGE}"
                    ),
                )
            )
        square_is_empty_result = square_service.verify_square_is_empty(square=destination)
        if square_is_empty_result.is_failure:
            return MoveResult.failure(
                MoveFailedException(
                    f"{method}: {MoveFailedException.DEFAULT_MESSAGE}",
                    ex=square_is_empty_result.exception,
                )
            )
        if not square_is_empty_result.payload:
            cls._to_occupied_square(token=token, square=destination, square_service=square_service)
        insertion_result = square_service.process_square_occupation(
            square=destination,
            token=token,
            token_service=token_service
        )
        if insertion_result.is_failure:
            return MoveResult.failure(
                MoveFailedException(
                    f"{method}: {MoveFailedException.DEFAULT_MESSAGE}",
                    ex=insertiion_result.exception,
                )
            )
        return insertion_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _to_occupied_square(
            token: Token,
            square: Square,
            square_service: SquareService,
            attack: Attack = Attack(),
    ):
        method = "Move._to_occupied_square"
        
        if not token.is_enemy(destination.occupant):
            return MoveResult.failure(
                MoveFailedException(
                    f"{method}: {MoveFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingFriendlySquareException(
                        f"{method}: {AttackingFriendlySquareException.DEFAULT_MESSAGE}"
                    )
                )
            )
        return attack.execute(token=token, square=square, square_service=square_service)
        
        
        