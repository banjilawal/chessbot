from typing import Generic, TypeVar, Optional


T = TypeVar('T')


class Directive(Generic[T]):
    """
    A data-holding object representing an`actor`'s intent to perform a
    state changing operation  on a `target`. An `Action` can change state of:

    The Directive is handled by an Executor who carry out the directive
    It is used for doing rollback

    * Its `actor` who initiates and performs the activity
    * The `target` which the operation is performed upon.

    ## Possible State Changes:
    - If the actor wants to change its state then target is a resource `actor` needs.
    - If `actor` wants to change `target` state then the `actor' state might not be affected

    Attributes:
        _id (`int`): A unique identifier for an `operation`.
        _actor (`T`): The entity performing the state-changing activity
        _target (`T`): The `target` can either
    """
    _id: int
    _actor: T
    _target: Optional[T]

    def __init__(self, directive_id: int, actor: T, target: Optional[T]=None):
        self._id = directive_id
        self._actor = actor
        self._target = target


    @property
    def id(self) -> int:
        return self._id


    @property
    def actor(self) -> T:
        return self._actor


    @property
    def target(self) -> Optional[T]:
        return self._target


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Directive):
            return False
        return self._id == other.id == other.id