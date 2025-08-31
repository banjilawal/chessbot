import unittest
from unittest.mock import Mock

from assurance.exception.event import ConflictingEventStateException
from assurance.result.event import RequestOutcome
from chess.exception.null.request import NullRequestException


class RequestOutcomeTest(unittest.TestCase):

    def test_construct_request_outcome_with_event_and_exception_raise_error(self):
        mock_request = Mock()
        mock_event = Mock()
        mock_exception = Mock()

        with self.assertRaises(ConflictingEventStateException):
            RequestOutcome(request=mock_request, event=mock_event, exception=mock_exception)


    def test_construct_request_outcome_with_null_request_raise_error(self):
        mock_event = Mock()
        mock_exception = Mock()

        with self.assertRaises(NullRequestException):
            RequestOutcome(request=None, event=mock_event, exception=mock_exception)


    def test_construct_request_outcome_with_event_only_succeeds(self):
        mock_request = Mock()
        mock_event = Mock()

        request_outcome = RequestOutcome(request=mock_request, event=mock_event, exception=None)

        self.assertEqual(request_outcome._event, mock_event)
        self.assertIsNone(request_outcome._exception, None)

    def test_construct_result_with_exception_only_succeeds(self):
        mock_request = Mock()
        mock_exception = Mock()

        request_outcome = RequestOutcome(request=mock_request, event=None, exception=mock_exception)

        self.assertIsNone(request_outcome._event, None)
        self.assertEqual(request_outcome._exception, mock_exception)


if __name__ == '__main__':
    unittest.main()
