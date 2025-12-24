from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_PERSONA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
    "PersonaSuperKeyBuildRouteException",
]


# ======================# UNHANDLED_PERSONA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
class PersonaSuperKeyBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that PersonaSuperKeyBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use PersonaSuperKey. There are different configurations of PersonaSuperKey that are correct. Each
        configuration must have a build route to guarantee all PersonaSuperKey products are safe. If a
        PersonaSuperKey configuration does not have a build route the last step in the logic will return a
        BuildResult containing a PersonaSuperKeyBuildRouteException.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PERSONA_SUPER_KEY_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The PersonaSuperKeyBuilder did not handle one of the paths necessary to guarantee PersonaSuperKeys are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )