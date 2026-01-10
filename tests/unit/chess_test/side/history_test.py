import unittest
from unittest.mock import create_autospec

from chess.exception.stack_exception import PushingNullEntityException, DuplicatePushException
from chess.side.team import Side
from chess.competitor.side import SideRecord


class TeamStackTest(unittest.TestCase):

  def test_internal_data_structure_not_null(self):
    self.assertIsNotNone(SideRecord().items)


  def test_new_team_stack_is_empty(self):
    self.assertTrue(len(SideRecord().items) == 0)


  def test_null_team_push_raises_exception(self):
    with self.assertRaises(PushingNullEntityException):
      SideRecord().push_team_to_player(None)


  def test_duplicate_team_push_raises_exception(self):
    team = create_autospec(Side, instance=True)
    team_stack = SideRecord()
    team_stack.push_team_to_player(team)

    with self.assertRaises(DuplicatePushException):
      team_stack.push_team_to_player(team)

  def test_pushing_team_updates_current_team(self):
    a_team = create_autospec(Side, instance=True)
    b_team = create_autospec(Side, instance=True)

    team_stack = SideRecord()
    team_stack.push_team_to_player(a_team)
    self.assertEqual(team_stack.current_team, a_team)

    team_stack.push_team_to_player(b_team)
    self.assertEqual(team_stack.current_team, b_team)


  def test_popping_items_does_not_mutate_stack(self):
    team = create_autospec(Side, instance=True)
    team_stack = SideRecord()
    team_stack.push_team_to_player(team)

    popped_team = list(team_stack.items).pop()

    self.assertEqual(popped_team, team)
    self.assertEqual(team_stack.size(), 1)
    self.assertEqual(team_stack.current_team, team)


  def test_pushing_team_increments_size(self):
    mock_team = create_autospec(Side, instance=True)

    team_stack = SideRecord()
    original_size = team_stack.size()
    self.assertEqual(team_stack.size(), 0)

    team_stack.push_team_to_player(mock_team)
    self.assertEqual(team_stack.size(), original_size + 1)


  def test_is_empty_corresponds_to_zero_stack_size(self):
    team_stack = SideRecord()
    self.assertTrue(team_stack.is_empty() and team_stack.size() == 0)


  def test_is_empty_false_when_stack_has_items(self):
    mock_team = create_autospec(Side, instance=True)
    team_stack = SideRecord()
    team_stack.push_team_to_player(mock_team)

    self.assertTrue(not team_stack.is_empty() and team_stack.size() > 0)


  def test_if_stack_Is_empty_then_current_team_is_null(self):
    team_stack = SideRecord()
    self.assertTrue(team_stack.is_empty() and team_stack.current_team is None)


if __name__ == '__main__':
  unittest.main()
