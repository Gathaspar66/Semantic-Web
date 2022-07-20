import requests
import pandas as pd

url = 'https://query.wikidata.org/sparql'
out = open('out.csv', 'w')
out.write('name; types\n')

with open('input.txt') as topo_file:
    for line in topo_file:
        print(line.split(' ', 1)[0])
        try:

            ent = line.split(' ', 1)[0].rstrip()
            query = '''
            SELECT ?itemLabel ?typeLabel
            WHERE {
            ?item rdfs:label \'''' + ent + '''\'@en;
                wdt:P31 ?type.
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
            }
            '''
            r = requests.get(url, params={'format': 'json', 'query': query})
            data = r.json()
            types = data['results']['bindings']
            vls = set([tp['typeLabel']['value'] for tp in types])
            sent = ent + ';' + str(vls) + '\n'
            out.write(sent)
        except Exception as e:
            print(e, '\n skipping result...')
            pass
out.close()

data = pd.read_csv('out.csv', encoding='windows-1250', sep=';')
html = data.to_html()
Html_file = open("HTML.html", "w")
Html_file.write(html)
Html_file.close()
