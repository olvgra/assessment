def parse_csv(text: str) -> list[dict]:
    lines = [line for line in text.strip().splitlines() if line.strip()]
    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]

    records = []
    for line in lines[1:]:
        fields = [f.strip() for f in line.split(",")]
        record = {headers[i]: fields[i] for i in range(len(headers))}
        records.append(record)

    return records