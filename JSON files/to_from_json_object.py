import json

# convert from JSON to Python
student_record = '{"name": "Lucy", "year" : 1, "college": "Dawson"}'
parsed_record = json.loads(student_record) # parse student records

print(parsed_record)
print(type(parsed_record))

#convert from Python to JSON
student_dict = {'name':'Lucy', 'year': 1, 'college': 'Dawson' }
student_record_json = json.dumps(student_dict)
print(student_record_json)
print(type(student_record_json))

print('\n\n')
print(json.dumps({'name':'Lucy', 'year': 1})) # dict --> JSON OBJECTS
print(json.dumps(['red', 'green', 'blue'])) # list --> ARRAYS
print(json.dumps(('apples', [1, 2, 3]))) # tuples -- > ARRAYS
print(json.dumps('hello world')) # string --> string
print(json.dumps(12)) # int --> NUMBER
print(json.dumps(12.33)) #float --> NUMBER
print(json.dumps(True)) # True  -->true
print(json.dumps(False)) # False  --> false
print(json.dumps(None)) # None  --> null

