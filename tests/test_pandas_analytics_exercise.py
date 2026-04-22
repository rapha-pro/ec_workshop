"""
Tests for short pandas analytics exercise
"""

import pytest
from src.pandas_analytics_exercise import j_e_p, f_e_m


def test_join_structure(employee_data, project_assignments, months):
    """
    Test that join returns expected columns.
    """

    # TODO:
    # check that "birth_month" is a column
    # check that "<your_name>" is in the merged dataframe
    # check that "<your department>" is in the merged dataframe
    # check that "<your birthmonth>" is in the merged dataframe
    # (hint: use result.columns)


@pytest.mark.parametrize("month,expected_count", [
    ("February", _),
    ("January", _),
    ("June", _),
    ("August", _),
])
def test_filter_employees_by_month(
    employee_data,
    project_assignments,
    months,
    month,
    expected_count
):
    """
    Test filtering employees by month.
    """

    df = j_e_p(employee_data, project_assignments, months)
    result = f_e_m(df, month)

    # TODO:
    # correctly fill the parametrize fixture on top of the function
    # check that the length of result equals expected_count
    # (hint: use len(...) and expected count)