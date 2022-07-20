from __future__ import print_function
import json
import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
import pandas as pd

data = pd.read_csv('aaa.csv', encoding='windows-1250', sep=';')

out = open('abc.csv', 'w')
out.write('name|descs|types\n')
service_url ='https://kgsearch.googleapis.com/v1/entities:search'
api_key = open('key.api_key').read()

for _, row in data.iterrows():

    query = row[0]
    print(query)
    params = {
        'query': query,
        'limit': 10,
        'indent': True,
        'key': api_key,
    }

    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())
    print(response)
    descs = []
    types = []
    for element in response['itemListElement']:
        try:
            descs.append(element['result']['description'])

            types += element['result']['@type']
        except Exception as e:
            #print('missing', e, '\nskipping...')
            pass
    try:
        sent = query + '|' + str(set(descs)) + '|' + str(set(types)) + '\n'
        out.write(sent)
    except Exception as e:
        #print(e, '\nskipping entity', query)
        pass

out.close()

data = pd.read_csv('abc.csv', encoding='windows-1250', sep='|')

html = data.to_html()

Html_file = open("wynik.html", "w")
Html_file.write(html)
Html_file.close()
