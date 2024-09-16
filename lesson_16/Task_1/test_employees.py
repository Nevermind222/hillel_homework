from employees import TeamLead
from assertpy import assert_that


class TestEmployees:

    qa_automation_team_lead: TeamLead = TeamLead("Mark", 5000, "Test department", 5)

    expected_mark_attrs: dict[str, object] = {
        "name": "Mark",
        "salary": 5000,
        "department": "Test department",
        "team_size": 5
    }

    expected_mark_attrs_negative: dict[str, object] = {
        "name": "Mark",
        "salary": 5000,
        "department": "Test_department",
        "team_size": 5
    }

    def test_employee_attrs(self):

        (assert_that(self.qa_automation_team_lead.__dict__, "User's attrs are not equal to expected attrs")
         .is_equal_to(self.expected_mark_attrs))

    def test_employee_attrs_negative(self):
        (assert_that(self.qa_automation_team_lead.__dict__, "User's attrs are not equal to expected attrs")
         .is_equal_to(self.expected_mark_attrs_negative))
