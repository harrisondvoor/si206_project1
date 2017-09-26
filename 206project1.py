import os
import filecmp

#1
def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	f = open(file, 'r')
	header = f.readline().strip().split(',')
	lst1 = []
	for x in f.readlines():
		dict1 = {}
		num = 0
		lst2 = x.strip().split(',')
		for key in header:
			dict1[key] = lst2[num]
			num +=1
		lst1.append(dict1)
	return lst1


#2
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sort_lst = sorted(data, key = lambda x: x[col])
	return sort_lst[0]["First"] + ' ' + sort_lst[0]["Last"]

#3
#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	size_of_grade = {'Senior':0, 'Junior':0, 'Sophomore':0, 'Freshmen':0}
	for y in data:
		if y['Class'] == 'Senior':
			size_of_grade['Senior'] +=1
		elif y['Class'] == 'Junior':
			size_of_grade['Junior'] += 1
		elif y['Class'] == 'Sophomore':
			size_of_grade['Sophomore'] += 1
		elif y['Class'] == 'Freshmen':
			size_of_grade['Freshmen'] += 1
		lst_srtd_classes = sorted(size_of_grade, key = lambda z: size_of_grade[z], reverse = True)
		tot = []
		for b in lst_srtd_classes:
			tot.append((b, size_of_grade[a]))
			return tot




#4
# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	dict_of_days = {}
	for x in a:
		date = x['DOB'].split('/')
		day = date[1]
	if day not in dict_of_day:
		dict_of_days = 1
	else:
		dict_of_days += 1
	srtd_days = sorted(dict_of_days, key = lambda d: dict_of_days[d], reverse = True)
	return int(srtd_days[0])

#5
# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	age = []
	for x in a[1:]:
		month, day, year = x['DOB'].split('/')
		current_year = int(datetime.date.today().year)
		current_month = int(datetime.date.today().month)
		current_day = int(datetime.date.today().day)
		if ((current_day > int(day)) and current_month > int(month)):
			age.append(current_year - int(year))
		else:
			age.append(current_year - int(year) + 1)
	return round((sum(age) / len(age)), 0)
		


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
#6
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	csv = open(fileName, 'w')
	srtdlst = sorted(a, key = lambda u: u[col])
	for element in srtdlst:
		temp = []
		for value in element.values():
			temp.append(value)
		row = ",".join(temp[:3])
		csv.write(row + "\n")




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

