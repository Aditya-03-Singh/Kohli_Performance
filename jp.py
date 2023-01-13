#------------first--------------->
# rtavnglist2d = [
#     ["spiderman",8],
#     ["groot",7],
#     ["Black widow", 8]
# ]
# print("the value are: ",rtavnglist2d)

# for i in rtavnglist2d:
#     for j in i:
#         print(j)


#-------------------------second------------------->

# employee = {
#     "name": "Aditya kumar Singh",
#     "emp_id":3,
#     "address": [
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "wb",
#             "pincode": "984805"
#         },
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "eb",
#             "pincode": "898090"
#         }
#     ]
# }

# for i in range (len(employee["address"])):
#     print(employee["address"] [i] ["pincode"])

#---------------------third-------------------------->


    
# employee = [
#     {
#      "name": "Aditya kumar Singh",
#      "emp_id":3,
#      "address": [
#          {
#              "line1": "fff",
#              "line2": "hhh",
#              "state": "wb",
#              "pincode": "984805"
#          },
#          {
#            "line1": "fff",
#              "line2": "hhh",
#              "state": "eb",
#              "pincode": "898090"
#          }
#      ]

# },
# {
#     "name": "iron",
#      "emp_id":3,
#      "address": [
#          {
#              "line1": "fff",
#              "line2": "hhh",
#              "state": "wb",
#              "pincode": "984805"
#          },
#          {
#            "line1": "fff",
#              "line2": "hhh",
#              "state": "eb",
#              "pincode": "898090"
#          }
#      ]
# }
# ]

# emp_pin_list = []
# for emp in employee:
#     emp_pin_list.append({"name":emp["name"]})
#     emp_pin_list[employee.index(emp)]["pincode"] = []
#     for address in emp["address"]:
#         emp_pin_list[employee.index(emp)]["pincode"].append(address)

# print(emp_pin_list)



# def multi( x,  y):
#     result = x*y
#     print(result)

# multi(45,67)




  
def bubble_sort(list1):  
      
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
  
print("The sorted list is: ", bubble_sort(list1)) 


    






