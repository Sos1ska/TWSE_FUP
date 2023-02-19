__structure__ = []

def __clear__():
    return __structure__.clear()

class Type:
    def _js_(self, info):
        d = len(info)
        if d == 1 : return {"1":info[0]}
        if d == 2 : return {"1":info[0], "2":info[1]}
        if d == 3 : return {"1":info[0], "2":info[1], "3":info[2]}
        if d == 4 : return {"1":info[0], "2":info[1], "3":info[2], "4":info[3]}
        if d == 5 : return {"1":info[0], "2":info[1], "3":info[2], "4":info[3], "5":info[4]}
        if d == 6 : return {"1":info[0], "2":info[1], "3":info[2], "4":info[3], "5":info[4], "6":info[5]}
        if d == 7 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6]}
        if d == 8 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6],"8":info[7]}
        if d == 9 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6],"8":info[7],"9":info[8]}
        if d == 10 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6],"8":info[7],"9":info[8],"10":info[9]}
        if d == 11 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6],"8":info[7],"9":info[8],"10":info[9],"11":info[10]}
        if d == 12 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6],"8":info[7],"9":info[8],"10":info[9],"11":info[10],"12":info[11]}
        if d == 13 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6],"8":info[7],"9":info[8],"10":info[9],"11":info[10],"12":info[11],"13":info[12]}
        if d == 14 : return {"1":info[0],"2":info[1],"3":info[2],"4":info[3],"5":info[4],"6":info[5],"7":info[6],"8":info[7],"9":info[8],"10":info[9],"11":info[10],"12":info[11],"13":info[12],"14":info[13]}
    def _html_(self, info):
        harvested_head = """<head>
    <title>TWSEConsoleFUP Break_IP services</title>
    <meta charset="utf-8">
</head>"""
        d = len(info)
        if d == 1 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
</body>"""
        if d == 2 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
</body>"""
        if d == 3 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
</body>"""
        if d == 4 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
</body>"""
        if d == 5 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
</body>"""
        if d == 6 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
</body>"""
        if d == 7 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
</body>"""
        if d == 8 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
    <div class="8">{info[7]}
    </div>
</body>"""
        if d == 9 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
    <div class="8">{info[7]}
    </div>
    <div class="9">{info[8]}
    </div>
</body>"""
        if d == 10 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
    <div class="8">{info[7]}
    </div>
    <div class="9">{info[8]}
    </div>
    <div class="10">{info[9]}
    </div>
</body>"""
        if d == 11 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
    <div class="8">{info[7]}
    </div>
    <div class="9">{info[8]}
    </div>
    <div class="10">{info[9]}
    </div>
    <div class="11">{info[10]}
    </div>
</body>"""
        if d == 12 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
    <div class="8">{info[7]}
    </div>
    <div class="9">{info[8]}
    </div>
    <div class="10">{info[9]}
    </div>
    <div class="11">{info[10]}
    </div>
    <div class="12">{info[11]}
    </div>
</body>"""
        if d == 13 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
    <div class="8">{info[7]}
    </div>
    <div class="9">{info[8]}
    </div>
    <div class="10">{info[9]}
    </div>
    <div class="11">{info[10]}
    </div>
    <div class="12">{info[11]}
    </div>
    <div class="13">{info[12]}
    </div>
</body>"""
        if d == 14 : return f"""{harvested_head}
<body>
    <div class="1">{info[0]}
    </div>
    <div class="2">{info[1]}
    </div>
    <div class="3">{info[2]}
    </div>
    <div class="4">{info[3]}
    </div>
    <div class="5">{info[4]}
    </div>
    <div class="6">{info[5]}
    </div>
    <div class="7">{info[6]}
    </div>
    <div class="8">{info[7]}
    </div>
    <div class="9">{info[8]}
    </div>
    <div class="10">{info[9]}
    </div>
    <div class="11">{info[10]}
    </div>
    <div class="12">{info[11]}
    </div>
    <div class="13">{info[12]}
    </div>
    <div class="14">{info[13]}
    </div>
</body>"""
    def __init__(self) : pass
    def __text__(self, *info):
        try : __clear__()
        except : pass
        try:
            for frames in range(0, 14) : __structure__.append(":::%s:::" % (info[frames]))
        except IndexError : pass
        finally : return __structure__
    def __json__(self, *info):
        try : __clear__()
        except : pass
        try:
            for frames in range(0, 14) : __structure__.append(info[frames])
        except IndexError : pass
        finally: 
            return self._js_(__structure__)
    def __html__(self, *info):
        try : __clear__()
        except : pass
        try:
            for frames in range(0, 14) : __structure__.append(info[frames])
        except IndexError : pass
        finally:
            return self._html_(__structure__)
