import unittest
from unittest.mock import Mock

from assurance.exception.result import ResultPayloadConflictException
from assurance.result.base import Result


class ResultTest(unittest.TestCase):

    def test_construct_result_with_payload_and_exception_raise_error(self):
        mock_payload = Mock()
        mock_exception = Mock()

        with self.assertRaises(ResultPayloadConflictException):
            Result(payload=mock_payload, exception=mock_exception)


    def test_construct_result_with_payload_only_succeeds(self):
        mock_payload = Mock()
        result = Result(payload=mock_payload, exception=None)

        self.assertEqual(result._payload, mock_payload)
        self.assertIsNone(result._exception)

    def test_construct_result_with_exception_only_succeeds(self):
        mock_exception = Mock()
        result = Result(payload=None, exception=mock_exception)

        self.assertIsNone(result._payload, None)
        self.assertEqual(result._exception, mock_exception)


if __name__ == '__main__':
    unittest.main()
