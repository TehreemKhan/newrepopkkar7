# # fh1=open("test.txt","a")
# # # s=fh1.read()
# # # print(s+s)
# # fh1.write("from code")
# # fh1.close()
#
try:
    with open("test.txt", "r") as fh:
        # fh.write("jjjjjlkjkl")
        print(fh.read())
except FileNotFoundError:
    print("handled")

# s = [1, 2, 3]
# try:
#     # print(s[0])
#     print(10 / 0)
#
# # except ZeroDivisionError:
# except ZeroDivisionError:
#     print("except call ZeroDivisionError error")
# except ArithmeticError:
#     print("except call arithmetic error")
# finally:
#     print("finally run")
# print("end of file")
