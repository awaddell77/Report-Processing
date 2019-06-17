

def equ_parse(equation):
	equ_data = []
	for i in range(0, len(equation)): equ_data.append(equation[i])

def equ_eval(equ_data):
	eq_operators = ['/', '+', '-', '^', '*']
	for i in range(0, len(equ_data)):
