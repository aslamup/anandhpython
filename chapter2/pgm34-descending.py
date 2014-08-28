def word_freq(words):
        frequency={}
        for i in words:
                frequency[i] = frequency.get(i,0) + 1
        return frequency

def read_words(filename):
        return open(filename).read().split()

def main(filename):
        frequency = word_freq(read_words(filename))
        l=[]
	for word, count in frequency.items():
		s=word,count
		l.append(s)
	a=reversed(sorted(l,key=lambda x :x[1]))
	for x,y in a:
		print x,y
	
	
		

word_freq(['foo.txt'])
read_words('foo.txt')
print main('foo.txt')
