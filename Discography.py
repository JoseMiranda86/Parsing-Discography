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