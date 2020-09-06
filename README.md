# json-input-output
This is an exercise to practice input and output json file using python

Given the file data.json as your input, perform the following:

1. Create a CSV file, with a header, that contains the fullname, age, address and occupation.
	- Note: fullname is in "Firstname Lastname: format)
2. Generate statistics (in JSON format) using the following criteria and answers the following questions:
	- Use the lastname as the key.
	- How many people have the same last name?
	- How many different ages are there?
	- How many different occupations?
	
	- The output should look like:
		{
			'lastname1': {
				'count': number_of_people,
				'age': {
					'age1': occurence,
					'age2': occurence
				},
				'address': {
					'address1': occurence,
					'address2': occurence
				},
				'occupation': {
					'job1': occurence
				}
			}
		}
