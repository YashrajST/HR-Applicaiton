from common.hr import Designation
d1=Designation(10,"Watchman")
d1._validate_values()
js=d1.to_json()
print(js)
print("*"*30)
d1=Designation.from_json(js)
print(d1)
print("Code: ",d1.code)
print("Title: ",d1.title)
print("Exceptions: ",d1.exceptions)
print("Has exceptions: ",d1.has_exceptions)