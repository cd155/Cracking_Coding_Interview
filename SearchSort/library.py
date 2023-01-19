# convert input to a dictionary
def convToDictBaseIndex(lis, dic, i):
    for ele in lis:
        if ele[i] in dic: 
            dic[ele[i]].append(ele)
        else:
            dic[ele[i]] = [ele]
    return dic
