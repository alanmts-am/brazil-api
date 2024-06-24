from datetime import datetime


class Response:
    def __init__(self) -> None:
        pass

    def sucess(key: str, value: list) -> dict:
        dict = {}
        dict['status'] = 'OK'
        dict['datetime'] = datetime.now()
        dict[key] = value
        return dict

    def error(message: str) -> dict:
        dict = {}
        dict['status'] = 'ERROR'
        dict['datetime'] = datetime.now()
        dict['message'] = message
        return dict
