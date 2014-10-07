import os

def function():
    vol=raw_input("Plaese Input the Volume which to lock:")
    cmd='manage-bde -lock '+vol+':'
    fp=os.popen(cmd)
    res=fp.read()
    stat=fp.close()
    print "____________________________________________________________________"
    zy=res.find('-ForceDismount')
    if zy>0:
        crtl=raw_input("This Volume is used ,Force to lock?(Y/N)")
        if (crtl=='Y') or ((crtl=='y')):
            cmd='manage-bde -lock '+vol+': -ForceDismount'
            fp=os.popen(cmd)
            res=fp.read()
            stat=fp.close()
            print res
            return
    else :
        print res
        return


print "Kuroko Bitlocker Administrate Software"
print "--Chiruom Lab  2014.4.12  Vision 1.0--"

print "____________________________________________________________________"

function()
print "____________________________________________________________________"
while(True):
    c=raw_input("Press 'C' before 'Enter' to continue or any key to quit...")
    if c=='c' or c=='C' :
        function()
        print "____________________________________________________________________"
    else:
        print "Thanks!"
        break
