"""
Activity 3: Join employees with projects and analyze birthdays
"""

import pandas as pd


def j_e_p(
    employees_df,
    projects_df,
    months_df
):
    """
    Join employee data with project assignments and month names.

    Note:
        Use INNER JOIN.

    Args:
        employees_df: Employee DataFrame (includes birth_month as int)
        projects_df: Project assignments DataFrame
        months_df: Mapping of month number to month name

    Returns:
        Merged DataFrame with employee info + project + month name
    """
    # TODO:
    # - add type hints
    # - rename function
    # - implement joins
    pass


def f_e_m(
    df,
    month
):
    """
    Filter employees born in a specific month.

    Args:
        df: DataFrame with employee info
        month: Month name (e.g., "February")

    Returns:
        Filtered DataFrame
    """
    # TODO:
    # - add type hints
    # - rename function
    # - implement filtering
    pass