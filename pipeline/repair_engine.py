def repair_schema(schemas, validation):

    if validation["valid"]:
        return schemas

    tables = [table["table"] for table in schemas["database"]]

    for error in validation["errors"]:

        if "Missing table for API" in error:

            api_path = error.split("API ")[1]
            table_name = api_path.replace("/", "")

            if table_name not in tables:

                schemas["database"].append({
                    "table": table_name,
                    "fields": ["id"]
                })

    return schemas