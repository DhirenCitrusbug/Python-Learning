import csv
  
employee_info = ['emp_id', 'emp_name', 'skills']
  
new_dict = [
{'emp_id': 456, 'emp_name': 'George', 'skills': 'Python'},
{'emp_id': 892, 'emp_name': 'Adam', 'skills': 'Java'},
{'emp_id': 178, 'emp_name': 'Gilchrist', 'skills': 'Mongo db'},
{'emp_id': 155, 'emp_name': 'Elon', 'skills': 'Sql'},
{'emp_id': 299, 'skills': 'Ruby','emp_name': 'Mask' },
]
  
with open('test4.csv', 'r+') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = employee_info)
    writer.writeheader()
    writer.writerows(new_dict)
    csvfile.seek(0)
    r = csv.DictReader(csvfile)
    print(list(r))

employee_info = ['emp_id', 'emp_name', 'skills']
  
with open('mycsv.csv', 'w', newline='') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])