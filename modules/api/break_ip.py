__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

my_name = 'break_ip'

__services__ = ["htmlweb", "ip-api", "2ip"]

from ..handlers.type_returns import Type
from ..handlers.exception import DataError, ParametersError, RequestsError
from ..handlers._pather import Pather
from requests import *
from bs4 import BeautifulSoup
from json import loads, load

class BreakIPAddress:
    def __init__(self, mode, ip, way=None, proxy=None, service=__services__[1]):
        self.mode=mode
        self.ip=ip
        self.way=way
        self.proxy=proxy
        self.service=service
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
        match self.service:
            case "ip-api":
                try:
                    if self.proxy is not None:
                        match self.__checkproxy__():
                            case True : pass
                            case False : raise RequestsError("Proxy not working")
                    if self.proxy is not None : send_requests = get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting', proxies=self.proxy)
                    else : send_requests = get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting')
                    answer = send_requests
                    soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = loads(soup_json)
                    Handler = site_json
                except : raise DataError("Error work with data. Maybe not found connection to internet")
                finally : return Handler
            case "htmlweb":
                try:
                    if self.proxy is not None:
                        match self.__checkproxy__():
                            case True : pass
                            case False : raise RequestsError("Porxy not working")
                    if self.proxy is not None : send_requests = get(f"https://htmlweb.ru/geo/api.php?json&ip={self.ip}", proxies=self.proxy)
                    else : send_requests = get(f"https://htmlweb.ru/geo/api.php?json&ip={self.ip}")
                    answer = send_requests
                    soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = loads(soup_json)
                    Handler = site_json
                except : raise DataError("Error work with data. Maybe not found connection to internet")
                finally : return Handler
            case "2ip":
                try:
                    if self.proxy is not None:
                        match self.__checkproxy__():
                            case True : pass
                            case False : raise RequestsError("Porxy not working")
                    if self.proxy is not None : send_requests = get(f"https://api.2ip.ua/geo.json?ip={self.ip}", proxies=self.proxy)
                    else : send_requests = get(f"https://api.2ip.ua/geo.json?ip={self.ip}")
                    answer = send_requests
                    soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = loads(soup_json)
                    Handler = site_json
                except : raise DataError("Error work with data. Maybe not found connection to internet")
                finally :  return Handler

    def main(self, type_return="list", ignore_msg=False):
        match self.service:
            case "ip-api":
                match self.mode:
                    case "HTML":
                        if self.way is not None:
                            Handler = self.__sendrequest__()
                            data = Type().__html__(
                                Handler["continent"], 
                                Handler["country"], 
                                Handler["regionName"], 
                                Handler["city"], 
                                Handler["lat"], 
                                Handler["lon"], 
                                Handler["isp"], 
                                Handler["org"], 
                                Handler["as"], 
                                Handler["asname"],
                                Handler["reverse"], 
                                Handler["mobile"], 
                                Handler["proxy"], 
                                Handler["hosting"]
                            )
                            create_file = Pather().__html__(self.way, data) 
                            if create_file == True: 
                                if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                                elif ignore_msg == True : pass
                            else : raise DataError("Error with data at creating file")
                        else:
                            Handler = self.__sendrequest__()
                            return Type().__html__(
                                Handler["continent"], 
                                Handler["country"], 
                                Handler["regionName"], 
                                Handler["city"], 
                                Handler["lat"], 
                                Handler["lon"], 
                                Handler["isp"], 
                                Handler["org"], 
                                Handler["as"], 
                                Handler["asname"], 
                                Handler["reverse"], 
                                Handler["mobile"], 
                                Handler["proxy"], 
                                Handler["hosting"]
                            )
                    case "JSON":
                        if self.way is not None:
                            Handler = self.__sendrequest__()
                            data = Type().__json__(
                                Handler["continent"], 
                                Handler["country"], 
                                Handler["regionName"], 
                                Handler["city"], 
                                Handler["lat"], 
                                Handler["lon"], 
                                Handler["isp"], 
                                Handler["org"], 
                                Handler["as"], 
                                Handler["asname"], 
                                Handler["reverse"], 
                                Handler["mobile"], 
                                Handler["proxy"], 
                                Handler["hosting"]
                            )
                            create_file = Pather().__json__(self.way, data)
                            if create_file == True:
                                if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                                elif ignore_msg == True : pass
                            else : raise DataError("Error with data at creating file")
                        else:
                            Handler = self.__sendrequest__()
                            return Type().__json__(
                                Handler["continent"], 
                                Handler["country"], 
                                Handler["regionName"], 
                                Handler["city"], 
                                Handler["lat"], 
                                Handler["lon"], 
                                Handler["isp"], 
                                Handler["org"], 
                                Handler["as"], 
                                Handler["asname"], 
                                Handler["reverse"], 
                                Handler["mobile"],
                                Handler["proxy"], 
                                Handler["hosting"]
                            )
                    case "OnlyText":
                        Handler = self.__sendrequest__()
                        if type_return == "list":
                            return Type().__text__(
                                Handler["continent"], 
                                Handler["country"], 
                                Handler["regionName"], 
                                Handler["city"], 
                                Handler["lat"], 
                                Handler["lon"], 
                                Handler["isp"], 
                                Handler["org"], 
                                Handler["as"], 
                                Handler["asname"], 
                                Handler["reverse"], 
                                Handler["mobile"], 
                                Handler["proxy"], 
                                Handler["hosting"]
                            )
                        elif type_return == "str":
                            answer = Type().__text__(
                                Handler["continent"], 
                                Handler["country"], 
                                Handler["regionName"], 
                                Handler["city"], 
                                Handler["lat"], 
                                Handler["lon"], 
                                Handler["isp"], 
                                Handler["org"], 
                                Handler["as"], 
                                Handler["asname"], 
                                Handler["reverse"], 
                                Handler["mobile"], 
                                Handler["proxy"], 
                                Handler["hosting"]
                            )
                            d = len(answer)
                            for i in range(0, d) : print(answer[i], end="\n")
            case "htmlweb":
                match self.mode:
                    case "HTML":
                        if self.way is not None:
                            Handler = self.__sendrequest__()
                            data = Type().__html__(
                                Handler["country"]["english"], 
                                Handler["country"]["iso"], 
                                Handler["country"]["mcc"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["english"], 
                                Handler["rajon"]["english"], 
                                Handler["city_english"], 
                                Handler["city_telcod"], 
                                Handler["iso"], 
                                Handler["level"], 
                                Handler["country_telcod"]
                            )
                            create_file = Pather().__html__(self.way, data)
                            if create_file == True:
                                if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                                elif ignore_msg == True : pass
                            else : raise DataError("Error with data at creating file")
                        else:
                            Handler = self.__sendrequest__()
                            return Type().__html__(
                                Handler["country"]["english"], 
                                Handler["country"]["iso"], 
                                Handler["country"]["mcc"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["english"], 
                                Handler["rajon"]["english"], 
                                Handler["city_english"], 
                                Handler["city_telcod"], 
                                Handler["iso"], 
                                Handler["level"], 
                                Handler["country_telcod"]
                            )
                    case "JSON":
                        if self.way is not None:
                            Handler = self.__sendrequest__()
                            data = Type().__json__(
                                Handler["country"]["english"], 
                                Handler["country"]["iso"], 
                                Handler["country"]["mcc"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["english"], 
                                Handler["rajon"]["english"], 
                                Handler["city_english"], 
                                Handler["city_telcod"], 
                                Handler["iso"], 
                                Handler["level"], 
                                Handler["country_telcod"]
                            )
                            create_file = Pather().__json__(self.way, data)
                            if create_file == True:
                                if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                                elif ignore_msg == True : pass
                            else : raise DataError("Error with data at creating file")
                        else:
                            Handler = self.__sendrequest__()
                            return Type().__json__(
                                Handler["country"]["english"], 
                                Handler["country"]["iso"], 
                                Handler["country"]["mcc"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["english"], 
                                Handler["rajon"]["english"], 
                                Handler["city_english"], 
                                Handler["city_telcod"], 
                                Handler["iso"], 
                                Handler["level"], 
                                Handler["country_telcod"]
                            )
                    case "OnlyText":
                        Handler = self.__sendrequest__()
                        if type_return == "list":
                            return Type().__text__(
                                Handler["country"]["english"], 
                                Handler["country"]["iso"], 
                                Handler["country"]["mcc"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["english"], 
                                Handler["rajon"]["english"], 
                                Handler["city_english"], 
                                Handler["city_telcod"], 
                                Handler["iso"], 
                                Handler["level"], 
                                Handler["country_telcod"]
                            )
                        elif type_return == "str":
                            answer = Type().__text__(
                                Handler["country"]["english"], 
                                Handler["country"]["iso"], 
                                Handler["country"]["mcc"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["capital"], 
                                Handler["region"]["english"], 
                                Handler["rajon"]["english"], 
                                Handler["city_english"], 
                                Handler["city_telcod"], 
                                Handler["iso"], 
                                Handler["level"], 
                                Handler["country_telcod"]
                            )
                            d = len(answer)
                            for i in range(0, d) : print(answer[i], end="\n")
            case "2ip":
                match self.mode:
                    case "HTML":
                        if self.way is not None:
                            Handler = self.__sendrequest__()
                            data = Type().__html__(
                                Handler["country"],
                                Handler["city"],
                                Handler["latitude"],
                                Handler["longitude"],
                                Handler["zip_code"]
                            )
                            create_file = Pather().__html__(self.way, data)
                            if create_file == True:
                                if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                                elif ignore_msg == True : pass
                            else : raise DataError("Error with data at creating file")
                        else:
                            Handler = self.__sendrequest__()
                            return Type().__html__(
                                Handler["country"],
                                Handler["city"],
                                Handler["latitude"],
                                Handler["longitude"],
                                Handler["zip_code"]
                            )
                    case "JSON":
                        if self.way is not None:
                            Handler = self.__sendrequest__()
                            data = Type().__json__(
                                Handler["country"],
                                Handler["city"],
                                Handler["latitude"],
                                Handler["longitude"],
                                Handler["zip_code"]
                            )
                            create_file = Pather().__json__(self.way, data)
                            if create_file == True:
                                if ignore_msg == False : print(f'[ TWSE_FUP ] - [ File created -> {self.way} ]')
                                elif ignore_msg == True : pass
                            else : raise DataError("Error with data at creating file")
                        else:
                            Handler = self.__sendrequest__()
                            return Type().__json__(
                                Handler["country"],
                                Handler["city"],
                                Handler["latitude"],
                                Handler["longitude"],
                                Handler["zip_code"]
                            )
                    case "OnlyText":
                        Handler = self.__sendrequest__()
                        if type_return == "list":
                            return Type().__text__(
                                Handler["country"],
                                Handler["city"],
                                Handler["latitude"],
                                Handler["longitude"],
                                Handler["zip_code"]
                            )
                        elif type_return == "str":
                            answer = Type().__text__(
                                Handler["country"],
                                Handler["city"],
                                Handler["latitude"],
                                Handler["longitude"],
                                Handler["zip_code"]
                            )
                            d = len(answer)
                            for i in range(0, d) : print(answer[i], end="\n")

class BreakIPAddress_modules:
    def __init__(self, ip, proxy=None, way="cache_ip.json"):
        BreakIPAddress(mode="JSON", ip=ip, way=way, proxy=proxy, service="ip-api").main(ignore_msg=True)
    def Continent(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["1"]
    def Country(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["2"]
    def RegionName(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["3"]
    def City(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["4"]
    def Latitude(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["5"]
    def Longtitude(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["6"]
    def ISP(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["7"]
    def Org(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["8"]
    def AS(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["9"]
    def ASName(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["10"]
    def Reverse(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["11"]
    def MobileConnection(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["12"]
    def ProxyConnection(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["13"]
    def Hosting(self):
        with open('cache_ip.json', 'r') as file_read : data=load(file_read)
        return data["14"]
