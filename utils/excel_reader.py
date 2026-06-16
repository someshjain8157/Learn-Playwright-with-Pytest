from pathlib import Path
import json
import pandas as pd

EXCEL_FILE = (
    Path(__file__).resolve().parent.parent
    / "api_testdata.xlsx"
)


def get_config():

    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Config"
    )

    config = {}

    for _, row in df.iterrows():
        config[row["key"]] = row["value"]

    return config


import json
import pandas as pd

EXCEL_FILE = "api_testdata.xlsx"


def get_api_test_data():

    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name="APIData"
    )

    df = df.fillna("")

    records = df.to_dict("records")

    for record in records:

        payload = record.get("payload")

        if payload:

            record["payload"] = json.loads(
                payload
            )

    return records