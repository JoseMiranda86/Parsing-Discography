import urllib.request, urllib.parse, urllib.error
import json
import ssl
import webbrowser
index = 0
Signal = 0

NameArtist = input('\nPlease provide the name of the band/singer:')

NameArtistList = NameArtist.split(" ")
if len(NameArtistList) == 2:
    NameURL = str.capitalize(NameArtistList[0])+"_"+str.capitalize(NameArtistList[1])
    NameArtist = (NameArtistList[0])+"_"+(NameArtistList[1])
elif len(NameArtistList) == 3:
    NameURL = str.capitalize(NameArtistList[0])+"_"+str.capitalize(NameArtistList[1])+"_"+str.capitalize(NameArtistList[2])
    NameArtist = (NameArtistList[0])+"_"+(NameArtistList[1])+"_"+(NameArtistList[2])
else:
    NameURL = NameArtist[0].upper()+NameArtist[1:len(NameArtist)]

ServiceURL = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'&prop=sections&disabletoc=1'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(ServiceURL, context=ctx)

Data1 = uh.read().decode()
Jason1 = json.loads(Data1)

try:
    SectionIndex = Jason1['parse']['sections']
    for element in SectionIndex:
        for a, b in element.items():
            if b == 'Discography':
                index = element['index']
except:
    index = 0

if index == 0:
    ServiceURL = 'https://es.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(ServiceURL, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Discografía':
                    index = element['index']
                    Signal = -2
    except:
        index = 0

if index == 0:
    ServiceURL = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(ServiceURL, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Discography':
                    index = element['index']
                    Signal = -1
    except:
        index = 0   

if index == 0:
    serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(band)'+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(ServiceURL, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Discography':
                    index = element['index']
                    Signal = 1
    except:
        index = 0           

if index == 0:
    serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(singer)'+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(serviceurl1, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Discography':
                    index = element['index']
                    Signal = 2
    except:
        index = 0      

if index == 0:
    serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(musician)'+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(serviceurl1, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Discography':
                    index = element['index']
                    Signal = 3
    except:
        index = 0

if index == 0:
    NAME1 = NameURL.upper()
    serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NAME1+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(serviceurl1, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)
    for x,y in Jason1.items():
        if x == 'error':
            print('\nName could not been found')
            exit()

    SectionIndex = Jason1['parse']['sections']
    for element in SectionIndex:
        for a, b in element.items():
            if b == 'Discography':
                index = element['index']
                Signal = 4
    if len(SectionIndex) < 1:
            print('\nName could not been found')
            exit()

if Signal == -2:
    serviceurl2 = 'https://es.wikipedia.org/w/api.php?action=parse&format=json&page='+NAME+'&prop=wikitext&section='+str(index)+'&disabletoc=1'
elif Signal == -1:
    serviceurl2 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NAME1+'&prop=wikitext&section='+str(index)+'&disabletoc=1'
elif Signal == 0:
    serviceurl2 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'&prop=wikitext&section='+str(index)+'&disabletoc=1'
    #serviceurl2 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'&prop=text&section='+index+'&disabletoc=1'
elif Signal == 1:
    serviceurl2 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(band)'+'&prop=wikitext&section='+index+'&disabletoc=1'
elif Signal == 2:
    serviceurl2 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(singer)'+'&prop=wikitext&section='+index+'&disabletoc=1'
elif Signal == 3:
    serviceurl2 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(musician)'+'&prop=wikitext&section='+index+'&disabletoc=1'
else:
    serviceurl2 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NAME1+'&prop=wikitext&section='+index+'&disabletoc=1'

uh2 = urllib.request.urlopen(serviceurl2, context=ctx)
data2 = uh2.read().decode()
Jason2 = json.loads(data2)

#print(js1)
#print('\n')
#print(js2)
print('\n')

SectionIndex2 = Jason2['parse']['wikitext']
#print('\n',SectionIndex2['*'])
x = SectionIndex2['*']
list = x.split("*")
list2 = list[0].split('\n')
#print(list2)
