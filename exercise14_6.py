import urllib

com = urllib.urlopen('http://thinkpython.com/secret.html')
for line in com:
    print line.strip()