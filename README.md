# TWSE_FUP
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub contributors](https://img.shields.io/badge/GitHub%20Contributors-1-blue)

# Version
0.4

# Required
<code>requests</code><br>
<code>bs4</code><br>
<code>json</code><br>
<code>python 3.10+</code><br>

The same as TWSE itself, only with the possibility of implementation in your program\script

# Parameters and arguments
<code>BreakIPAddress</code><br>
<code>mode</code> --- Sets the mode for the answer. <code>OnlyText</code> --- Gives only text. <code>FileAnswer</code> --- Gives the answer as a file. <code>HTML</code> --- Returns the response as an html file. <code>JSON</code> --- Returns the response as a json file<br>
<code>ip</code> --- The parameter is needed to set your ip<br>
<code>way</code> --- File path settings if specify mode as <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br>
<code>autoprint</code> --- Auto output to the console if mode is specified as <code>OnlyText</code><br>
<code>debug</code> --- Needed if the file is created and gives a response to the console if the value is <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br><br>

<code>BreakMACAddress</code><br>
<code>mode</code> --- Sets the mode for the answer. <code>OnlyText</code> --- Gives only text. <code>FileAnswer</code> --- Gives the answer as a file. <code>HTML</code> --- Returns the response as an html file. <code>JSON</code> --- Returns the response as a json file<br>
<code>mac</code> --- The parameter is needed to set your mac<br>
<code>way</code> --- File path settings if specify mode as <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br>
<code>autoprint</code> --- Auto output to the console if mode is specified as <code>OnlyText</code><br>
<code>debug</code> --- Needed if the file is created and gives a response to the console if the value is <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br><br>

<code>BreakNumber</code><br>
<code>mode</code> --- Sets the mode for the answer. <code>OnlyText</code> --- Gives only text. <code>FileAnswer</code> --- Gives the answer as a file. <code>HTML</code> --- Returns the response as an html file. <code>JSON</code> --- Returns the response as a json file<br>
<code>number</code> --- The parameter is needed to set your number phone<br>
<code>way</code> --- File path settings if specify mode as <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br>
<code>autoprint</code> --- Auto output to the console if mode is specified as <code>OnlyText</code><br>
<code>debug</code> --- Needed if the file is created and gives a response to the console if the value is <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br><br>

# How to use?
<code>from TWSE_FUP import BreakIPAddress</code><br>
<code>BreakIPAddress("OnlyText", "8.8.8.8", autoprint=True).main("all")</code><br>
Answer Example:<br>
Continent        :::North America:::<br>
Country          :::United States:::<br>
Region           :::Virginia:::<br>
City             :::Ashburn:::<br>
Lat              :::39.03:::<br>
Lon              :::-77.5:::<br>
ISP              :::Google LLC:::<br>
ORG              :::Google Public DNS:::<br>
AS               :::AS15169 Google LLC:::<br>
ASName           :::GOOGLE:::<br>
Reverse          :::dns.google:::<br>
MobileConnection :::False:::<br>
ProxyConnection  :::False:::<br>
Hosting          :::True:::<br>


<b>Install</b>
1. Downloading the repository<br>
2. Unpack and put in a folder "Python/Python(3.10+)/Lib/site-packages"<br>
3. The End
