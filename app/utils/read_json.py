import json as j


def get_json(file_path: str):
    with open(file_path, 'rb') as f:
        return j.load(f)
