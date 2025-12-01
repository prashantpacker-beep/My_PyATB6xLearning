import os
print(os.getcwd())
full_path = os.path.join(os.getcwd(),"prashant.txt")
print(full_path)

file= open(full_path,"r")
print(file.read())