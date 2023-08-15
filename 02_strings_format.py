name = 'bob'
# introduzindo o f
greeting= f'hello, {name}'

print(greeting)

print(f'hello, {name}')

# another way
name='Anastacia'
greeting='hello, {}'
with_name=greeting.format(name)
with_name_two=greeting.format('joao')

print(with_name)
print(with_name_two)


# longer_phrase
longer_phrase = 'hello, {}. Today is {}.'
formatado=longer_phrase.format("Andre", 'Sextou')
print(formatado)