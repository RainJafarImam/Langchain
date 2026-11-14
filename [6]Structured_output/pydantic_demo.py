#basic flow
'''from pydantic import BaseModel
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Student(BaseModel):
    name:str

new_student={'name':32}
student=Student(**new_student)


print(student)'''


#default vlaues
'''
from pydantic import BaseModel
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Student(BaseModel):
    name:str ='jafar'

new_student={}
student=Student(**new_student)


print(student)
'''


#optional fields
"""
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Student(BaseModel):
    name:str ='jafar'
    age:Optional[int]= None


#new_student={}
new_student={'age':21}


student=Student(**new_student)


print(student)
"""


#Corece :tyr to understand the type and convert it to the required type

'''
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Student(BaseModel):
    name:str ='jafar'
    age:Optional[int]= None


#new_student={}
new_student={'age':'21'}#age is int 


student=Student(**new_student)


print(student)

#output: name='jafar' age=21
'''


#Built in validators:it can be used to validate the data before creating the model instance. It can be used to check if the data is valid or not. If the data is not valid, it will raise a ValidationError.

'''
from pydantic import BaseModel,EmailStr
from typing import Optional
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Student(BaseModel):
    name:str ='jafar'
    age:Optional[int]= None
    email:EmailStr


#new_student={}
new_student={'age':'21', 'email':'abc@example.com'}#age is int 


student=Student(**new_student)


print(student)'''


#field Functions: it can be used to define the fields of the model. It can be used to define the type of the field, the default value of the field, and the validators of the field.

'''
from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Student(BaseModel):
    name:str ='jafar'
    age:Optional[int]= None
    email:EmailStr
    cgpa:float =Field(gt=0,lt=10,description="CGPA should be between 0 and 10",default=5)#gt:greater than, lt:less than


#new_student={}
new_student={'age':'21', 'email':'abc@example.com', 'cgpa':6}#age is int 


student=Student(**new_student)


print(student)

'''


#pydantic typr to dict or json 

from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Student(BaseModel):
    name:str ='jafar'
    age:Optional[int]= None
    email:EmailStr
    cgpa:float =Field(gt=0,lt=10,description="CGPA should be between 0 and 10",default=5)#gt:greater than, lt:less than


#new_student={}
new_student={'age':'21', 'email':'abc@example.com', 'cgpa':6}#age is int 


student=Student(**new_student)


student_dict=dict(student)
student_json=student.model_dump_json()


print(student_dict)
print(student_json)
print(type(student_dict))

print(type(student_json))
