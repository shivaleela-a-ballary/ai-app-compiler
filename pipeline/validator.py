def validate_schema(config):

    errors = []

    tables = []

    for table in config["database"]:
        tables.append(table["table"])

    for api in config["apis"]:

        expected_table = api["path"].replace("/", "")

        if expected_table not in tables:
            errors.append(
                f"Missing table for API {api['path']}"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }