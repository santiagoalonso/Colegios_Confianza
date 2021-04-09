from __future__ import division
import matplotlib.pyplot as plt
import json
import re
import os








#Change file names
#dataDir = "/Users/santiagoalonsodiaz/Google Drive/JaverianaGD/Cognicion matematica/Colegios/Data/Cole_CAFAM/"
dataDir = "/Users/santiagoalonsodiaz/Desktop/Temp/"
filenames = os.listdir(dataDir + "RATIO Y NUM/CUARTO/")
filenames = sorted(filenames)
filenamesCog = os.listdir(dataDir + "RAVEN - ACTMATH-MEMORIA/Cuarto/")
filenamesCog = sorted(filenamesCog)


filenames_ratio = []
filenames_num = []
for fn in filenames:
    x = re.search(".*_RATIO_data.json", fn)
    if (x):
        filenames_ratio.append(fn)
    x = re.search(".*_NUM_data.json", fn)
    if (x):
        filenames_num.append(fn)

filenames_mem = []
filenames_act = []
filenames_rav = []
for fn in filenamesCog:
    x = re.search(".*_actMat.json", fn)
    if (x):
        filenames_mem.append(fn)
    x = re.search(".*_DigitSpan_data.json", fn)
    if (x):
        filenames_act.append(fn)
    x = re.search(".*_Raven.json", fn)
    if (x):
        filenames_rav.append(fn)




filenames_ratio_rename = []
filenames_num_rename = []
filenames_ratio_renamefail = []
filenames_num_renamefail = []
subjCounter = 1
for fr in filenames_ratio:
    fr2 = fr.upper().replace(" ", "")
    fr2 = re.split("\B_RATIO_DATA.JSON", fr2)[0]
    fr2 = ''.join([i for i in fr2 if not i.isdigit()])
    #print(x)
    check = 0
    for fn in filenames_num:
        fn2 = fn.upper().replace(" ","")
        fn2 = re.split("\B_NUM_DATA.JSON", fn2)[0]
        fn2 = ''.join([i for i in fn2 if not i.isdigit()])
        for fm in filenames_mem:
            fm2 = fm.upper().replace(" ", "")
            fm2 = re.split("\B_DIGITSPAN_DATA.JSON", fm2)[0]
            fm2 = ''.join([i for i in fm2 if not i.isdigit()])
            for frv in filenames_rav:
                frv2 = frv.upper().replace(" ", "")
                frv2 = re.split("\B_RAVEN.JSON", frv2)[0]
                frv2 = ''.join([i for i in frv2 if not i.isdigit()])
                for fa in filenames_act:
                    fa2 = fa.upper().replace(" ", "")
                    fa2 = re.split("\B_ACTMAT.JSON", fa2)[0]
                    fa2 = ''.join([i for i in fa2 if not i.isdigit()])
                    if fn2 == fr2 and fn2 == fm2 and fn2 == frv2 and fn2 == fa2:
                        os.rename(dataDir + "RATIO Y NUM/CUARTO/" + fr,
                                  dataDir + "RATIO Y NUM/CUARTO_RENAME/CuartoR_" + subjCounter.__str__() + ".json")
                        os.rename(dataDir + "RATIO Y NUM/CUARTO/" + fn,
                                  dataDir + "RATIO Y NUM/CUARTO_RENAME/CuartoN_" + subjCounter.__str__() + ".json")

                        os.rename(dataDir + "RAVEN - ACTMATH-MEMORIA/Cuarto/" + fm,
                                  dataDir + "RAVEN - ACTMATH-MEMORIA/CUARTO_RENAME/CuartoMem_" + subjCounter.__str__() + ".json")
                        os.rename(dataDir + "RAVEN - ACTMATH-MEMORIA/Cuarto/" + frv,
                                  dataDir + "RAVEN - ACTMATH-MEMORIA/CUARTO_RENAME/CuartoRaven_" + subjCounter.__str__() + ".json")
                        os.rename(dataDir + "RAVEN - ACTMATH-MEMORIA/Cuarto/" + fa,
                                  dataDir + "RAVEN - ACTMATH-MEMORIA/CUARTO_RENAME/CuartoAct_" + subjCounter.__str__() + ".json")

                        subjCounter = subjCounter + 1
                        check = 1







filenames_ratio_rename[3]
filenames_ratio_renamefail[2]





filenames_ratio_rename.__len__()
filenames_ratio_renamefail.__len__()
filenames_num_rename.__len__()


a =   filenames_ratio[0].upper().replace(" ","")
b =   filenames_num[0].upper().replace(" ","")


a
b
a==b


filenames_ratio
len(filenames_ratio)
len(filenames_num)

filenames_ratio[0]
filenames_num[0]



#Check if "ain" is present at the beginning of a WORD:


str = "The rain in Spain"
str2 = "The rain in Spain"

str == str2

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", str)

print(x)


str = "The rain in Spain_Ratio"

#Check if the string starts with "The":

x = re.split("\B_Ratio", str)
print(x)
re.findall("\_Ratio", str)







sID = 'RA1'
with open('/Users/santiagoalonsodiaz/Google Drive/JaverianaGD/Cognicion matematica/RatioAdapt/Data9050discrete/' + sID + '_RATIO_data.json') as f:
    d = json.load(f)
    #print(d)

ntrials = len(d)
d[1].keys()