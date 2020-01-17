def count_jhon(statement, search_string):
	count = 0
	st=statement.split(" ")
	print(len(st), search_string)
	for i in range(len(st)):
		if st[i] == "Emma":
			count=count+1
	print(search_string, " appeared ", count, "times!")

count_jhon("Emma is good developer Emma is aslo a writer", "Emma")
