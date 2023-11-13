import json
from builtins import str


def readjson(filename):
    with open(filename,"r") as f:
        # data = f.read()
        data = json.load(f)
        return data


d=readjson("insulin.json")
# print(d["molecularWeightInsulinActual"])
# print(d["weights"])
# print(d["molecules"])
# for k, v in d.items():
#     print(str(k)+"---"+str(type(k)))
#     print(str(v)+"---"+str(type(v)))
# for k, v in d.items():
#     print(str(k)+"---"+str(type(k)))
#     print(str(v)+"---"+str(type(v)))

print(d["molecules"]["bInsulin"])