from fraction import Fractions as frac
def expected_height(n, e={0:0}):
	if n not in e:
		eh = expected_height
		e[n] = 1 + frac( sum( eh(max(n-i,i-1)) for i in range(1, n+1)) , n)
	return e[n]
