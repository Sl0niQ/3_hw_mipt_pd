#------------------------1------------------------
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
def print_call_number(x):
	print("hello", x)

for i in range(1, 5):
	print_call_number(i)

#------------------------2------------------------
"""
	Декоратор @clip, который пробрасывает в функцию все позиционные аргументы, при этом не 
	пробрасывает ключевые (например @clip от print(1, 2, 3, sep="_") напечатает "1 2 3", не 
	применив sep)
"""

def clip(func):
	def wrapper(*args, **kwargs):
		return func(*args)
	return wrapper

@clip
def print_clip(x, y, z = 0, s = "~"):
    print(x, y, z, sep = s)

print_clip(1, 2, z = 3, s = "_")       # 1~2~0
print(1, 2, 3, sep = "_")              # 1_2_3

#------------------------3------------------------