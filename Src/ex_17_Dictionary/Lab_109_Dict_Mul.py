student_infor1= {
    "name": "Prashant",
    "age": 33,
    "address": {
        "home_address":"IND",
        "office_address":"KA"
    }
}

student_infor2= {
    "name": "Pritesh",
    "age": 39,
    "address": {
        "home_address":"GOA",
        "office_address":"KA"
    }
}

student_infor3= {
    "name": "Pritesh",
    "age": 39,
    "address": {
        "home_address":"PODI",
        "office_address":"Vizag"
    }
}

student_list = [student_infor1, student_infor2, student_infor3]
print(student_list)

print((student_list[2]["address"]["office_address"]))
