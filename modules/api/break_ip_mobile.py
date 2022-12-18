my_name_file = "break_ip_mobile"

from ..Handlers.exceptions import ImportErrorTWSE, FileErrorTWSE, NotFoundParameters, Base

try : from requests import get
except ImportError : raise ImportErrorTWSE(f'[ {my_name_file} ] - [ Install lib "requests" ]')
try : from bs4 import BeautifulSoup
except ImportError : raise ImportErrorTWSE(f'[ {my_name_file} ] - [ Install lib "bs4" ]')

from json import loads, dump
import datetime

class Constructor:
    def __file__(self, country, iso, telcod, capital, mcc):
        data_for_out = f"""[{str(datetime.datetime.now().date())}]
Country={country}
ISO{iso}
TelCod{telcod}
Capital{capital}
MCC{mcc}"""
        return data_for_out
    def __text__(self, country, iso, telcod, capital, mcc):
        data_for_out = f"""
\t\t\tCountry :::{country}:::\n
\t\t\tISO     :::{iso}:::\n
\t\t\tTelCod  :::{telcod}:::\n
\t\t\tCapital :::{capital}:::\n
\t\t\tMCC     :::{mcc}:::"""
        return data_for_out
    def __html__(self, country, iso, telcod, capital, mcc):
        html = f"""<!DOCTYPE html>
<head>
    <title>TWSEConsoleFUP 0.1</title>
</head>
<body>
    <div class="Country">{country}
    </div>
    <div class="ISO">{iso}
    </div>
    <div class="TelCod">{telcod}
    </div>
    <div class="Capital">{capital}
    </div>
    <div class="MCC">{mcc}
    </div>
</body>
"""
        return html
    def __json__(self, country, iso, telcod, capital, mcc):
        jsona = {
            "Country": f"{country}",
            "ISO": f"{iso}",
            "TelCod": f"{telcod}",
            "Capital": f"{capital}",
            "MCC": f"{mcc}"
        }
        return jsona

class BreakIPAddressMobile(Constructor):
    my_name_class = "BreakIPAddressMobile"

    way = ""
    mode = ""
    ip = ""
    autoprint = ""
    debug = ""

    modelist = ["FileAnswer", "OnlyText", "HTML", "JSON"]
    speclist = ["FileAnswer", "HTML", "JSON"]

    def __init__(self, mode, ip=bytes, way=None, autoprint=True or False, debug=True or False):
        """`mode` - Sets the mode for the answer.
        There are 4 in total -> "FileAnswer", "OnlyText", "HTML", "JSON".
        
        `way` - Sets the path to a file and create him.
        There are 3 in total -> "FileAnswer", "HTML", "JSON".
        
        `autoprint` - Sets the auto print the answer.
        There are 1 in total -> "OnlyText".
        
        `debug` - Sets debug answer.
        There are 3 in total -> "FileAnswer", "HTML", "JSON".
        
        `FileAnswer` - Creates a file with a construction from a file with the ini extension, which allows it to be parsed if necessary.
        
        `OnlyText` - Outputs the answer as text. With autoprint allows you to automatically output to the console or transfer data.
        
        `HTML` - Creates a file with the html extension, will create a lighter one, because will allow it to be quickly parsed or simply output for the server.
        
        `JSON` - Creates a file with the json extension, will create an easier one, because will allow it to be quickly parsed or simply output for the server"""
        self.mode=mode
        self.ip=ip
        self.autoprint=autoprint
        self.debug=debug
        if mode in self.modelist:
            if mode in self.speclist:
                if way == None or way == "" or way == " " : raise Base(f'[ {my_name_file}.{self.my_name_class} ] - [ Way ust be mandatory for "FileAnswer", "HTML", "JSON"! Your mode -> {mode} ]')
                else : self.way=way
        else : raise NotFoundParameters(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found Parameters -> {mode} ]')

    def main(self):
        if self.mode == "OnlyText":
            send_requests = get(f'https://htmlweb.ru/geo/api.php?ip={self.ip}&json')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            if self.autoprint == True or self.autoprint == "True" : print(
                super().__text__(Handler["country"]["name"], Handler["country"]["iso"], Handler["country"]["telcod"], Handler["country"]["capital"], Handler["country"]["mcc"])
            )
            elif self.autoprint == False or self.autoprint == "False" : super().__text__(Handler["country"]["name"], Handler["country"]["iso"], Handler["country"]["telcod"], Handler["country"]["capital"], Handler["country"]["mcc"])
            else : raise NotFoundParameters(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found Parameters -> {self.autoprint} ]')
        elif self.mode == "FileAnswer":
            send_requests = get(f'https://htmlweb.ru/geo/api.php?ip={self.ip}&json')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : file.write(super().__file__(Handler["country"]["name"], Handler["country"]["iso"], Handler["country"]["telcod"], Handler["country"]["capital"], Handler["country"]["mcc"])), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "HTML":
            send_requests = get(f'https://htmlweb.ru/geo/api.php?ip={self.ip}&json')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : file.write(super().__html__(Handler["country"]["name"], Handler["country"]["iso"], Handler["country"]["telcod"], Handler["country"]["capital"], Handler["country"]["mcc"])), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "JSON":
            send_requests = get(f'https://htmlweb.ru/geo/api.php?ip={self.ip}&json')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : dump(super().__json__(Handler["country"]["name"], Handler["country"]["iso"], Handler["country"]["telcod"], Handler["country"]["capital"], Handler["country"]["mcc"]), file), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
