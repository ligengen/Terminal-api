import unittest
import mock
from src.execute_cleanup.execute_cleanup import *
from click.testing import CliRunner
from tests.test_info import *
from tests.test_mock import MockResponse
from unittest.mock import Mock, patch


res = {
    "statistics": {
        "deleted_tasks": 10
    }
}
query_req = {

}
query_url = "/api/v1/_manage/cleanup"


class ExecCleanupTest(unittest.TestCase):
    @mock.patch('requests.post')
    def test_post(self, mock_class):
        mock_class.return_value = MockResponse(success_res, 200)
        status_code, response = response_post()
        self.assertEqual(status_code, 200)
        self.assertEqual(response, success_res)

    @mock.patch('src.execute_cleanup.execute_cleanup.response_post')
    def test_cleanup(self, mock_class):
        mock_class.return_value = (200, res)
        runner = CliRunner()
        result = runner.invoke(exec_cleanup)
        output = "have been deleted"
        self.assertIn(output, result.output)
        self.assertEqual(result.exit_code, 0)

    @patch('requests.post')
    def test_response_get_err(self, mock_requests):
        mock_response = Mock(status_code=500)
        mock_requests.get.return_value = mock_response
        self.assertFalse(self.test_post())

    @mock.patch('requests.post')
    def test_response_not_200(self, mock_class):
        mock_class.return_value = MockResponse(res, 404)
        with self.assertRaises(SystemExit) as cm:
            response_post()
        self.assertEqual(cm.exception.code, 0)
