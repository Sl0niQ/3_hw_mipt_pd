import random
#------------------------1------------------------
"""
	#1 реализуйте:
	Декоратор @even, который будет заменять функцию на идентичную, но каждое нечётное по 
	порядку выполнение вместо исполнения не будет делать ничего (например вместо нормальной 
	логики будет возвращать None и завершать работу.)
"""
def divider(n):
	print(f"\n#{n} task")


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

divider(1)
for i in range(1, 5):
	print_call_number(i)

#------------------------2------------------------
"""
	#2 декоратор @clip, который пробрасывает в функцию все позиционные аргументы, при этом не 
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

divider(2)
print_clip(1, 2, z = 3, s = "_")       # 1~2~0
print(1, 2, 3, sep = "_")              # 1_2_3

#------------------------3------------------------
"""
	#3 Декоратор @repeat(x) (нужно реализовать функцию repeat(x), которая возвращает в качестве 
	результата декоратор), которая выполняет декорируемую функцию x раз (например @repeat(5) от 
	print(1, end="") выведет "11111"), и возвращает тюпл из значений-результатов (например 
	@repeat(5) от sum([1, 2, 3]) вернёт (6, 6, 6, 6, 6))
"""

def repeat(x):
	def decorator(func):
		def wrapper(n):
			result = []
			for i in range(x):
				result.append(func(n))
			return tuple(result)
		return wrapper
	return decorator

@repeat(5)
def random_sum(n):
    return sum(random.random() for i in range(n))

divider(3)
print(random_sum(10))

#------------------------4------------------------
"""
	#4 Декоратор @cash, который по входным данным проверяет, была ли уже выполнена функция от 
	таких аргументов, и если была - возвращает сохранённое значение. (для простоты можете считать, 
	что функция, которую мы декорируем всегда имеет всего один хешируемый аргумент. Если чувствуете 
	в себе силы, можете попробовать реализовать для общего случая)
"""

def cash(func):
	cashe = {}	
	def wrapper(*args, **kwargs):
		key = (args, frozenset(kwargs.items()))
		if key not in cashe:
			cashe[key] = func(*args, **kwargs)
		return cashe[key]
	return wrapper

@cash
def fib(x):
	print(f"вызвана фунция Фибоначчи f({x})")
	if x < 2:
		return 1
	else:
		return fib(x-1) + fib(x-2)

divider(4)
print(fib(10))
print(fib(10))