import json 
 
 # deserialization of JSON => conversion of JSON object to intx
 #repsectuve Python object 

input_file = open('JSON files/students.json', 'r')
data = json.load(input_file) #loaded into data, from top to bottom, cursor at the bottom
print(data)

input_file.seek(0)
for line in input_file:
    print(line)
#doesnt only read line by line, turns it into dictionnary object



input_file.close()

# serialization of JSON => conversion of Python objects to JSON
# objects/strings

# output_file = open('butterflies.json', 'w')
# d = {'painted lady': 1, 'bronze cooper': 12, 'monarch': 5}
# json.dump(d, output_file)
# output_file.close()
