"""
	реализуйте:
	Декоратор @even, который будет заменять функцию на идентичную, но каждое нечётное по 
	порядку выполнение вместо исполнения не будет делать ничего (например вместо нормальной 
	логики будет возвращать None и завершать работу.)
"""

def even(func):
	call_counter = 0
	def wrapper(*args, **kwargs):
		nonlocal call_counter
		call_counter += 1
		result = None
		if call_counter % 2 == 0:
			result = func(*args, **kwargs)
		return result
	return wrapper

@even # == print_call_counter = even(print_call_counter)
def print_call_number(i):
	print('i = ', i)

for i in range(1, 5):
	print_call_number(i)

