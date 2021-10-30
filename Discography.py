import urllib.request, urllib.parse, urllib.error
import json
import ssl
import webbrowser
index = 0
Signal = 0

NAME0 = input('\nPlease provide the name of the band/singer:')

NaLi = NAME0.split(" ")
if len(NaLi) == 2:
    NAME = str.capitalize(NaLi[0])+"_"+str.capitalize(NaLi[1])
    NAME0 = (NaLi[0])+"_"+(NaLi[1])
elif len(NaLi) == 3:
    NAME = str.capitalize(NaLi[0])+"_"+str.capitalize(NaLi[1])+"_"+str.capitalize(NaLi[2])
    NAME0 = (NaLi[0])+"_"+(NaLi[1])+"_"+(NaLi[2])
else:
    NAME = NAME0[0].upper()+NAME0[1:len(NAME0)]

serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NAME+'&prop=sections&disabletoc=1'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(serviceurl1, context=ctx)

data1 = uh.read().decode()
js1 = json.loads(data1)

try:
    SectionIndex = js1['parse']['sections']
    for element in SectionIndex:
        for a, b in element.items():
            if b == 'Discography':
                index = element['index']
except:
    index = 0
