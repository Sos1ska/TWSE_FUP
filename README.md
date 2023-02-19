# TWSE_FUP
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub contributors](https://img.shields.io/badge/GitHub%20Contributors-1-blue)

# Version
1.0

# Required
<code>requests</code><br>
<code>bs4</code><br>
<code>json</code><br>
<code>python 3.10+</code><br>

# Parameters
<code>ip, number, mac</code> - Задаются данные которые хотите получить<br>
<code>mode</code> - Передаётся режим работы. Есть 3 режима<br>
<pre><code>OnlyText</code> - Ну тут логично, только текст, но требует ещё один аргумент в модуле main, это <code>type_return</code></pre><br>
<pre><code>type_return</code> - Принимает <code>list</code> - вернёт ответ в виде массива, но не будет выводить в консоль<br>Принимает последний вариант, это <code>str</code></pre><br>
<code>proxy</code> - Принимает данные об прокси сервера, то есть отправит запрос через него<br>
<code>way</code> - Нужен при создании файла<br>

# Parameters _modules
<code>ip, number, mac</code> - Также задаются данные которые хотите получить<br>
<code>proxy</code> - Принимает данные об прокси сервера, то есть отправит запрос через него<br>

<h1>Get data</h1><br>
Для <code>BreakIPAddress_modules</code> это<br>
<pre>Continent
Country
RegionName
City
Latitude
Longtitude
ISP
Org
AS
ASName
Reverse
MobileConnection
ProxyConnection
Hosting</pre><br>
ВНИМАНИЕ! - они всего лишь возвращают данные которые хотите получить, вам их надо выводить<br>

Для <code>BreakMACAddress_modules</code> это <br>
<pre>Company
Address
Block_Size</pre><br>

Для <code>BreakNumberPhone_modules</code> это<br>
<pre>OperName
OperMNC
OperBrand
OperINN
MobileWorker
RegionName</pre><br>

<h1>Example</h1>
<code>from TWSE_FUP import BreakIPAddress_modules<br>
work = BreakIPAddress_modules(ip="8.8.8.8")
print("Continent", work.Continent())</code><br><br>
<code>from TWSE_FUP import BreakIPAddress<br>
print(BreakIPAddress(mode="OnlyText", ip="8.8.8.8").main(type_return="str")</code><br>
И так с другими модулями

# Groups
VK : https://vk.com/twse_newsoffc<br>
