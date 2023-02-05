__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

my_name = 'break_number'

from ..Handlers.type_returns import Type
from ..Handlers.exception import DataError, ParametersError
from requests import *
from bs4 import BeautifulSoup
from json import loads

class BreakNumberPhone:
    def __init__(self, mode, number, way=None, autoprint=True or False, debug=True, proxy=None):
        self.mode=mode
        self.number=number
        self.autoprint=autoprint
        self.debug=debug
        self.way=way
        self.proxy=proxy
    def __checkproxy__(self):
        bad = 0
        true = 0
        try:
            send_request = get("http://ip-api.com/json")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            user_ip = Handler["query"]
            try:
                send_request_proxy = get("http://ip-api.com/json", proxies=self.proxy)
            except exceptions.ConnectionError:
                raise RequestsError("Not Found connection to internet")
            answer_proxy = send_request_proxy
            soup_json_proxy = BeautifulSoup(answer_proxy.text, "html.parser").text.strip()
            site_json_proxy = loads(soup_json_proxy)
            Handler_proxy = site_json_proxy
            user_ip_proxy = Handler_proxy["query"]
            match self.debug:
                case True : print(f'[ TWSE_FUP ] - [ user -> {user_ip}, proxy_user -> {user_ip_proxy} ]')
                case False : pass
            if user_ip == user_ip_proxy:
                bad = bad + 1
            else:
                true = true + 1
        except:
            raise DataError("Error work with data. Maybe not found connection to internet")
        finally:
            if bad == 1:
                return False
            elif true == 1:
                return True
    def __sendrequest__(self):
        try:
            if self.proxy is not None:
                match self.__checkproxy__():
                    case True:
                        pass
                    case False:
                        raise RequestsError("Proxy not working")
            if self.proxy is not None:
                send_requests = get(f'https://htmlweb.ru/json/mnp/phone/{self.number}', proxies=self.proxy)
            else:
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
