from collections import defaultdict
def distance(l):
	if len(l) > 1:
		return l[-1]-l[0]
	else:
		return -1

def solution(S):
	N = len(S)
	d = defaultdict(list)
	if S.islower() and S.isalpha():
		for i in range(0, N-1):
			d[S[i] + S[i+1]].append(i)
		_max = -1
		for l in list(d.values()):
			if distance(l) > _max:
				_max = distance(l)
		return _max
	else:
		return -1

S = input()
print(solution(S))
