import fractions
from expected import expected_height as eh
import tree_Counter as tc

def compareOutput(n):
	calc = eh(n)
	empir = tc.average_height(n)
	if calc == empir:
		print("n %i: %r" % frac) 
		return True
	else:
		print("n %i: expected <%r> but got <%r>" % n, empir, calc)
		return False

if __name__ == '__main__':
	for i in range(12):
		compareOutput(n)
