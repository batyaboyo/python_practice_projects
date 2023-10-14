def word_replacement():
	
	name = input("Enter your name ")
	str = "Hello i'm " + name + " and i love coding in python"
	old_word= input("Enter word to replace ")
	new_word = input("Enter new word to replace the old word ")
	print(str.replace(old_word, new_word))
	
word_replacement()