from pathlib import Path
from pymongo import MongoClient

def do_dump(source_env: str, templates: list[str], output: Path, db_conn_string: str):
    conn = MongoClient(db_conn_string)

    # database names follow convention
    db_name = f'reporting-${source_env}'

    db = conn.get_database(db_name)

    # 1. query the mongo db for templates, reports and schedules, joining on the template id

    # 2. from every template, get an analysis id and start an batch-export-job using boto3

    # 3. smush each template-tree into a single json file

    # 4. write all the files to disk

    raise NotImplementedError('Not implemented yet')