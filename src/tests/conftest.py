import pytest
from datetime import datetime

@pytest.fixture
def sample_product_data(tmp_path):
    data = [
        "Product A, 2023-03-01, 100.00\n",
        "Product B, 2023-03-15, 150.00\n",
        "Product A, 2023-04-10, 120.00\n",
        "Product B, 2023-04-20, 160.00\n"
    ]
    file_path = tmp_path / "products"
    with open(file_path, "w") as file:
        file.writelines(data)
    return file_path

@pytest.fixture
def today_date():
    return datetime(2024, 4, 12)
