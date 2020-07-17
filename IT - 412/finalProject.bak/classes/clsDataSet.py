
from csv_convert.convert_to_csv import convert_csv
from json_convert.convert_to_json import convert_json
from utilFunctions.functions import *


class DataSet():
    def __init__(self, data):
        self.data = data

    def clean_data(self, file=None):
        if file == None:
            with open(self.data, 'r') as file:
                file = file.readlines()
            newFile = []
            for count, line in enumerate(file):
                if count == 0:
                    header = line.split('|')
                    lin = [li.replace('#', '').strip() for li in header]
                    newFile.append(lin)
                else:
                    lin = [li.replace('#', '').strip()
                            for li in line.split('|')]
                    newFile.append(lin)
            return newFile
        else:
            with open(file, 'r') as file:
                file = file.readlines()
            newFile = []
            for count, line in enumerate(file):
                if count == 0:
                    header = line.split('|')
                    lin = [li.replace('#', '').strip() for li in header]
                    newFile.append(lin)
                else:
                    lin = [li.replace('#', '').strip()
                            for li in line.split('|')]
                    newFile.append(lin)
            return newFile

    def conver_json(self):
        data = self.clean_data()
        convert_json(data)

    def conver_csv(self):
        data = self.clean_data()
        convert_csv(data)

	def enter_record_and_validate(self):

		name = "abcdefghijklmnopqrstuvwxyz1234567890- '"

		address_not = '!"@$%^&*_=+<>?;[]{\}\''

		city_allowed = "abcdefghijklmnopqrstuvwxyz' "

		phone = '0123456789-'

		email_not = '! " \' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } '

		check = 0
		while True:

			while True:
				check_first = 0
				print('To Exit, enter "EXIT"')
				firstName = input('Please enter the first name: ')
				if firstName.strip().lower() == 'exit':
					print('Your are now exiting the application')
					check += 1
					break
				if len(firstName.strip()) != 0 and hasLetters(firstName) == True:
					pass
				else:
					print('Please enter a value for first name.')
				for i in firstName:
					if i.lower() not in name:
						check_first += 1
						print('Please enter a valid first name.')
						break
				if check_first > 0:
					continue
				break
			if check == 1:
				break

			while True:
				check_last = 0
				print('To exit, enter "Exit"')
				lastName = input('Please enter the last name: ')
				if lastName.strip() == 'exit':
					print('You are now exiting the application.')
					check += 1
					break
				if len(lastName.strip()) != 0 and hasLetters(lastName) == True:
					pass
				else:
					print('Please enter a valid value for last name.')
				for i in lastName:
					if i.lower() not in name:
						check_last += 1
						print('Please enter a valid last name.')
						break
				if check_last > 0:
					continue
				break
			if check == 1:
				break

			while True:
				print('To exit, enter "Exit"')
				companyName = input('Please enter company name:')
				if companyName.strip() == 'exit' or companyName.lower() == 'exit':
					check += 1
					break
				if len(companyName.strip()) != 0:
					pass
				else:
					print('Please enter a value for company name.')
				if len(companyName.strip()) != 0:
					companyName = companyName.replace(
						'"', '').replace("'", '')
					break
			if check == 1:
				break

			while True:
				check_address = 0
				print('To exit, enter "Exit"')
				address = input('Please enter the address :')
				if address.strip() == 'exit' or address.lower() == 'exit':
					check += 1
					break
				if len(address.strip()) != 0:
					pass
				else:
					print('Please enter a value for the address.')
				for i in address:
					if i.lower() in address_not:
						check_address += 1
						print('The address you entered is invalid')
						break
				if check_address > 0:
					continue
				break
			if check == 1:
				break

			while True:
				check_city = 0
				print('To exit, enter "exit"')
				city = input('Please enter the city name :')
				if city.strip() == 'exit' or city.lower() == 'exit':
					check += 1
					break
				if len(city.strip()) != 0:
					pass
				else:
					print('Please enter a value for the city.')
				for i in city:
					if i.lower() not in city_allowed:
						print('The city entered was invalid')
						check_city += 1
						break
				if check_city > 0:
					continue
				break
			if check == 1:
				break

			while True:
				check_county = 0
				print('To exit, enter "Exit"')
				county = input('Please enter the county name: ')
				if county == 'exit' or county.lower() == 'exit':
					check += 1
					break
				if len(county.strip()) != 0:
					pass
				else:
					print('Please enter a value for the county')
				for i in address:
					if i.lower() not in city_allowed:
						check_county += 1
						print('Please enter a valid value for the county')
						break
				if check_county > 0:
					continue
				break
			if check == 1:
				break

			while True:
				check_state = 0
				print('To exit, enter "Exit"')
				state = input('Please enter the State: ')
				if state == 'exit' or state.lower() == 'exit':
					check += 1
					break
				if len(state.strip()) != 0 and hasLetters(state) == True:
					pass
				else:
					print('Please enter a valid state.')
				for i in state:
					if len(state.strip()) != 2 or not state.isalpha():
						print('The state you entered was invalid')
						check_state += 1
						break
				if check_state > 0:
					continue
				break
			if check == 1:
				break

			while True:
				check_zip = 0
				print('To exit, enter "Exit"')
				zipCode = input('Please enter the zipcode: ')
				if zipCode == 'exit' or zipCode.lower() == 'exit':
					check += 1
					break
				if len(zipCode.strip()) != 0:
					pass
				else:
					print('Please enter a value for Zipcode.')
					continue
				"""Check this line below"""
				if len(zipCode.strip()) < 4 or len(zipCode.strip()) > 5 or not zipCode.isdigit():
					check_zip += 1
					print('The zipcode entered was invalid')
					continue

				if check_zip > 0:
					continue
				break
			if check == 1:
				break

			while True:
				check_phone = 0
				print('To exit, enter "Exit"')
				phoneNumber = input('Please enter your phone number: ')
				if phoneNumber == 'exit' or phoneNumber.lower() == 'exit':
					check += 1
					break
				if len(phoneNumber.strip()) != 0:
					pass
				else:
					print('Enter a value')
				for i in phoneNumber:
					if i not in phone:
						check_phone += 1
						print('---- phone format invalid ----')
						break
				if check_phone > 0:
					continue
				break
			if check == 1:
				break

			while True:
				check_email = 0
				print('To exit, enter "Exit"')
				email = input('Please enter an email address: ')
				if email == 'exit' or email.lower() == 'exit':
					check += 1
					break
				if len(email.strip()) != 0:
					pass
				else:
					print('Please enter a value for email address.')
				for i in email:
					if i in email_not:
						check_email += 1
						print('The email address you entered is invalid.')
						break
				if check_email > 0:
					continue
				break
			if check == 1:
				break
			break

		if check == 1:
			print('The Record was not entered.')
			return
		else:
			details = {'firstName': firstName, 'lastName': lastName, 'email': email, 'phoneNumber': phoneNumber,
						'address': address, 'zip': zipCode, 'county': county, 'state': state, 'city': city, 'companyName': companyName}
			print(details)
			return details
            
	def insert(self,conn):
    		mycursor = conn.cursor()
		data_r= self.enter_record_and_validate()

		if data_r == 0:
			print('No data is entered !!')

		sql= "INSERT INTO `crm_data` (fName,lName,address,city,state,zipcode,company,primaryPhone,secondaryPhone,emailAddress ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		data=(data_r['first_name'],data_r['last_name'],data_r['address'],data_r['city'],data_r['state'],
			  data_r['zip'],data_r['company_name'],data_r['phone_number'],data_r['phone_number_2'],data_r['email'])
		try:
			mycursor.execute(sql, data)
			conn.commit()
			print("saved successfully")
		except Exception as e:
			print("Record already exists...")
	def show(self,conn):
	  	mycursor = conn.cursor()
	  	sql= "SELECT * FROM `crm_data`"
	  	try:
	  		mycursor.execute(sql)
	  		results=mycursor.fetchall()
	  		conn.commit()
	  		print("saved successfully")
	  		print('Columns - \n')
	  		print('crmID,fName,lName,address,city,state,zipcode,company,primaryPhone,secondaryPhone,emailAddress')
	  		print('\n Rows -\n')
	  		for result in results:
	  			print(str(result)[1:-1])

	  	except Exception as e:
	  		print(e)
     
	def print_menu(self):
	  	print('\n')
	  	print('--- input 1 to see all the records')
	  	print('--- input 2 to insert a record')
	  	print('--- input 3 to delete a record')
	  	print('--- input 4 to update a record')
	  	print('--- input 5 to quit program')
	  	print('\n')

	def menu(self):
	  	self.print_menu()
	  	while True:		  	
		  	accept='12345'
		  	input_value= input('--- Enter a value :')
		  	if input_value.strip() ==0 or len(input_value.strip()) >1:
		  		print('--- Please enter a valid value')
		  	else:
		  		for value in input_value:
		  			if value not in accept:
		  				print('--- Please input a valid value')
		  				print('--- To see the menu again, press 1, to enter an option, press 0 :(0 or 1) ')
		  				g_value= input('Enter your choice :')
		  				if g_value== '1':
		  					self.print_menu()
		  					continue
		  				elif g_value== '0':
		  					continue
		  				else:
		  					print('starting again... choose your option')
		  					self.print_menu()
		  					continue
		  			else:
		  				db = pymysql.connect(host='Localhost',user='root',passwd='',port=3308, db='ifezue')
						
		  				if input_value=='1':
		  					self.show(db)
		  				elif input_value=='2':
		  					self.insert(db)
		  				elif input_value=='3':
		  					self.delete(db)
		  				elif input_value=='4':
		  					self.update(db)
		  				elif input_value=='5':
		  					print('Quiting application...')
		  					return
		  			print('\n')
		  			print('\n')

		  			print('Will you like to run another option(1) or quit (0)')
		  			value= input('Enter your choice :')
		  			if value.strip() == '0':
		  				print('quiting application...')
		  				return
		  			else:
		  				print('starting again... choose your option')
	  					self.print_menu()
	  					continue



	def delete(self,conn):
	  	mycursor = conn.cursor()
	  	while True:	  
	   		check=0
	   		print('To quit, press "quit"')
	   		first_name= input(' --- Input first name to delete:')
	   		if first_name.strip() =='quit':
	   			check+=1
	   			break
	   		if len(first_name.strip()) !=0:
	   			break
	   		else:
	   			print('Enter a value')
	  	if check ==1:
	   		print('--- quiting')
	  	while True:	  
	   		check=0 
	   		print('To quit, press "quit"')
	   		last_name= input(' --- Input last name to delete:')
	   		if last_name.strip() =='quit':
	   			check+=1 
	   			break
	   		if len(last_name.strip()) !=0:
	   			pass
	   			break
	   		else:
	   			print('Enter a value')
	  	if check ==1:
	   		print('--- quiting')
	   		return 0
	  	query= 'SELECT * FROM `crm_data` WHERE `fName` =%s AND `lName` =%s'
	  	mycursor.execute(query,(first_name,last_name))
	  	results=mycursor.fetchall()
	  	if len(results) ==0:
	  		print('There is no such record')
	  		return
	  	else:
	  		print('Deleting...')
	  		sql='DELETE FROM `crm_data` WHERE `fName` =%s AND `lName` =%s'
	  		mycursor.execute(sql,(first_name,last_name))
	  		conn.commit()
	  		print('--- Record deleted successfully')
	def update(self,conn):
		mycursor = conn.cursor()
		while True:	  
	   		check=0
	   		print('To quit, press "quit"')
	   		first_name= input(' --- Input first name to update:')
	   		first_name=first_name.lower()
	   		if first_name.strip() =='quit':
	   			check+=1 
	   			break
	   		if len(first_name.strip()) !=0:
	   			pass
	   			break
	   		else:
	   			print('Enter a value')
		if check ==1:
			print('--- quiting')
		while True:	  
	   		check=0
	   		print('To quit, press "quit"')
	   		last_name= input(' --- Input last name to update:')
	   		last_name=last_name.lower()
	   		if last_name.strip() =='quit':
	   			check+=1 
	   			break
	   		if len(last_name.strip()) !=0:
	   			pass
	   			break
	   		else:
	   			print('Enter a value')
		if check ==1:
			print('--- quiting')
			return 0
		query= 'SELECT * FROM `crm_data` WHERE `fName` =%s AND `lName` =%s'
		mycursor.execute(query,(first_name,last_name))
		results=mycursor.fetchall()
		if len(results) ==0:
			print('There is no such record')
		else:
			print(results[0])
			print('Updating...')
			print('Enter new record for the row')
			data_r= self.enter_record_and_validate()
			if data_r==0:
				print('No data is entered!')
				print('going back to the main menu')
				return
			sql='UPDATE `crm_data` SET fName=%s,lName=%s,address=%s,city=%s,state=%s,zipcode=%s,company=%s,primaryPhone=%s\
	   			,secondaryPhone=%s,emailAddress=%s WHERE `fName` =%s AND `lName` =%s'
			data=(data_r['first_name'],data_r['last_name'],data_r['address'],data_r['city'],data_r['state'],
			  data_r['zip'],data_r['company_name'],data_r['phone_number'],data_r['phone_number_2'],data_r['email'],first_name,last_name)
			mycursor.execute(sql,data)
			conn.commit()
			print('--- Record updated successfully')
   
   
