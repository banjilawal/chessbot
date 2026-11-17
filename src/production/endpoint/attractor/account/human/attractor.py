# src/production/endpoint/attractor/account/human/attractor.py

"""
Module: production.endpoint.attractor.account.human.attractor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account, AccountContext, HumanAccount
from environment import AccountCollisionDetector
from err import HumanAccountAttractorException
from production import AccountAttractor
from util import LoggingLevelRouter


class HumanAccountAttractor(AccountAttractor[HumanAccount]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Detect if an insert breaks Account collection's uniqueness
            constraint.

    Attributes:
        detector: AccountCollisionDetector

    Provides:
        -   def execute(target: Account, collection: AccountStack) -> CollisionReport
        
    Super Class
        AccountAttractor
    """
    
    def __init__(self, detector: Optional[AccountCollisionDetector] | None = None):
        """
        Args:
            detector: Optional[AccountCollisionDetector]
        """
        super().__init__(detector=detector or AccountCollisionDetector())

    @property
    def detector(self) -> AccountCollisionDetector:
        return cast(AccountCollisionDetector, super().detector)
    
    @LoggingLevelRouter.monitor
    def execute(self, target: HumanAccount, particle_stream: AccountStack) -> CollisionReport:
        """
        Assure the target will be unique in the Account collection.
        
        Action:
            1.  If the target shares an attribute-value supposed to be unique to the
                collection, send an exception chain in the report.
            2.  Otherwise, report that primary keys will be maintained.
        Args:
            target: Account
            particle_stream: AccountStack
        Returns:
           CollisionReport
        Raises:
            HumanAccountAttractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        # Handle the case that the id attracts a particle/
        report = self._id_attraction(target=target, particle_stream=particle_stream)
        if report.collision_exists:
            # Send the exception chain in the report.
            context = cast(AccountContext, report.context)
            particle = cast(Account, report.particle)
            return CollisionReport.collision(
                context=context,
                particle=particle,
                exception=HumanAccountAttractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountAttractorException.MSG,
                    err_code=HumanAccountAttractorException.ERR_CODE,
                    ex=report.exception
                )
            )
        # Handle the case that the email attracts a particle.
        report = self._email_attraction(target=target, particle_stream=particle_stream)
        if report.collision_exists:
            # Send the exception chain in the report.
            context = cast(AccountContext, report.context)
            particle = cast(HumanAccount, report.particle)
            return CollisionReport.collision(
                context=context,
                particle=particle,
                exception=HumanAccountAttractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountAttractorException.MSG,
                    err_code=HumanAccountAttractorException.ERR_CODE,
                    ex=report.exception
                )
            )
        # --- Forward the work product. ---#
        return CollisionReport.empty()
    
    @LoggingLevelRouter.monitor
    def _id_attraction(
            self, target: HumanAccount, particle_stream: AccountStack,
    ) -> CollisionReport:
        """
        Assure the target will be unique in the Account collection.

        Action:
            1.  Send an exception chain in the report if any of the following occur.
                    -   The colliding particle is only an Account instead of a HumanAccount.
                    -   The other HumanAccount has a different email address.
            2.  Otherwise, report that no collision was detected.
        Args:
            target: Account
            particle_stream: AccountStack
        Returns:
           CollisionReport
        Raises:
            HumanAccountAttractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Initialize temp variables and run the detector. ---#
        particle = target
        context = AccountContext(id=target.id)
        report = self.detector.execute(context=context, particle_stream=particle_stream)
        
        # --- Process the collision cases ---#
        if report.collision_exists:
            particle = cast(Account, report.particle)
        # Handle the case that the attractor is not a HumanAccount.
        if not isinstance(particle, HumanAccount):
            # Send an exception chain in the report.
            return CollisionReport.collision(
                context=context,
                particle=particle,
                exception=HumanAccountAttractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountAttractorException.MSG,
                    err_code=HumanAccountAttractorException.ERR_CODE,
                    ex=report.exception
                )
            )
        # --- Cast the particle for additional processing. ---#
        person = cast(HumanAccount, particle)
        
        # Handle the case that the other account has a different email address.
        if person.email.upper() != target.email.upper():
            # Send an exception chain in the report.
            return CollisionReport.collision(
                context=context,
                particle=person,
                exception=HumanAccountAttractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountAttractorException.MSG,
                    err_code=HumanAccountAttractorException.ERR_CODE,
                    ex=report.exception
                )
            )
        # --- Process the non-collision and equality cases. ---#
        return CollisionReport.empty()
    
    @LoggingLevelRouter.monitor
    def _email_attraction(
            self, target: HumanAccount, particle_stream: AccountStack,
    ) -> CollisionReport:
        """
        Assure the target will be unique in the Account collection.

        Action:
            1.  Send an exception chain in the report if any of the following occur.
                    -   The colliding particle has a different id.
            2.  Otherwise, report that no collision was detected.
        Args:
            target: Account
            particle_stream: AccountStack
        Returns:
           CollisionReport
        Raises:
            HumanAccountAttractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Initialize temp variables and run the detector. ---#
        particle = target
        context = AccountContext(email=target.email)
        report = self.detector.execute(context=context, particle_stream=particle_stream)
        
        # --- Process the collision cases ---#
        if report.collision_exists:
            particle = cast(Account, report.particle)
        # Handle the case that the attractor is not a HumanAccount.
        if not isinstance(particle, HumanAccount):
            # Send an exception chain in the report.
            return CollisionReport.collision(
                context=context,
                particle=particle,
                exception=HumanAccountAttractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountAttractorException.MSG,
                    err_code=HumanAccountAttractorException.ERR_CODE,
                    ex=report.exception
                )
            )
        # Handle the case that the other account has a different id address.
        if particle.id != target.id:
            # Send an exception chain in the report.
            return CollisionReport.collision(
                context=context,
                particle=particle,
                exception=HumanAccountAttractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountAttractorException.MSG,
                    err_code=HumanAccountAttractorException.ERR_CODE,
                    ex=report.exception
                )
            )
        # --- Process the non-collision and equality cases. ---#
        return CollisionReport.empty()

        
        