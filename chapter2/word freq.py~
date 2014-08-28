def word_freq(words):
	frequency={}
	for i in words:
		frequency[i] = frequency.get(i,0) + 1
	return frequency

def read_words(filename):
	return open(filename).read().split()

def main(filename):
	frequency = word_freq(read_words(filename))
	for word, count in frequency.items():
		print word, count

print word_freq(['foo.txt'])
print read_words('foo.txt')
print main('foo.txt')
