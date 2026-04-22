import pytest
from src.pandas_analytics_exercise import (
    join_employees_projects_months,
    filter_employees_by_month
)


def test_join_structure(employee_data, project_assignments, months):
    result = join_employees_projects_months(
        employee_data,
        project_assignments,
        months
    )

    assert "name" in result.columns.str.lower()
    assert "project_name" in result.columns.str.lower()

    assert "raphael" in result["name"].str.lower().values
    assert "reporting" in result["project_name"].str.lower().values
    assert "december" in result["month_name"].str.lower().values


@pytest.mark.parametrize("month,expected_count", [
    ("February", 4),
    ("July", 1),
    ("December", 1),
    ("June", 1),
])
def test_filter_employees_by_month(
    employee_data,
    project_assignments,
    months,
    month,
    expected_count
):
    df = join_employees_projects_months(
        employee_data,
        project_assignments,
        months
    )

    result = filter_employees_by_month(df, month)

    assert len(result) == expected_count