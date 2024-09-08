from assertpy import assert_that
from homework_10 import log_event
import logging


class TestThatFunction:
    def test_info_logs(self, caplog):
        caplog.set_level(logging.DEBUG)
        log_event("UserA", "success")
        output = caplog.text
        assert_that(output.startswith("INFO")).is_true()

    def test_warning_logs(self, caplog):
        caplog.set_level(logging.DEBUG)
        log_event("UserB", "expired")
        output = caplog.text
        assert_that(output.startswith("WARNING")).is_true()

    def test_error_logs(self, caplog):
        caplog.set_level(logging.DEBUG)
        log_event("UserC", "forbidden")
        output = caplog.text
        assert_that(output.startswith("ERROR")).is_true()
