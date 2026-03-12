import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path(__file__).parent.parent.parent / "db" / "scores.db"

def get_connection(db_path: Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: Path = DEFAULT_DB_PATH) -> None:
    with get_connection(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name    TEXT    NOT NULL,
                second_name    TEXT    NOT NULL,
                score   INTEGER NOT NULL
            )
        """)
        conn.commit()

def insert_scores(records: list[dict], db_path: Path = DEFAULT_DB_PATH) -> None:
    init_db(db_path)
    with get_connection(db_path) as conn:
        conn.executemany(
            "INSERT INTO scores (first_name, second_name, score) VALUES (?, ?, ?)",
            [(r["First Name"], r["Second Name"], int(r["Score"])) for r in records],
        )
        conn.commit()

def insert_score(first_name: str, second_name: str, score: int, db_path: Path = DEFAULT_DB_PATH) -> int:
    with get_connection(db_path) as conn:
        cursor = conn.execute(
            "INSERT INTO scores (first_name, second_name, score) VALUES (?, ?, ?)", (first_name, second_name, score)
        )
        conn.commit()
        return cursor.lastrowid

def get_score(id: int, db_path: Path = DEFAULT_DB_PATH) -> dict:
    with get_connection(db_path) as conn:
        row = conn.execute(
            "SELECT score FROM scores WHERE id = ?",
            (id,),
        ).fetchone()
        return dict(row) if row else None