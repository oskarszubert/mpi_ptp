from math import sqrt

class Euler_pi:
	
	@staticmethod
	def compute_subtotals(left_bound, right_bound):
		subtotal = 0
		for number in range(left_bound, right_bound + 1):
			subtotal += (number**2)**-1

		return subtotal

	@staticmethod
	def add_subtotals(first_subtotal, second_subtotal):
		return first_subtotal + second_subtotal

	@staticmethod
	def calucalte_pi(sum_eries):
		pi_number = sqrt(6*sum_eries)
		return pi_number