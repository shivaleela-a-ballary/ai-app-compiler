def generate_schemas(architecture):

    db_schema = []
    api_schema = []

    for entity in architecture["entities"]:

        db_schema.append({
            "table": entity["name"].lower() + "s",
            "fields": entity["fields"]
        })

        api_schema.append({
            "path": "/" + entity["name"].lower() + "s",
            "method": "GET"
        })

    return {
        "app_type": architecture["app_type"],
        "database": db_schema,
        "apis": api_schema
    }