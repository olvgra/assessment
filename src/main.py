from pathlib import Path

from src.service.csv_parser import parse_csv
from src.service.scores import insert_scores_from_csv, find_top_scorers

DATA_FILE = Path(__file__).parent.parent / "data" / "TestData.csv"

def main() -> None:
    text = DATA_FILE.read_text()
    records = parse_csv(text)
    insert_scores_from_csv(records)

    top_score, top_names = find_top_scorers(records)
    print(top_score)
    print(top_names)


if __name__ == "__main__":
    main()