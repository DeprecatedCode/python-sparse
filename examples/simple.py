import sys
import sparse

# Language grammar
grammar = {
	'init': {
		'&'					: '\s+',
		'variable-name'		: '\w+'
	},

	'variable-name': {
		'&'					: '\s+',
		'&variable-value'	: '\(\s*'
	},

	'variable-value': (
		'@self'				, '\d+',
		'&init'				, '\s*\)',
		'junk'				, '.*'
	)
}

print grammar
exit()

# Define the simple language
@sparse.grammar(grammar)

print 
exit()
def simple(node, token):
	return node;

# Test the simple language parser
result = simple(
	"""'ace(101) box(202) cat(303)',
	'door(404) eel() foo ( 505 ) goo(',
	' 606',
	')'"""
)

print result