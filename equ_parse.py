

def equ_parse(equation):
	equ_data = []
	for i in range(0, len(equation)): equ_data.append(equation[i])

def equ_eval(equ_data):
	eq_operators = ['/', '+', '-', '^', '*']
	open_p_count = 0
	closed_p_count = 0
	numbers = []
	ops = []
	for i in range(0, len(equ_data)):
		if equ_data == '(': open_p_count +=1
		if equ_data == ')': close_p_count +=1
		if equ_data[i] not in eq_operators:
			numbers.append(equ_data[i])
		if equ_data[i] in eq_operators: 


