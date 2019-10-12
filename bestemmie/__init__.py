import requests


class Bestemmie:
    def __init__(self):
        self.base_url = "http://bestemmie.org/api/{}"
        self.bestemmie_list = []

    def random(self):
        response = requests.get(self.base_url.format("random"))
        response.raise_for_status()

        return response.json()['bestemmia']

    def all(self):

        url = self.base_url.format("bestemmie")

        while url is not None:
            response = requests.get(url)
            response.raise_for_status()
            self.bestemmie_list.append(response.json()['results'])
            url = response.json()['next'] or None
        return self.bestemmie_list

    def add(self, bestemmia, show_succes_message=False):
        params = {"bestemmia": bestemmia}
        response = requests.post(
            self.base_url.format("bestemmie/"), params)
        response.raise_for_status()
        if response.status_code == 204:
            if show_succes_message:
                print(f"Added: {bestemmia}")
        else:
            print(f"There is a problem on adding {bestemmia}")
