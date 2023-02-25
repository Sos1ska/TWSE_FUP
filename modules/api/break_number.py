__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

my_name = 'break_number'

from ..handlers.type_returns import Type
from ..handlers.exception import DataError, ParametersError, RequestsError
from ..handlers._pather import Pather
from requests import *
from bs4 import BeautifulSoup
from json import loads, load

class BreakNumberPhone:
    def __init__(self, mode, number, way=None, proxy=None):
        self.mode=mode
        self.number=number
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
            try : send_request_proxy = get("http://ip-api.com/json", proxies=self.proxy)
            except exceptions.ConnectionError : raise RequestsError("Not Found connection to internet")
            answer_proxy = send_request_proxy
            soup_json_proxy = BeautifulSoup(answer_proxy.text, "html.parser").text.strip()
            site_json_proxy = loads(soup_json_proxy)
            Handler_proxy = site_json_proxy
            user_ip_proxy = Handler_proxy["query"]
            if user_ip == user_ip_proxy : bad = bad + 1
            else : true = true + 1
        except : raise DataError("Error work with data. Maybe not found connection to internet")
        finally:
            if bad == 1 : return False
            elif true == 1 : return True
    def __sendrequest__(self):
        try:
            if self.proxy is not None:
                match self.__checkproxy__():
                    case True : pass
                    case False : raise RequestsError("Proxy not working")
            if self.proxy is not None : send_requests = get(f'https://htmlweb.ru/json/mnp/phone/{self.number}', proxies=self.proxy)
            else : send_requests = get(f'https://htmlweb.ru/json/mnp/phone/{self.number}')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
        except : raise DataError("Error work with data. Maybe not found connection to internet")
        finally : return Handler
    def main(self, type_return="list", ignore_msg=False):
        match self.mode:
            case "HTML":
                if self.way is not None:
                    Handler = self.__sendrequest__()
                    data = Type().__html__(
                        Handler["oper"]["name"],
                        Handler["oper"]["mnc"],
                        Handler["oper"]["brand"],
                        Handler["oper"]["inn"],
                        Handler["mobile"],
                        Handler["region"]["name"]
                    )
                    create_file = Pather().__html__(self.way, data)
                    if create_file == True:
                        if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                        elif ignore_msg == True : pass
                    else : raise DataError("Error with data at creating file")
                else:
                    Handler = self.__sendrequest__()
                    return Type().__html__(
                        Handler["oper"]["name"],
                        Handler["oper"]["mnc"],
                        Handler["oper"]["brand"],
                        Handler["oper"]["inn"],
                        Handler["mobile"],
                        Handler["region"]["name"]
                    )
            case "JSON":
                if self.way is not None:
                    Handler = self.__sendrequest__()
                    data = Type().__json__(
                        Handler["oper"]["name"],
                        Handler["oper"]["mnc"],
                        Handler["oper"]["brand"],
                        Handler["oper"]["inn"],
                        Handler["mobile"],
                        Handler["region"]["name"]
                    )
                    create_file = Pather().__json__(self.way, data)
                    if create_file == True:
                        if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                        elif ignore_msg == True : pass
                    else : raise DataError("Error with data at creating file")
                else:
                    Handler = self.__sendrequest__()
                    return Type().__json__(
                        Handler["oper"]["name"],
                        Handler["oper"]["mnc"],
                        Handler["oper"]["brand"],
                        Handler["oper"]["inn"],
                        Handler["mobile"],
                        Handler["region"]["name"]
                    )
            case "OnlyText":
                Handler = self.__sendrequest__()
                if type_return == "list":
                    return Type().__text__(
                        Handler["oper"]["name"],
                        Handler["oper"]["mnc"],
                        Handler["oper"]["brand"],
                        Handler["oper"]["inn"],
                        Handler["mobile"],
                        Handler["region"]["name"]
                    )
                elif type_return == "str":
                    answer = Type().__text__(
                        Handler["oper"]["name"],
                        Handler["oper"]["mnc"],
                        Handler["oper"]["brand"],
                        Handler["oper"]["inn"],
                        Handler["mobile"],
                        Handler["region"]["name"]
                    )
                    d = len(answer)
                    for i in range(0, d) : print(answer[i], end="\n")

class BreakNumberPhone_modules:
    def __init__(self, number, proxy=None, way="cache_number_phone.json"):
        self.way=way
        BreakNumberPhone(mode="JSON", number=number, way=way, proxy=proxy).main(ignore_msg=True)
    def OperName(self):
        with open(self.way, 'r') as file_read : data=load(file_read)
        return data["1"]
    def OperMNC(self):
        with open(self.way, 'r') as file_read : data=load(file_read)
        return data["2"]
    def OperBrand(self):
        with open(self.way, 'r') as file_read : data=load(file_read)
        return data["3"]
    def OperINN(self):
        with open(self.way, 'r') as file_read : data=load(file_read)
        return data["4"]
    def MobileWorker(self):
        with open(self.way, 'r') as file_read : data=load(file_read)
        return data["5"]
    def RegionName(self):
        with open(self.way, 'r') as file_read : data=load(file_read)
        return data["6"]
