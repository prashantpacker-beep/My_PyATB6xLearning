
try:

 with open('testdata.txt','r') as file:
    #content= file.readline() list format
    content= file.read()
    print(content)
except FileNotFoundError as fnfe:
    print(fnfe)


