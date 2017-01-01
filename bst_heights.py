from fractions import Fraction as frac
from math import factorial as fac


def average_height(n, distribution):
	return frac( sum(h*count for h, count in distribution.items()), fac(n) )


#-----------------part 1 : empirical measures----------------------------------
'''
computes the average height of a BST with n nodes
O(n! n log n) [+ O(n)

slow as #F for n >= 10
'''
def slow_av(n):
	average_height(n, height_counts(n))



'''
Generates all permutation of an [0, 1, 2..., n-1]
and calculates the height of each corresponding BST
O(n! n log n)
'''
from itertools import permutations as permute
from collections import Counter
def height_counts(n):
	return Counter(get_height(order) for order in permute(range(n)))

'''
computes the height of a BST given the insert order
O(n log n) average

needs optimisation

definition:
height(subtree) = 1 + max( height(leftsub), height(rightsub) )
'''
def get_height(insert_order):
	if not insert_order:
		return 0

	root, Lsub, Rsub = insert_order[0], [], []
	for x in insert_order[1:]:
		if x < root: 	Lsub.append(x)
		else:		Rsub.append(x)
	return 1 + max(get_height(Lsubtree), get_height(Rsubtree))



	
'''
same as above
O(n log n) average
non-recursive (but slower)

values agree with above for at least up to n = 10
'''
def get_height_new(insert_order):
	stackFrame = [(insert_order, 0)]
	n = len(insert_order)
	maxDepth = 0
	while stackFrame:
		subtree, depth = stackFrame.pop()
		maxDepth = max(depth, maxDepth)
		if maxDepth == n:
			break
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




# -------------------------part 2: analytic recreation---------------------------------
def fast_av(n):
	return average_height(n, bst_height_distribution(n))


def choose(n, k): # O(n)
	num, denom = 1, 1
	for n in range(n - k + 1, n + 1):
		num *= n
	for k in range(1, k + 1):
		denom *= k
	return num // denom



# O(n^3)? definitely polynomial time
def bst_height_distribution(n, cache={0:{0:1}}):
	if n < 0: return cache
	if n not in cache:
		self = bst_height_distribution
		cache[n] = {}
		for i in range(1, n + 1):
			rTrees = self(n - i)
			lTrees = self(i - 1)
			permutations = choose(n - 1, i - 1)
			for LHeight, LCount in lTrees.items():
				for RHeight, RCount in rTrees.items():
					h = 1 + max(LHeight, RHeight)
					cache[n][h] = cache[n].get(h, 0) + LCount * RCount * permutations
	return cache[n]





# -------------------------part 3: naiivette-------------------------------------------


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
	return e[n]