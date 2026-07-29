import json
import os


def save_json(projects):

    os.makedirs("report", exist_ok=True)

    with open(
        "report/report.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            projects,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("JSON saved successfully!") 