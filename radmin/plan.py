from pathlib import Path

def do_plan(target: str, output: Path):
    """
    1. Read all the .json files in the current directory or the input directory (see --chdir option) resursively
    2. dump the resources in the target environment
    3. compare the resources in the target environment with the dumped resources
    4. categorise the differences into create, update and delete operations
    5. write the plan file to disk
    """
    raise NotImplementedError