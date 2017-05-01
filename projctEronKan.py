import json 
with open ('findFee.json') as json_data:  #open findFee json file and store it as json_data
    data = json.load(json_data)  

#store user input in variables defined
feeType = {1: "Application Fee" , 2: "Exam Fee" }
nationality = {1: "INDIAN" , 2: "FOREIGN" , 3: "NRI", 4: "SAARC"}
level1 = {1:"UG" , 2: "PG", 3: "UG-DIPLOMA"}
level2 = 'ALL_LEVEL'
courses = 'ALL_COURSES'


# take input from user 
a = raw_input("Hello Sir\Mam\nTo determine the accurate fee to be paid.\nPlease select Fee Type: \n1 for Application Fee\n2 for Exam Fee?\n")

if ( a == '2'):
	b = raw_input("Please select Nationality: \n1 for INDIAN   \n2 for FOREIGN  \n3 for NRI	\n4 for SAARC?\n")
else:
	b = raw_input("Please select Nationality: \n1 for INDIAN   \n2 for FOREIGN\n")


c = raw_input("Please select Course Type: \n1 for Medical \n2 for Dental \n3 for Ayurveda?\n")
d = raw_input("Please select Level: \n1 for UG \n2 for PG \n3 for UG-DIPLOMA?\n")

	
#conditions for getting output from user based on json file
if (feeType[int(a)] == 'Application Fee' and nationality[int(b)] == 'INDIAN'):
	print 'Fee to be paid is $' + str(data[feeType[int(a)]][nationality[int(b)]][courses][level1[int(d)]]['amount'])
	
elif (feeType[int(a)] == 'Application Fee' and nationality[int(b)] == 'FOREIGN'):
	print 'Fee to be paid is $' + str(data[feeType[int(a)]][nationality[int(b)]][courses][level1[int(d)]]['amount'])
	
elif feeType[int(a)] == 'Exam Fee':
    print 'Fee to be paid is $' + str(data[feeType[int(a)]][nationality[int(b)]][courses][level2]['amount'])

else:
	print('please try again')
