from datetime import datetime


class Response:
    def __init__(self) -> None:
        pass

    def base_response(self, status: str):
        return {'status': status, 'datetime': datetime.now()}

    def sucess(self, key: str, value: list, extra_dict: dict = {}) -> dict:
        dict = self.base_response('OK')
        dict['count'] = len(value)
        if extra_dict != {}:
            for _key, _value in extra_dict.items():
                dict[_key] = _value
        dict[key] = value
        return dict

    def error(self, message: str) -> dict:
        dict = self.base_response('ERROR')
        dict['message'] = message
        return dict
