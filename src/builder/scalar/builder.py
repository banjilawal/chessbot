# src/builder/scalar/builder.py

"""
Module: builder.scalar.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""




class ScalarBuilder(Builder[Scalar]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
     """
    @LoggingLevelRouter.monitor
    def build(
            self,
            value: int,
            toolkit: NumberToolkit | None = None,
    ) -> BuildResult[Scalar]:
        """
        # ACTION:
        If the absolute value of the param is within BOARD_DIMENSION return a new Scalar instance.
        Otherwise, return an exception.
    
        # PARAMETERS:
            *   value (int)
            *   scalar_validator (ScalarValidator)
    
        # RETURNS:
          BuildResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.
    
        Raises:
            * ScalarBuilderException
        """
        method = "ScalarBuilder.build"
        
        try:
            validation = scalar_validator.validate_value(value)
            if validation.is_failure():
                return BuildResult.failure(validation.exception)
            
            return BuildResult.sucess(payload=Scalar(value=value))
        
        except Exception as ex:
            return BuildResult.failure(
                ScalarBuilderException(
                    ex=ex,
                    msg=f"{method}: "
                            f"{ScalarBuilderException.MSG}"
                )
            )
