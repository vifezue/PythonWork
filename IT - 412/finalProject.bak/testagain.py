sqlUpdateCustomer = 'UPDATE `crm_data` SET fName=%s,lName=%s,address=%s,city=%s,state=%s,zipcode=%s,company=%s,primaryPhone=%s\
			,secondaryPhone=%s,emailAddress=%s WHERE `fName` =%s AND `lName` =%s' % (updatedCustomer['firstName'],
                                                                                    updatedCustomer['lastName'],
                                                                                    updatedCustomer['address'],
                                                                                    updatedCustomer['city'],
                                                                                    updatedCustomer['state'],
                                                                                    updatedCustomer['zip'],
                                                                                    updatedCustomer['company_name'],
                                                                                    updatedCustomer['phone_number'],
                                                                                    updatedCustomer['phone_number_2'],
                                                                                    updatedCustomer['email'],
                                                                                    firstName,
                                                                                    lastName)
