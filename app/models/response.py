from datetime import datetime
from app.interface.response_interface import IResponse


class Response(IResponse):
    def __init__(self) -> None:
        pass

    def sucess(self, value: list[dict]) -> dict:
        dict = {}
        dict['status'] = 'OK'
        dict['datetime'] = datetime.now()
        dict['count'] = len(value)
        dict['data'] = value
        return dict

    def error(self, message: str) -> dict:
        dict = {}
        dict['status'] = 'ERROR'
        dict['datetime'] = datetime.now()
        dict['message'] = message
        return dict
