import subprocess
import os

def sh(cmd, input=""):
    rst = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input.encode("utf-8"))
    assert rst.returncode == 0, rst.stderr.decode("utf-8")
    return rst.stdout.decode("utf-8")

s1 = sh('cat /etc/issue')

p1 = sh('python3 --version')
p2 = sh('jupyter notebook --version')
p3 = sh('jupyter lab --version')
p4 = sh('pip3 --version')
p5 = sh('pip3 freeze | grep pandas')
p6 = sh('pip3 freeze | grep matplotlib')
p7 = sh('pip3 freeze | grep numpy')
p8 = sh('pip3 freeze | grep scipy')

r1 = sh('R --version')
r2 = sh('pip3 freeze | grep rpy2')

print('')
print('########## System ###########')
print(s1)

print('########## Python ###########')
print(p1, 'jupyter notebook =', p2, 'jupyter lab =', p3, p4, p5, p6, p7, p8)

print('')
print('########## R ################')
print(r1, r2)

# remove single files
if os.path.exists('results_versions.txt'):
    os.remove('results_versions.txt')

# create a file
if not os.path.exists('results_versions.txt'):
    os.mknod('results_versions.txt')

# append data and some new lines
file = open('results_versions.txt','a')
file.write('\n')
file.write('######### System ########')
file.write('\n')
file.write(s1)
file.write('######### Python ########')
file.write('\n')
file.write(p1)
file.write('jupyter notebook = ' + p2)
file.write('jupyter lab = ' + p3)
file.write(p4)
file.write(p5)
file.write(p6)
file.write(p7)
file.write(p8)
file.write('\n')
file.write(r1)
file.write(r2)
file.write('\n')
file.close()
