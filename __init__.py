import re
class grammar(object):

	def __init__(self, grammar):
		self.grammar = grammar

	def __call__(self, function):
		def process(input):
			print self.grammar
			node = {}
			token = {'name': 'token-name', 'value': 'token-value'}
			function(node, token)
			return node
		return process