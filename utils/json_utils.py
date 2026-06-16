import json
from pathlib import Path


def save_actual_response(tc_id, response_json):
    """
    Save actual API response.
    File:
    actual_resp/<tc_id>_resp_actual.json
    """

    output_dir = Path("actual_resp")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / f"{tc_id}_resp_actual.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(
            response_json,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_expected_response(tc_id):
    """
    Load expected response.
    File:
    expected_resp/<tc_id>_resp_expected.json
    """

    file_path = (
        Path("expected_resp")
        / f"{tc_id}_resp_expected.json"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def compare_json(
        actual,
        expected,
        skip_keys=None,
        parent=""
):

    if skip_keys is None:
        skip_keys = []

    mismatches = []

    for key, expected_value in expected.items():

        if key in skip_keys:
            continue

        current_path = (
            f"{parent}.{key}"
            if parent else key
        )

        if key not in actual:

            mismatches.append(
                f"Missing key: {current_path}"
            )
            continue

        actual_value = actual[key]

        if (
            isinstance(expected_value, dict)
            and isinstance(actual_value, dict)
        ):

            mismatches.extend(
                compare_json(
                    actual_value,
                    expected_value,
                    skip_keys,
                    current_path
                )
            )

        elif actual_value != expected_value:

            mismatches.append(
                f"{current_path}: "
                f"Expected={expected_value}, "
                f"Actual={actual_value}"
            )

    return mismatches


def log_mismatch(tc_id, mismatches, actual, expected):
    """
    Write mismatch details to:
    logs/mismatched.txt
    """

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "mismatched.txt"

    with open(log_file, "a", encoding="utf-8") as f:

        f.write("\n")
        f.write("=" * 100 + "\n")
        f.write(f"TEST CASE : {tc_id}\n")
        f.write("=" * 100 + "\n")

        f.write("\nMISMATCHES:\n")

        for mismatch in mismatches:
            f.write(f"{mismatch}\n")

        f.write("\nEXPECTED RESPONSE:\n")
        f.write(
            json.dumps(
                expected,
                indent=4,
                ensure_ascii=False
            )
        )

        f.write("\n\nACTUAL RESPONSE:\n")
        f.write(
            json.dumps(
                actual,
                indent=4,
                ensure_ascii=False
            )
        )

        f.write("\n\n")