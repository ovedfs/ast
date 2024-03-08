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

class Program:
	tokens = []

	def __init__(self, code):
		self.code = code

	def __repr__(self):
		return "\n".join([repr(item) for item in Token.tokens]) or ""

	def parse(self):
		# Leer el programa línea por línea
		# Emitir tokens por cada unidad sintáctica
		# yield | Poner todos los tokens en una colección
		
		with open(self.code, 'r') as file:
			for num_line, line in enumerate(file, start=0):
				i = 0
				while i < len(line):
					if line[i] in '0123456789':
						number = ''
						column = i
						while line[i] in '0123456789' and i < len(line):
							number += line[i]
							i += 1
						Program.tokens.append(Token('INT', number, num_line, column))
					if line[i] in '+-*/':
						op = line[i]
						column = i
						i += 1
						Program.tokens.append(Token('OP', op, num_line, column))
					else:
						i += 1
		
		print(Program.tokens)

class Token:
	def __init__(self, kind, value, line, column):
		self.type = kind
		self.value = value
		self.line = line
		self.column = column

	def __repr__(self):
		return self.value

	
code = sys.argv[1]

program = Program(code)
program.parse()




