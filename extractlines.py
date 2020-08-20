#!\usr\bin\env python
#
#
#
#

import bs4
import inspect
def extractlines(directory):

	x = open(directory, "r", encoding = "utf-8").read()

	soup = bs4.BeautifulSoup(x)

	for k in soup.select("lines"):
		print("\"\"\"", end = "")

		for index, j in enumerate(k.select("string")):

			if index == len(k.select("string")) - 1:

				print(j.text + "\"\"\",\n")

			else:

				print(j.text)

		#print("\"\"\",")

if __name__ == "__main__":

	extractlines("C:\\Users\\RetailAdmin\\Desktop\\jump\\Jump.King\\Content\\props\\textures\\old_man\\lines\\skeleton_quotes.xml")

	# line = """ ssassd


	# 			sfa
	# 			sdf"""

	# print(inspect.cleandoc(line))