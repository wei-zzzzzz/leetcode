'''
解題思路：
1.先比較字串長度以及為空之字串（因無法交換），再者Ａ與Ｂ字串一一校對，若有兩個字母不同則交換完在做比對
2.若只有一個字母不同則直接回傳False（修正 j 之處）。
   麻煩點為兩字串接一樣長且字母皆一樣！！解決辦法為：
3.以dictionary 紀錄字母出現次數（用此方法的原因在於可以不浪費空間造list 存放26格）
4. 找出dictionary的values以list呈現，並看是否次數有大於1之存在者，若有則回傳 True，反之則 False
'''
class Solution:
	def buddyStrings(self, A: str, B: str) -> bool:
		if (len(A) != len(B)) or (A == "") or (B == ""):
			return False
		i = 0
		t = 0
		while A[I] == B[I]:
			i += 1
			if I == len(A):
				count = {}
				tempL = list(A)
				for idex in tempL:
					count[idex] = 0
				for idex in tempL:
					count[idex] += 1
				countV = list(count.values())
				for t in range(len(countV)):
					if countV[t] > 1:
						return True
					t += 1
				return False
		j = I+1
		if j == len(A):
			return False
		while A[j] == B[j]:
			j += 1
			if j == len(A):
				return False
		#swap letters
		tempL = list(A)
		temp = tempL[I]
		tempL[I] = tempL[j]
		tempL[j] = temp
		A = ''.join(tempL)
		return A == B
