import pytest
from datetime import datetime, timedelta
from src.productReader import read_product_changes, calculate_price_change



def test_read_product_changes(sample_product_data):
    changes = read_product_changes(sample_product_data, "Product A")
    assert len(changes) == 0
def test_calculate_price_change(today_date):
    price_changes = [
        (datetime(2023, 3, 1), 100.00),
        (datetime(2023, 4, 10), 120.00)
    ]
    price_change = calculate_price_change(price_changes)
    assert price_change == 20.00

def test_read_product_changes_empty(sample_product_data):
    changes = read_product_changes(sample_product_data, "Product C")
    assert len(changes) == 0

@pytest.mark.parametrize("date_str, expected_date", [
    ("2023-03-01", datetime(2023, 3, 1)),
    ("2023-04-10", datetime(2023, 4, 10))
])
def test_date_parsing(date_str, expected_date):
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    assert parsed_date == expected_date
