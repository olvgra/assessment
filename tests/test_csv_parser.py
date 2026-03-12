from pathlib import Path
from src.service.csv_parser import parse_csv

DATA_FILE = Path(__file__).parent.parent / "data" / "TestData.csv"

def test_parse_csv_from_file():
    text = DATA_FILE.read_text()
    result = parse_csv(text)

    assert len(result) == 4
    assert result[0] == {"First Name": "Dee", "Second Name": "Moore", "Score": "56"}