import unittest
from unittest.mock import create_autospec

from chess.exception.stack import PopEmptyStackException, PushingNullEntityException, DuplicatePushException
from chess.team.model import Team
from chess.team.stack import TeamStack


class TeamStackTest(unittest.TestCase):

    def test_internal_data_structure_not_null(self):
        self.assertIsNotNone(TeamStack().items)


    def test_new_team_stack_is_empty(self):
        self.assertTrue(len(TeamStack().items) == 0)


    def test_pop_empty_stack_raises_exception(self):
        with self.assertRaises(PopEmptyStackException):
            TeamStack().items.pop()


    def test_null_team_push_raises_exception(self):
        with self.assertRaises(PushingNullEntityException):
            TeamStack().push_team(None)


    def test_duplicate_team_push_raises_exception(self):
        team = create_autospec(Team, instance=True)
        team_stack = TeamStack()
        team_stack.push_team(team)

        with self.assertRaises(DuplicatePushException):
            team_stack.push_team(team)

    def test_pushing_team_updates_current_team(self):
        a_team = create_autospec(Team, instance=True)
        b_team = create_autospec(Team, instance=True)

        team_stack = TeamStack()
        team_stack.push_team(a_team)
        self.assertEqual(team_stack.current_team, a_team)

        team_stack.push_team(b_team)
        self.assertEqual(team_stack.current_team, b_team)

    # def test_only_copies_of_stack_are_popable(self):
    #     mock_team = create_autospec(Team, instance=True)
    #     team_stack = TeamStack().push_team(mock_team)


    def test_pushing_team_increments_size(self):
        mock_team = create_autospec(Team, instance=True)

        team_stack = TeamStack()
        original_size = team_stack.size()
        self.assertEqual(team_stack.size(), 0)

        team_stack.push_team(mock_team)
        self.assertEqual(team_stack.size(), original_size + 1)


    # def test_undo_push_decrements_size(self):
    #
    #     team_stack = TeamStack()
    #     team_stack.push_team(Team(row=1, column=1))
    #     size_before_undo = team_stack.size()
    #
    #     team_stack.undo_push()
    #     self.assertEqual(team_stack.size(), size_before_undo - 1)


    def test_is_empty_corresponds_to_zero_stack_size(self):
        team_stack = TeamStack()
        self.assertTrue(team_stack.is_empty() and team_stack.size() == 0)


    def test_is_empty_false_when_stack_has_items(self):
        mock_team = create_autospec(Team, instance=True)
        team_stack = TeamStack()
        team_stack.push_team(mock_team)

        self.assertTrue(not team_stack.is_empty() and team_stack.size() > 0)


    def test_if_stack_Is_empty_then_current_team_is_null(self):
        team_stack = TeamStack()
        self.assertTrue(team_stack.is_empty() and team_stack.current_team is None)


if __name__ == '__main__':
    unittest.main()
