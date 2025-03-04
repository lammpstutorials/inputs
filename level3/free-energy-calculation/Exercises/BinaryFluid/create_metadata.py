# create metadata file for WHAM algorithm
import os

k=1.5 # set the value of  k in kCal/mol

folder='data-particle1/'
f = open("metadata-particle1.dat", "w")
for n in range(-50,50):
    datafile=folder+'position.'+str(n)+'.dat'
    if os.path.exists(datafile):
        # read the imposed position is the expected one
        with open(datafile) as g:
            _ = g.readline()
            _ = g.readline()
            firstline = g.readline()
        imposed_position = firstline.split(' ')[-1][:-1]
        # write one file per file
        f.write(datafile+' '+str(imposed_position)+' '+str(k)+'\n')
f.close()

folder='data-particle2/'
f = open("metadata-particle2.dat", "w")
for n in range(-50,50):
    datafile=folder+'position.'+str(n)+'.dat'
    if os.path.exists(datafile):
        # read the imposed position is the expected one
        with open(datafile) as g:
            _ = g.readline()
            _ = g.readline()
            firstline = g.readline()
        imposed_position = firstline.split(' ')[-1][:-1]
        # write one file per file
        f.write(datafile+' '+str(imposed_position)+' '+str(k)+'\n')
f.close()
