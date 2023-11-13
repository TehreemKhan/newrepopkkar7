import os
import subprocess
# s = input("enter any command to run on shell")
# os.system(s)

# subprocess.run(["ls", "-l"])
# s = "g1 g2 g3"
#
# l=s.split(" ")
# print(l[0:-1])
# # print(l)
s="ps"
i="-aux"
subprocess.run([s,i])

# print(type(l))
print("----")