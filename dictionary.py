a="A dictionary is mutable and is another container type that can store any number of Python objects, including other container types. Dictionaries consist of pairs of keys and their corresponding values."
c={}
for w in a.lower().replace(',','').replace('.','').split():
	if w in c:
		c[w]+=1
	else:
		c[w]=1

print c

print c.get('and')

del c['and']
print c

c.clear()
print c