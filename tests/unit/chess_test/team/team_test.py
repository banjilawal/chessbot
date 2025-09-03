import unittest
from unittest.mock import create_autospec

from chess.team.model import Side


class TeamTest(unittest.TestCase):

    @staticmethod
    def valid_mock_team():
        mock_team = create_autospec(Side, instance=True)

if __name__ == "__main__":
    unittest.main()