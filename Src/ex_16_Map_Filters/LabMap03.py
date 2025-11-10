response_time_ms = [1200,1500,1800]

def mil_sec(x):
    return x/1000
response_time_s= list(map(mil_sec, response_time_ms))
print(response_time_s) 
