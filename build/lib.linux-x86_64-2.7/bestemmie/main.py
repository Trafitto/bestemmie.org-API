import requests

class Bestemmie:
    base_ulr = "http://bestemmie.org/api/{}/"
    bestemmie = []
    def random():
        response = requests.get(self.base_url.format("random"))
        response.raise_for_status()

        return response.json()['bestemmia']
    
    def all(url=self.base_ulr.format(bestemmie)):
        
        response = requests.get(url)
        response.raise_for_status()

        for bestemmie in response.json()['results']:
            self.bestemmie.append(bestemmie['bestemmia'])
        next_url = response.json()['next']
        if next_url:
            all(next_url)
        else:
            return self.bestemmie