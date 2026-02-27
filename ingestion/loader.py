from ingestion.github_loader import clone_repo
from ingestion.reader import read_codebase
from ingestion.zip_loader import extract_zip

def load_source(src_type, src_val):

    if(src_type == "local"):
        root_path = src_val
    elif(src_type == "github"):
        root_path = clone_repo(src_val)
    elif(src_type == "zip"):
        root_path = extract_zip(src_val)
    else:
        raise ValueError("Invalid source type")

    files = read_codebase(root_path)

    return files