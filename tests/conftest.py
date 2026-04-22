import pytest
import pandas as pd


@pytest.fixture
def employee_data():
    return pd.DataFrame({
        'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
        'name': [
            'Ferdinand', 'Cynthia', 'Brittny', 'Gretha',
            'James', 'Alex', 'Raphael', 'Justin'
        ],
        'birth_month': [6, 2, 2, 2, 7, 12, 2, 5],
    })


@pytest.fixture
def project_assignments():
    return pd.DataFrame({
        'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
        'project_name': [
            'sas translation',
            'power bi',
            'sas translation',
            'sas translation',
            'power bi',
            'sas translation',
            'reporting',
            'power bi',
        ]
    })


@pytest.fixture
def months():
    return pd.DataFrame({
        'birth_month': list(range(1, 13)),
        'month_name': [
            'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ]
    })