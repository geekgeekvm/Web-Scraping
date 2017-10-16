import re
import urllib

symbollist = ["aapl","amzn", "goog","baba"]
i = 0
for symbol in symbollist:
    url = "http://finance.yahoo.com/q?s="+symbollist[i]+"&q1=1"
    hfile = urllib.urlopen(url)
    htext = hfile.read()

    regex = '<span id="yfs_l84_' + symbollist[i] + '">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htext)
    print price
    i+=1
