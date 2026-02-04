#python is a dnamically typed language and the data types are defined while run time
#we can add type hints to variables which helps to understand while data type is that particular variable is expecting

#Eg:


num : int = 10
decimal : float = 1.0
flag : bool = False
numbers : list[int] = [1,2,3,6,5,4] #list with integers
list1: list[int | str] = [15,"january",2000] # pipe operator for multiple expectations

date: tuple[int,...] = (10,5,2024) #as it expects multiple integer values (for tuple ... should be used)

dictionary: dict[str ,str | int] = {
  "state" : "Kerala",
  "dist" : "Tvm",
  "pincode": 545454
}

class City:
  def __init__(self,location,pincode):
    self.location = location
    self.pincode = pincode   
  
Delhi: object = City("Delhi",524156) 

Location : list[City, float] = [Delhi, 25.0] #City class instance is expected (list[object,float] is also acceptable) 

def get_value(num: int,exp: int | float | None) -> float:
  return pow(num , .5 if exp is None else exp)

print(get_value(25, None))


