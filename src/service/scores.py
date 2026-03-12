from src.dao.scores import get_score, insert_scores


def find_top_scorers(records: list[dict]) -> tuple[int, list[str]]:
    if not records:
        raise ValueError("No records provided.")

    top_score = None
    top_names = []

    for record in records:
        try:
            score = int(record["Score"])
        except (KeyError, ValueError) as exc:
            raise ValueError(f"Invalid score for record {record!r}") from exc

        first_name = record.get("First Name", "").strip()
        second_name = record.get("Second Name", "").strip()
        if not first_name or not second_name:
            raise ValueError(f"Missing name in record {record!r}")

        if top_score is None or score > top_score:
            top_score = score
            top_names = [first_name + " " + second_name]
        elif score == top_score:
            top_names.append(first_name + " " + second_name)

    top_names.sort()
    return top_score, top_names

def insert_scores_from_csv(records: list[dict]) -> None:
    if not records:
        raise ValueError("No records provided.")
    insert_scores(records)

def insert_score(first_name: str, second_name: str, score: int) -> int:
    return insert_score(first_name, second_name, score)

def get_score_by_id(id:int) -> dict:
    return get_score(id)