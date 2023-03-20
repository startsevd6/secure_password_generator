from random import choice


def generate_password(len1, chars):
	password = ''
	for j in range(len1):
		password += choice(chars)
	return password


def generate_more():
	while True:
		more = input('Нужно ещё генерировать пароли? (да/нет)\n')
		if len(more) > 0:
			if more.startswith('д'):
				return True
			elif more.startswith('н'):
				return False
			else:
				print('Вам нужно ввести "да" или "нет"')
		else:
			print('Вам нужно ввести "да" или "нет"')


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous = 'il1Lo0O'

chars = ''

more = True
while more:
	while True:
		count1 = input('Сколько паролей нужно сгенерировать? (от 1 до 1000)\n')
		if count1.isdigit():
			count1 = int(count1)
			if 1 > count1 > 1000:
				print('Вам нужно ввести число от 1 до 1000')
			else:
				break
		else:
			print('Вам нужно ввести целое число')
	while True:
		len1 = input('Какой длины должны быть пароли? (от 1 до 64)\n')
		if len1.isdigit():
			len1 = int(len1)
			if 1 > len1 > 64:
				print('Вам нужно ввести число от 1 до 64')
			else:
				break
		else:
			print('Вам нужно ввести целое число')
	while True:
		q_digits = input('Должны ли пароли содержать цифры от 0 до 9? (да/нет)\n')
		if len(q_digits) > 0:
			if q_digits.startswith('д'):
				chars += digits
				break
			elif q_digits.startswith('н'):
				break
			else:
				print('Вам нужно ввести "да" или "нет"')
		else:
			print('Вам нужно ввести "да" или "нет"')
	while True:
		q_lowercase_letters = input('Должны ли пароли содержать прописные буквы от "A" до "Z"? (да/нет)\n')
		if len(q_lowercase_letters) > 0:
			if q_lowercase_letters.startswith('д'):
				chars += lowercase_letters
				break
			elif q_lowercase_letters.startswith('н'):
				break
			else:
				print('Вам нужно ввести "да" или "нет"')
		else:
			print('Вам нужно ввести "да" или "нет"')
	while True:
		q_uppercase_letters = input('Должны ли пароли содержать строчные буквы от "a" до "z"? (да/нет)\n')
		if len(q_uppercase_letters) > 0:
			if q_uppercase_letters.startswith('д'):
				chars += uppercase_letters
				break
			elif q_uppercase_letters.startswith('н'):
				break
			else:
				print('Вам нужно ввести "да" или "нет"')
		else:
			print('Вам нужно ввести "да" или "нет"')
	while True:
		q_punctuation = input('Должны ли пароли содержать символы от !#$%&*+-=?@^_.? (да/нет)\n')
		if len(q_punctuation) > 0:
			if q_punctuation.startswith('д'):
				chars += punctuation
				break
			elif q_punctuation.startswith('н'):
				break
			else:
				print('Вам нужно ввести "да" или "нет"')
		else:
			print('Вам нужно ввести "да" или "нет"')
	while True:
		q_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет)\n')
		if len(q_ambiguous) > 0:
			if q_ambiguous.startswith('д'):
				chars = list(chars)
				for i in ambiguous:
					if i in chars:
						chars.remove(i)
				chars = ''.join(chars)
				break
			elif q_ambiguous.startswith('н'):
				break
			else:
				print('Вам нужно ввести "да" или "нет"')
		else:
			print('Вам нужно ввести "да" или "нет"')
	for i in range(count1):
		print(generate_password(len1, chars), sep='\n')
	more = generate_more()
print('Обращайтесь ещё!')
