# import csv
# import copy
# myVehicle = {
#     "vin" : "<empty>",
#     "make" : "<empty>" ,
#     "model" : "<empty>" ,
#     "year" : 0,
#     "range" : 0,
#     "topSpeed" : 0,
#     "zeroSixty" : 0.0,
#     "mileage" : 0
# }
#
# # for key, value in myVehicle.items():
# #     print("{} : {}".format(key,value))
#
#
# myInventoryList = []
#
# with open('car.csv') as csvFile:
#     csvReader = csv.reader(csvFile, delimiter=',')
#     lineCount = 0
#     for row in csvReader:
#         if lineCount == 0:
#             # print(f'Column names are: {", "+str(row)}')
#             # print(f'Column names are: {", ".join(row)}')
#             lineCount += 1
#         else:
#             # print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
#             currentVehicle = copy.deepcopy(myVehicle)
#             currentVehicle["vin"] = row[0]
#             currentVehicle["make"] = row[1]
#             currentVehicle["model"] = row[2]
#             currentVehicle["year"] = row[3]
#             currentVehicle["range"] = row[4]
#             currentVehicle["topSpeed"] = row[5]
#             currentVehicle["zeroSixty"] = row[6]
#             currentVehicle["mileage"] = row[7]
#             myInventoryList.append(currentVehicle)
#             # lineCount += 1
#     # print(f'Processed {lineCount} lines.')
#

for x in range(1,20):
    print(x)

#
# for x in myInventoryList:
#     print(x)
#     for k,v in x.items():
#         print("key is -----"+str(k))
#         print("value is -----"+str(v))
#     print("-----------")
#
#
#     # 1 2 foo 4 bar foo 7 8 foo 10 11 foo 13 14 foobar
#
#


# def myfunc(a=1):
#     print(a)
#     return a + a
#
#
# def myfunc(a, b):
#     return a + b
#
#
# # print(myfunc("aaa"))
# # i = myfunc(10)
# # print(i)
# # myfunc()
# print(myfunc(a=10, b=20))


# no arg + no return type
# def show1():
#     print("no arg no return")
# # arg + no return type
# def show2(a):
#     print(str(a)+"--- arg but no return")
# # arg + return type
# def show3(a):
#     print(str(a)+"--- arg and return")
#     return a+a
#     print("-----")
# # no arg + return type
# def show4():
#     print("no arg and return")
#     return "---"
#
#
# i=30
# show1()
# show2(i)
# print(show3(20))
# print(show4())
# # show4()


def add(a,b):
    return a+b

# 10 20 30 40

# print(add(add(30,50),add(10,20)))
print("---")


