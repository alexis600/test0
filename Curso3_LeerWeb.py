import urllib2
import urllib

f = urllib2.urlopen('http://www.python.org')
f2 = urllib.urlopen('http://www.python.org')

print (f.read(200))
print (f2.read(200))

response = urllib.urlopen('http://google.com')
for line in response:
    pass
    print line.rstrip()