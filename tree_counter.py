def height(insert_order):
	if insert_order:
		# if this looks like vanilla quick sort, it's no coincidence
		Lsubtree, Rsubtree = [], []
		for x in insert_order[1:]:
			if x < insert_order[0]:
				Lsubtree.append(x)
			else:
				Rsubtree.append(x)
		return 1 + max(height(Lsubtree), height(Rsubtree))
	else:
		return 0

from itertools import permutations as permute
def countHeights(n):
	heights = {}
	for tree in permute(list(range(n))):
		h = height(tree)
		heights[h] = 1 + heights.get(h, 0)
	return heights

from fractions import Fraction as frac
def average_height(n):
	heights = countHeights(n)
	weighed_sum = 0
	total = 0
	for h, count in heights.items():
		weighed_sum += h*count
		total += count
	return frac(weighed_sum, total)
