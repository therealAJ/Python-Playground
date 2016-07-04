def repeat(s, exclaim):
	result = s
	if exclaim:
		result = result + '!!!'
	return result

def main():
	print repeat('Yay', False)
	print repeat('Woohoo', True)

if __name__ == '__main__':
	main()