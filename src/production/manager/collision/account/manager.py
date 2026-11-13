# src/production/manager/collision/account/manager.py

"""
Module: production.manager.collision.account.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, Optional, cast

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account, AccountContext, HumanAccount, MachineAccount
from environment import AccountCollisionDetector
from err import ChessException
from production import CollisionManager
from util import LoggingLevelRouter


class AccountCollisionManager(CollisionManager[Account]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Detect if an insert breaks Account collection's uniqueness
            constraint.

    Attributes:
        detector: AccountCollisionDetector

    Provides:
        -   def execute(item: Account, collection: AccountStack) -> CollisionReport
        
    Super Class
        CollisionManager
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
    def execute(self, item: Account, collection: AccountStack) -> CollisionReport:
        """
        Assure the item will be unique in the Account collection.
        
        Action:
            1.  If the item shares an attribute-value supposed to be unique to the
                collection, send an exception chain in the report.
            2.  Otherwise, report that primary keys will be maintained.
        Args:
            item: Account
            collection: AccountStack
        Returns:
           CollisionReport
        Raises:
            AccountCollisionManagerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        table: Dict[int, List[Account]] = {}
        context = AccountContext(id=item.id)

        report = self.detector.router.execute(context=context, stream=collection)
        if report.collision_exists:
            particle = cast(Account, report.particle)
            table[0] = [item, particle]
        if isinstance(item, HumanAccount):
            account = cast(HumanAccount, item)
            context = AccountContext(email=account.email)
        if isinstance(item, MachineAccount):
            account = cast(MachineAccount, item)
            context = AccountContext(machine_name=account.name)
        report = self.detector.router.execute(context=context, stream=collection)
        if report.collision_exists:
            particle = cast(Account, report.particle)
            table[1] = [item, particle]
            
        type_count = self._type_counter(table)
        table_size = len(table)
        if table_size == 0 and type_count == 0:
            return CollisionReport.empty()
        if table_size 1
             # decembeer 12 mcn start 7 pm
        matches = [
            account for account in collection.list if account.id == item.id
        ]
        if len(matches) > 0:
            table[0] = [item, matches[0]]
        string_table = self._human(item=item, collection=collection)
        
        table_size = len(table)
        
        for key in self._human.keys():
            table[key] = string_table[key]
        type_count = self._type_counter(table)
        if type == 0:
            return CollisionReport.empty()
        if type_count == 1 and table_size == 2:
            return CollisionReport.
            
            
            
        
        
        
        # success_report = CollisionReport.empty()
        # failure_report = CollisionReport.empty()
        # # --- Assure the global primary key constraint is not violated. ---#
        # report = self.detector.execute(
        #     context=context,
        #     stream=collection,
        # )
        # if report.collision_exists:
        #     table = {
        #         "account_original": item
        #     }
        # return CollisionReport.empty()
    
    @LoggingLevelRouter.monitor
    def _human(
            self,
            account: HumanAccount,
            collection: AccountStack,
    ) -> CollisionReport:
        email_collider = account
        id_collider = account
        context = AccountContext(id=account.id)
        id_report = self.detector.execute(context=context, stream=collection)
        if id_report.collision_exists:
            id_collider = cast(Account, id_report.particle)
        context = AccountContext(email=account.email)
        email_report = self.detector.execute(context=context, stream=collection)
        if email_report.collision_exists:
            email_collider = cast(HumanAccount, email_report.particle)
        if not isinstance(id_collider, HumanAccount):
            return CollisionReport.collision(
                context=context,
                particle=id_collider,
                exception=ChessException(ex=id_report.exception)
            )
        human_id_collider = cast(HumanAccount, id_collider)
        
        if human_id_collider.email.upper() == account.email.upper():
        
        table = {}
        if (item, HumanAccount):
            target = cast(HumanAccount, item).email.upper()
            matches = [
                account for account in collection.human_accounts if (
                        account.email.upper() == target
                )
            ]
            if len(matches) > 0:
                table[1] = [item, matches[0]]
        table = self._machine(item=cast(MachineAccount,item), collection=collection)
        return table
   
    @LoggingLevelRouter.monitor
    def _machine(self, item: MachineAccount, collection: AccountStack) -> Dict[int, List[Account]]:
        target = item.name.upper()
        table = {}
        matches = [
            account for account in collection.machine_accounts if(
                account.name.upper() == target
            )
        ]
        if len(matches) > 0:
            table[1] = [item, matches[0]]
        return table
    
    @LoggingLevelRouter.monitor
    def _type_counter(self, table: Dict[int, List[Account]]) -> int:
        count = 0
        for key in table.keys():
            items = table[key]
            if [type(items[0]).__name__.upper() == type(items[1]).__name__.upper()]:
                count = count + 1
            count = count + 2
        if count == 2:
            type_1 = table[0][0]
            type_2 = table[1][0]
            if type_1.upper() == type_2.upper():
                count = 1
        return count
    
    @LoggingLevelRouter.monitor
    def __human_resolver(self, table: Dict[int, List[Account]]) -> int:
        target_class = type(HumanAccount).__name__.upper()
        for key in table.keys():
            items = table[key]
            if [type(items[0]).__name__.upper() == type(items[1]).__name__.upper()]:
                count = count + 1
            count = count + 2
        if count == 2:
            type_1 = table[0][0]
            type_2 = table[1][0]
            if type_1.upper() == type_2.upper():
                count = 1
        return count

        
        