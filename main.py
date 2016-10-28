import fraction
from expected import expected_height as eh
import tree_Counter as tc

def compareOutput(n):
	calc = eh(n)
	empir = tc.average_height(n)
	if calc == empir:
		return True
	else
		print("expeted <%r> but got <%r>" % empir, calc)
		return False

if __name__ == '__main__':
	for i in range(12):
		compareOutput(n)
