__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

my_name = 'break_number'

from ..handlers.type_returns import Type
from ..handlers.exception import DataError, ParametersError
from requests import get
from bs4 import BeautifulSoup
from json import loads

class BreakNumberPhone:
    def __init__(self, mode, number, way=None, autoprint=True or False, debug=True):
        self.mode=mode
        self.number=number
        self.autoprint=autoprint
        self.debug=debug
        self.way=way
    def __sendrequest__(self):
        try:
            send_requests = get(f'https://htmlweb.ru/json/mnp/phone/{self.number}')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
        except:
            raise DataError("Error work with data. Maybe not found connection to internet")
        finally:
            return Handler
    def main(self, _answer="all", view="ini", _mode="w"):
        match self.mode:
            case "HTML":
                Handler = self.__sendrequest__()
                Type(self.debug).__html__(my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], path=self.way)
            case "OnlyText":
                Handler = self.__sendrequest__()
                match self.autoprint:
                    case True:
                        print(Type(self.debug).__text__(my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], _answer=_answer))
                    case False:
                        Type(self.debug).__text__(my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], _answer=_answer)
            case "JSON":
                Handler = self.__sendrequest__()
                Type(self.debug).__json__(my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], path=self.way)
            case "FileAnswer":
                Handler = self.__sendrequest__()
                Type(self.debug).__file__(my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], path=self.way, view=view, _mode=_mode)
            case _:
                raise ParametersError(f"Not found parameters -> {self.mode}. [\"HTML\", \"OnlyText\", \"JSON\", \"FileAnswer\"]")
