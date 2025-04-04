import json

# convert from JSON to Python
student_record = '{"name": "Lucy", "year" : 1, "college": Dawson}'
parsed_record = json.loads(student_record) # parse student records

print(parsed_record)
print(type(parsed_record))
#convert from Python to JSON