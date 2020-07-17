def showRecords(database):

    sqlString = "SELECT * FROM " + database
    try:
		results = my_db.executeSelectQuery(sqlString)
		print('Columns - \n')
		print('crmID,fName,lName,address,city,state,zipcode,company,primaryPhone,secondaryPhone,emailAddress')
		print('\n Rows -\n')
		for result in results:
			print(str(result)[1:-1])
    except Exception as e:
        print(e)
