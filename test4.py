
import requests

# SPARQL-Abfrage als String
query = """
SELECT ?country ?countryLabel ?population WHERE {
  ?country wdt:P31 wd:Q6256;
          wdt:P1082 ?population.
  ?country rdfs:label ?countryLabel.
  
  FILTER(?population > 50000000)
  
  FILTER(LANG(?countryLabel) = "en")
}
ORDER BY DESC(?population)
"""

# URL des Wikidata Query Service
url = "https://query.wikidata.org/sparql"

# HTTP-GET-Anfrage senden
response = requests.get(url, params={'query': query, 'format': 'json'})

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # JSON-Antwort parsen
    data = response.json()
    
    # Ergebnisse extrahieren und in eine Liste umwandeln
    results = []
    for item in data['results']['bindings']: #Iteration über jedes Element in data['results']['bindings']
        country = item['countryLabel']['value'] #Ländername (countryLabel) wird extrahiert.
        population = int(item['population']['value']) #Bevölkerung (population) wird extrahiert.
        results.append({'country': country, 'population': population}) #Diese Daten werden als Dictionary mit den Schlüsseln country und population zur Liste results hinzugefügt.
    
    # Ergebnisse ausgeben
    for result in results:
        print(f"Land: {result['country']}, Bevölkerung: {result['population']}")
else:
    print(f"Fehler bei der Anfrage: {response.status_code}") #Falls die Anfrage nicht erfolgreich war, wird ein Fehlerstatuscode ausgegeben.