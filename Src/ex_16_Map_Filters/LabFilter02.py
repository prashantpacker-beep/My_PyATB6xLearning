test_result = ["PASS","FAIL","PASS","SKIP","FAIL"]

pass_give= list(filter(lambda x:x=="PASS",test_result))
print(pass_give)