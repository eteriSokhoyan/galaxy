import glob, os, sys
import shutil
from shutil import copyfile
from os import system
import re
#from sklearn.metrics.cluster import completeness_score
#from sklearn.metrics.cluster import homogeneity_score
from sklearn import metrics

def sh(script):
    system("bash -c '%s'" % script)

dataNames = sys.argv[1]



listOfClusters = []
listOfClasses = []

cluster_seqs_stats_path = "RESULTS/*/cluster.seqs.stats"
cluster_seqs_stats_files = glob.glob(cluster_seqs_stats_path)

blackList =[]
numberOfClusters = 0
for singleFile in sorted(cluster_seqs_stats_files):
    numberOfClusters += 1
    with open(singleFile, "r") as f:
        for line in f.readlines():
            uniqueId = line.split()[4]
            #print uniqueId
            clustNum = line.split()[1]
            rnaClass, sep, tail = uniqueId.partition("_")
            #classToClusterDict[rnaClass] = clustNum
            listOfClasses.append(rnaClass)
            listOfClusters.append(clustNum)
            #print rnaClass
            #print clustNum


            with open(dataNames, "r") as names:
                for nameLine in names.readlines():
                    fullUniqeId = nameLine.split()[3]
                    #print fullUniqeId
                    #rnaClass, sep, tail = fullUniqeId.partition("_")
                    if fullUniqeId == uniqueId:
                        blackList.append(uniqueId)

print "numberOfClusters = " ,numberOfClusters
numberOfClusters += 1 ### 1 cluster for all anassigned seqs
with open(dataNames, "r") as names:
    for nameLine in names.readlines():
        fullUniqeId = nameLine.split()[3]
        rnaClass, sep, tail = fullUniqeId.partition("_")
        #print fullUniqeId
        #rnaClass, sep, tail = fullUniqeId.partition("_")
        if fullUniqeId not in blackList:
            #numberOfClusters += 1 ### separate cluster for all anassigned seqs
            listOfClasses.append(rnaClass)
            listOfClusters.append(numberOfClusters)



completeness_score = metrics.completeness_score(listOfClasses, listOfClusters)
homogeneity_score = metrics.homogeneity_score(listOfClasses, listOfClusters)
adjusted_rand_score = metrics.adjusted_rand_score(listOfClasses, listOfClusters)
adjusted_mutual_info_score = metrics.adjusted_mutual_info_score(listOfClasses, listOfClusters)
v_measure_score = metrics.v_measure_score(listOfClasses, listOfClusters)

toWrite = "completeness_score : " + str(completeness_score) + "\n" + "homogeneity_score : " + str(homogeneity_score) + "\n" + "adjusted_rand_score : " +str(adjusted_rand_score)  + "\n" + "adjusted_mutual_info_score : " + str(adjusted_mutual_info_score)+ "\n" + "v_measure_score : " + str(v_measure_score)

with open("RESULTS/evaluation.txt", "w") as fOut:
    fOut.write(toWrite)



print "compl_score = ", completeness_score, "\n"
print "homog_score = ", homogeneity_score , "\n"
print "v_measure_score = ", v_measure_score , "\n"
print "adjusted_rand_score = ", adjusted_rand_score , "\n"
print "adjusted_mutual_info_score = ", adjusted_mutual_info_score , "\n"
