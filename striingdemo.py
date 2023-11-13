# # s='''ORIGIN
# #         1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
# #        61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
# # //'''
# # # print(s)
# # with open("preproinsulin-seq.txt","w") as f:
# #     f.write(s)#
# with open("preproinsulin-seq.txt", "r") as f:
#     s=f.read()
# # print(s.split("l"))
# # print(s.find("//"))
# # print(s.count("a"))
# # print(s.startswith("Ojafksld"))
# i="     jslkdfjsdkaf      "
# # print("----"+i+"---")
# # i=i.lstrip()
# # print("----"+i+"---")
# # print(i.replace("j","A"))
# # s=s.replace("ORIGIN","")
# # s=s.replace("//","")
# s1=s[s.find("1 ")+2:s.find("aed")+3]
# s2=s[s.find("61 ")+3:s.find("ycn")+3]
# s=s1+s2
# # print(s1)
# # print(s)
# # print(s2)
#
# with open("lsinsulin-seq-clean.txt","w") as f1:
#     f1.write(s[0:25])


preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# Calculating the molecular weight of insulin
# Creating a list of the amino acid (AA) weights
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
             'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
             'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
             'V': 117.15, 'W': 204.23, 'Y': 181.19}
# Count the number of each amino acids

aaCountInsulin = dict()
l = ['A', 'C',
     'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
     'Q', 'R', 'S', 'T',
     'V', 'W', 'Y']
for x in l:
    aaCountInsulin[x] = float(insulin.upper().count(x))

# aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
#                                                                 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
#                                                                 'Q', 'R', 'S', 'T',
#                                                                 'V', 'W', 'Y']})
# Multiply the count by the weights

d = dict()
for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
     'S', 'T', 'V', 'W', 'Y']:
    d[x]=(aaCountInsulin[x] * aaWeights[x])

molecularWeightInsulin=sum(d.values())

# molecularWeightInsulin = sum({x: (aaCountInsulin[x] * aaWeights[x]) for x in
#                               ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
#                                'S', 'T', 'V', 'W', 'Y']}.values())
print("The rough molecular weight of insulin: " +
      str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(
    ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
