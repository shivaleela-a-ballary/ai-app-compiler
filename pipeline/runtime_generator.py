def generate_fastapi_code(schemas):

    code = "from fastapi import APIRouter\n\n"
    code += "router = APIRouter()\n\n"

    for api in schemas["apis"]:

        path = api["path"]

        name = path.replace("/", "")

        code += f'''
@router.get("{path}")
def get_{name}():
    return []

'''

    return code


def generate_sql_schema(schemas):

    sql = ""

    for table in schemas["database"]:

        sql += f"CREATE TABLE {table['table']} (\n"

        columns = []

        for field in table["fields"]:

            if isinstance(field, dict):

                name = field.get("name", "unknown")
                dtype = field.get("type", "TEXT")

                sql_type_map = {
                    "UUID": "UUID",
                    "string": "VARCHAR(255)",
                    "timestamp": "TIMESTAMP"
                }

                sql_type = sql_type_map.get(dtype, "TEXT")

                column = f"    {name} {sql_type}"

                if field.get("primary_key"):
                    column += " PRIMARY KEY"

                columns.append(column)

            else:
                columns.append(f"    {field} TEXT")

        sql += ",\n".join(columns)

        sql += "\n);\n\n"

    return sql