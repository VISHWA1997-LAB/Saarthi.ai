

l1=["kolkata", "delhi"]
letter='''How far is <name1> from <name2>", How is the weather in <name1>'''
letter=letter.replace('<name1>', l1[0])
letter=letter.replace('<name2>', l1[1])
letter=letter.replace('<name3>', l1[0])

print(letter)