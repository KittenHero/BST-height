#-----------------part 1 : empirical measures----------------------------------
'''
computes the average height of a BST with n nodes
O(n! n log n) [+ O(n)

slow as #F for n >= 10
'''
from fractions import Fraction as frac
def average_height(n):
	weighed_sum = 0
	total = 0
	for h, count in height_counts(n).items():
		weighed_sum += h*count
		total += count
	# assert total == __import__('math').factorial(n), total
	return frac(weighed_sum, total)

'''
Generates all permutation of an [0, 1, 2..., n-1]
and calculates the height of each corresponding BST
O(n! n log n)
'''
from itertools import permutations as permute
def height_counts(n):
	heights = {}
	for insert_order in permute(tuple(range(n))):
		h = get_height(insert_order)
		heights[h] = 1 + heights.get(h, 0)
	return heights

'''
computes the height of a BST given the insert order
O(n log n) average

needs optimisation

definition:
height(subtree) = 1 + max( height(leftsub), height(rightsub) )
'''
def get_height_old(insert_order):
	if insert_order:
		Lsubtree, Rsubtree = [], []
		for x in insert_order[1:]:
			if x < insert_order[0]:
				Lsubtree.append(x)
			else:
				Rsubtree.append(x)
		return 1 + max(get_height_old(Lsubtree), get_height_old(Rsubtree))
	else:
		return 0

'''
same as above
O(n log n) average

not any faster, but non-recursive

values agree with above for at least up to n = 10
'''
def get_height(insert_order):
	stackFrame = [(insert_order, 0)]
	maxDepth = 0
	while stackFrame:
		subtree, depth = stackFrame.pop()
		maxDepth = max(depth, maxDepth)
		if subtree:
			Lsub, Rsub = [], []
			for x in subtree[1:]:
				if x < subtree[0]:
					Lsub.append(x)
				else:
					Rsub.append(x)
			stackFrame.append((Lsub, depth + 1))
			stackFrame.append((Rsub, depth + 1))
	# assert maxDepth == get_height_old(insert_order), 'n=%r:%d' % (insert_order, maxDepth)
	return maxDepth
# -------------------------part 2: analytic measures-------------------------------------------
'''
Straight forward implementation
O(n^2)

expected(subtree) = 1 + average< max <expected(leftsub), expected(rightsub)> >

agrees with empirical method only up to n = 6
'''
def expected_height_old(n, e={0:0}):
	if n not in e:
		eh = expected_height_old
		e[n] = 1 + frac( sum( eh(max(n-i,i-1)) for i in range(1, n+1)) , n)
		# avh = average_height(n)
		# assert e[n] == avh, '%.2f should be %.2f' % (e[n], avh)
	return e[n]

'''
sub-Optimied version : O(n)

agrees with non-optimised version for at least up to n = 500
simplified recurrence obtained from
	n e[n] - (n-1) e[n-1]
	and using e[n] monotonic behaviour to simplify max
'''
def expected_height(n, e={0:0}):
	if n not in e:
		eh = expected_height
		e[n] = frac(1 + (n + 1)*eh(n-1) - eh((n-1)//2), n)
		# assert e[n] == expected_height_old(n), '%.2f should be %.2f?' % (e[n], expeceted_height_old(n))
	return e[n]
