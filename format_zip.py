def main():
	form_s = lambda x: "'%s',"% x.replace('\n', '')
	filename = input('File name: ')
	try:
		if filename:
			f = open(filename, 'r+')
		else:
			f = open('zipcodes.txt', 'r+')
	except Exception as e:
		print('\n**invalid file name**')
		return e

	out = [form_s(line) for line in f]
	out = ''.join(out)[:-1]

	with open('zip_output.txt', 'r+') as output:
		output.seek(0)
		output.truncate()
		output.write(out)
	output.close()
	f.close()

if __name__ == '__main__':
	main()
