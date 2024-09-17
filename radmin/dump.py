from pathlib import Path

def do_dump(source: str, templates: list[str], output: Path):
    # 1. query the mongo db for templates, reports and schedules, joining on the template id
    # 2. from every template, get an analysis id and start an batch-export-job using boto3
    # 3. smush each template-tree into a single json file
    # 4. write all the files to disk

    raise NotImplementedError('Not implemented yet')