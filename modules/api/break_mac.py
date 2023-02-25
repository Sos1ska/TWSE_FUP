__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

my_name = 'break_mac'

from ..handlers.type_returns import Type
from ..handlers.exception import DataError, ParametersError, RequestsError
from ..handlers._pather import Pather
from requests import *
from bs4 import BeautifulSoup
from json import loads, load

class BreakMACAddress:
    def __init__(self, mode, mac, way=None, proxy=None):
        self.mode=mode
        self.mac=mac
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
            if self.proxy is not None : send_requests = get(f'https://api.2ip.ua/mac.json?mac={self.mac}', proxies=self.proxy)
            else : send_requests = get(f'https://api.2ip.ua/mac.json?mac={self.mac}')
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
                        Handler["company"],
                        Handler["address"],
                        Handler["block_size"]
                    )
                    create_file = Pather().__html__(self.way, data)
                    if create_file == True : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                    else : raise DataError("Error with dataa at creating file")
                else:
                    Handler = self.__sendrequest__()
                    return Type().__html__(
                        Handler["company"],
                        Handler["address"],
                        Handler["block_size"]
                    )
            case "JSON":
                if self.way is not None:
                    Handler = self.__sendrequest__()
                    data = Type().__json__(
                        Handler["company"],
                        Handler["address"],
                        Handler["block_size"]
                    )
                    create_file = Pather().__json__(self.way, data)
                    if create_file == True: 
                        if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                        elif ignore_msg == True : pass
                    else : raise DataError("Error with data at creating file")
                else:
                    Handler = self.__sendrequest__()
                    return Type().__json__(
                        Handler["company"],
                        Handler["address"],
                        Handler["block_size"]
                    )
            case "OnlyText":
                Handler = self.__sendrequest__()
                if type_return == "list":
                    return Type().__text__(
                        Handler["company"],
                        Handler["address"],
                        Handler["block_size"]
                    )
                elif type_return == "str":
                    answer = Type().__text__(
                        Handler["company"],
                        Handler["address"],
                        Handler["block_size"]
                    )
                    d = len(answer)
                    for i in range(0, d) : print(answer[i], end="\n")

class BreakMACAddress_modules:
    def __init__(self, mac, proxy=None, way="cache_mac.json"):
        BreakMACAddress(mode="JSON", mac=mac, way=way, proxy=proxy).main(ignore_msg=True)
    def Company(self):
        with open(r'cache_mac.json', 'r') as file_read : data = load(file_read)
        return data["1"]
    def Address(self):
        with open(r'cache_mac.json', 'r') as file_read : data = load(file_read)
        return data["2"]
    def Block_Size(self):
        with open(r'cache_mac.json', 'r') as file_read : data = load(file_read)
        return data["3"]
