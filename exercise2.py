def find_longest_word(a):
	length = len(a[0])
	words = a [0]
	for i in wordlist:
		if len (i) > length:
			words = (i)
	return words, length


if __name__ == '__main__':
			wordlist = raw_input(['Inserisci' + ' ' +'parole' + ' ' + 'separate' + ' ' + 'da' + ' ' + 'spazi']).split()
			words, length = find_longest_word(wordlist)
			print (words, "is", length, "characters long")
