import pandas as pd


def join_employees_projects_months(
    employees_df: pd.DataFrame,
    projects_df: pd.DataFrame,
    months_df: pd.DataFrame
) -> pd.DataFrame:
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

    merged = employees_df.merge(
        projects_df,
        on="employee_id",
        how="inner"
    )

    merged = merged.merge(
        months_df,
        on="birth_month",
        how="inner"
    )

    return merged


def filter_employees_by_month(
    df: pd.DataFrame,
    month: str
) -> pd.DataFrame:
    """
    Filter employees born in a specific month.

    Args:
        df: DataFrame with employee info
        month: Month name (e.g., "February")

    Returns:
        Filtered DataFrame
    """

    return df[df["month_name"] == month]