import requests


class Bestemmie:
	def __init__(self):
		self.base_url = "http://bestemmie.org/api/{}/"
		self.bestemmie = []

	def random(self):
		response = requests.get(self.base_url.format("random"))
		response.raise_for_status()

		return response.json()['bestemmia']

	def all(self, url=None):

		if url is None:
			url = self.base_url.format("bestemmie")

		response = requests.get(url)
		response.raise_for_status()

		for bestemmie in response.json()['results']:
			self.bestemmie.append(bestemmie['bestemmia'])
		next_url = response.json()['next']
		if next_url:
			all(next_url)
		else:
			return self.bestemmie
