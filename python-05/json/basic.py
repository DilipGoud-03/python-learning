import json

x ={"name":"Dilip","age" :23,"city" : "Ujjain"}

y = json.dumps(x,indent=3)

print(y)
parse_y = json.loads(y)
del parse_y
print(y)



print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 