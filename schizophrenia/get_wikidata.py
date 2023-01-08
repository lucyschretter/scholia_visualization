import requests


# Set the SPARQL query that you want to execute
query = '''
PREFIX target: <http://www.wikidata.org/entity/Q41112>

SELECT
  DISTINCT
  ?start_date
  ?trial ?trialLabel
  ?intervention ?interventionLabel
  ?sponsor ?sponsorLabel
WHERE {
  ?trial wdt:P31 wd:Q30612 ;
  wdt:P1050 / wdt:P279* target: .
  OPTIONAL {
    ?trial wdt:P580 ?starttime
    BIND(SUBSTR(STR(?starttime), 0, 11) AS ?start_date)
  }
  OPTIONAL { ?trial wdt:P4844 ?intervention }
  OPTIONAL { ?trial wdt:P859 ?sponsor }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,pl,ru,sv,zh". }
}
ORDER BY DESC(?starttime)
'''

# Use the 'sparql' action to execute the query
url = 'https://query.wikidata.org/sparql'
params = {
    'format': 'json',
    'query': query
}
response = requests.get(url, params=params).json()

# Print the results of the query
# print(response['results']['bindings'])
# print(response)
for key, value in response.items():
    print(key)
    for a, b in value.items():
        print(a)
        print(b)

    # print(value)
