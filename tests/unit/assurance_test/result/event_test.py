import unittest
from unittest.mock import Mock

from assurance.exception.empty.result import EmptyEventOutcomeConstructorException
from chess.operation.op_result import OperationResult
from chess.operation.null_occupation_request import NullRequestException


class RequestOutcomeTest(unittest.TestCase):

    def test_construct_request_outcome_with_null_request_raises_error(self):
        mock_event = Mock()

        with self.assertRaises(NullRequestException):
            OperationResult(request=None, event=mock_event, exception=None)

    def test_construct_request_outcome_with_null_event_null_exception_raises_error(self):
        mock_request = Mock()

        with self.assertRaises(EmptyEventOutcomeConstructorException):
            OperationResult(request=mock_request, event=None, exception=None)


    def test_construct_request_outcome_with_event_only_succeeds(self):
        mock_request = Mock()
        mock_event = Mock()

        request_outcome = OperationResult(request=mock_request, event=mock_event, exception=None)

        self.assertEqual(request_outcome._event, mock_event)
        self.assertIsNone(request_outcome._exception, None)

    def test_construct_result_with_exception_only_succeeds(self):
        mock_request = Mock()
        mock_exception = Mock()

        request_outcome = OperationResult(request=mock_request, event=None, exception=mock_exception)

        self.assertIsNone(request_outcome._event, None)
        self.assertEqual(request_outcome._exception, mock_exception)


if __name__ == '__main__':
    unittest.main()
