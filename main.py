import Fractions
from expected import expected_height as eh
import tree_Counter as tc

def compareOutput(n):
	calc = eh(n)
	empir = tc.average_height(n)
	if calc == empir:
		return True
	else
		print("expeted <%r> but got <%r>" % empir, calc)
