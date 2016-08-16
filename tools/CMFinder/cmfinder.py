import glob, os, sys
import shutil
from shutil import copyfile
import subprocess
from os import system

def sh(script):
    system("bash -c '%s'" % script)


#print sh("pwd")


input_dir = sys.argv[1]


#path = input_dir + '/*/MODEL/*'
path = input_dir + '/CLUSTER/*/MODEL/*'
treePath =    input_dir + '/CLUSTER/*/TREE/mloc/results'
#path = '/home/sokhoyae/Desktop/GalaxyProject/galaxy/tools/CMFinder/CLUSTER/*/MODEL/*'
files=glob.glob(path)
#output = ""

#subprocess.call("/home/sokhoyae/Desktop/GalaxyProject/galaxy/tools/CMFinder/cmfinder --g 1.0 -a /home/sokhoyae/Desktop/GalaxyProject/galaxy/tools/CMFinder/CLUSTER/1.1.cluster/MODEL/model.tree.stk /home/sokhoyae/Desktop/GalaxyProject/galaxy/tools/CMFinder/CLUSTER/1.1.cluster/MODEL/cmfinder.fa output", shell=True)


#~ for i in range(0, len(files), 2):


     #~ directory, sep, name = files[i].rpartition('/')
     #~ print "dir = ", directory
     #~ os.popen("/home/sokhoyae/Desktop/GalaxyProject/galaxy/tools/CMFinder/cmfinder --g 1.0 -a "+files[i] + " " + files[i+1] + " " + directory + "/output > " + directory +"/model.cmfinder.stk && rm " + directory + "/output")
     #~ if os.stat(directory +"/model.cmfinder.stk").st_size == 0 :

		#~ #copyfile(src, dst)

		#~ sh("cd "+ directory + "; cd ../TREE/mloc/results; cp -v result.aln " + directory +"/model.cmfinder.stk")

		#~ print "pwdic araj"
		#~ print sh("pwd")

for i in range(0, len(files), 2):


     directory, sep, name = files[i].rpartition('/')
     updir, sep, tail = directory.rpartition('/')

     cmd = "cd "+ directory + "; pwd;  cp -f ../TREE/mloc/results/result.aln " +  "model.cmfinder.stk"
     print cmd
     sh(cmd)

     alifoldCmd = "cd "+ directory +" ; perl ../../../alifold.pl -file  ../TREE/mloc/results/result.aln"
     sh(alifoldCmd)

     cmd_stk = "perl mloc2stockholm.pl -file " + directory + "/model.cmfinder.stk  -split_input yes  --con_struct " + updir + "/TREE/mloc/results/result.aln.alifold"
     ##test##cmd_stk = "perl mloc2stockholm.pl -file " + directory + "../TREE/mloc/results/result.aln  -split_input yes  --con_struct " + updir + "/TREE/mloc/results/result.aln.alifold"
     sh(cmd_stk)

     #print "dir = ", directory

     #print updir
     sh("rm -f $model_dir/model.cmfinder.stk");

     #os.popen("/home/eteri/GalaxyProject/galaxy/tools/CMFinder/cmfinder --g 1.0 -a "+files[i] + " " + files[i+1] + " " + directory + "/output > " + directory +"/model.cmfinder.stk && rm " + directory + "/output")
     os.popen("/home/eteri/GalaxyProject/galaxy/tools/CMFinder/cmfinder --g 1.0 -a "+files[i] + " " + files[i+1] + " " + directory + "/output ")# + directory +"/model.cmfinder.stk && rm " + directory + "/output")
     if os.path.isfile(directory + '/output') :
        copyfile(directory +"/output", directory +"/model.cmfinder.stk")
        sh("rm " + directory+ "/output")
        sh("rm " + directory+ "/model.cmfinder.stk.sth")
     else :
        copyfile(directory + "/model.cmfinder.stk.sth", directory +"/model.cmfinder.stk")
        sh("rm " + directory+ "/model.cmfinder.stk.sth")

    #  if os.stat(directory +"/output").st_size > 0 :
	# 	copyfile(directory +"/output", directory +"/model.cmfinder.stk")




directory, sep, name = path.rpartition('CMFinder/')
clst, sep, tail = name.partition('/')

shutil.make_archive('CLUSTER', 'zip', clst)
