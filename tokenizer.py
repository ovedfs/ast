# fiso
# INT: 123, 78, 8, 9
# VAR: 'var'
# OP: +, -, *, /
# PLUS: +
# MINUS: -
# MULT: *
# DIV: /
# EQUAL: =
# LEFT_SBRACKET: [
# RIGHT_SBRACKET: ]
# COMA: ,

# Programa (ejemplo)
# 8 + 9
# TOKEN(INT, 8, 1, 1)
# TOKEN(OP, '+', 1, 3)
# TOKEN(INT, 9, 1, 5)
#
# var mi_variable = 9
# TOKEN(VAR, 'var', 1, 1)

import sys

class Token:
	def __init__(self, kind, value, line, column):
		self.type = kind
		self.value = value
		self.line = line
		self.column = column

	def __repr__(self):
		pass

	def parse(program):
		# Leer el programa línea por línea
		# Emitir tokens por cada unidad sintáctica
		# yield | Poner todos los tokens en una colección
		
		with open(program, 'r') as file:
			for linea in file:
				print(linea.strip())




program = sys.argv[1]
Token.parse(program)




