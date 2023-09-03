def format_linter_error(error: dict) -> dict:
    formatted_error = {
        "line": error["line_nuber"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }
    return formatted_error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    formatted_errors = [format_linter_error(error) for error in errors]
    status = "failed" if formatted_errors else "passed"
    formatted_file = {
        "errors": formatted_errors,
        "path": file_path,
        "status": status,
    }
    return formatted_file


def format_linter_report(linter_report: dict) -> list:
    formatted_report = [format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items()]
    return formatted_report
