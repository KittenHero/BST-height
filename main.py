import fractions
from expected import expected_height as eh
import tree_counter as tc

def compare_output(n):
	calc = eh(n)
	empir = tc.average_height(n)
	if calc == empir:
		print("n %i: %s" % (n, calc)) 
		return True
	else:
		print("n %i: expected <%s> but got <%s>" % (n, empir, calc))
		return False

if __name__ == '__main__':
	for i in range(12):
		compare_output(i)
