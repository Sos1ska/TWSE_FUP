# TWSE_FUP
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub contributors](https://img.shields.io/badge/GitHub%20Contributors-1-blue)

# Version
0.1

# Required
<code>requests</code><br>
<code>bs4</code><br>
<code>json</code><br>

The same as TWSE itself, only with the possibility of implementation in your program\script

# Parameters and arguments
<code>BreakIPAddress</code><br>
<code>mode</code> --- Sets the mode for the answer. <code>OnlyText</code> --- Gives only text. <code>FileAnswer</code> --- Gives the answer as a file. <code>HTML</code> --- Returns the response as an html file. <code>JSON</code> --- Returns the response as a json file<br>
<code>ip</code> --- The parameter is needed to set your ip<br>
<code>way</code> --- File path settings if specify mode as <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br>
<code>autoprint</code> --- Auto output to the console if mode is specified as <code>OnlyText</code><br>
<code>debug</code> --- Needed if the file is created and gives a response to the console if the value is <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br><br>

<code>BreakIPAddressMobile</code><br>
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
<code>number</code> --- The parameter is needed to set your ip<br>
<code>way</code> --- File path settings if specify mode as <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br>
<code>autoprint</code> --- Auto output to the console if mode is specified as <code>OnlyText</code><br>
<code>debug</code> --- Needed if the file is created and gives a response to the console if the value is <code>FileAnswer</code>, <code>HTML</code>, <code>JSON</code><br><br>

# How to use?
<code>from TWSE_FUP import BreakIPAddress</code><br>
<code>startwork = BreakIPAddress("OnlyText", "8.8.8.8", autoprint=True).__main__</code><br>
<code>startwork()</code><br>
<b>Example Answer</b><br>

                        Country    :::United States:::     

                        RegionName :::Virginia:::

                        City       :::Ashburn:::

                        AS         :::AS15169 Google LLC:::