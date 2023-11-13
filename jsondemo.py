import json

#
# name = ""
#
# try:
#     with open("file.json") as f:
#         name = json.load(f)
# except IOError:
#     print("first time login")
# if name != "":
#     print("welcome back " + name)
# else:
#     name = input("enteryour name...")
#     print("welcome " + name)
#
# with open("file.json", "w") as f:
#     json.dump(name, f)

# l = [1, 2, 3]
with open("file.json", "r") as f:
    # json.dump(l, f)
    l=json.load(f)

print(l)
print(type(l))