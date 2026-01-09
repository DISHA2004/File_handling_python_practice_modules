import os
import shutil
# des_path= input('Enter the folder you want to arrange')
des_path= r'C:/Users/Disha/Desktop/Automated/auotmation'
#print(des_path)
# p=os.getcwd(), onlyto print what current directory you're working in and takes no argument
inside=os.listdir(des_path)
desnames=['/imagefiles','/pdfiles']
for i in range(0,2):
    if not os.path.exists(des_path+desnames[i]):
        print(des_path+desnames[i])
        p=os.path.join(des_path+desnames[i])
        os.makedirs(p)
for x in inside:
    if '.jpg' in x and not os.path.exists(des_path + '/imagefiles/'+ x):
        shutil.move(des_path+'/'+x,des_path + '/imagefiles/'+ x )
        continue
    elif '.pdf' in x and not os.path.exists(des_path + '/pdfiles/'+ x):
        shutil.move(des_path+'/'+x,des_path + '/pdfiles/'+ x )
        continue
    else:
        print('there are some not moved')
