'''
Created on 09-Feb-2017
@author: Kumar Swapnil
'''
import matplotlib.pyplot as plt
import os

my_documents_path = r"C:\Users\vikram singh\Documents"
language = [1,2,3,4]
count = []

dir_list = [f.path for f in os.scandir(path=r'C:\Users\vikram singh\Documents') if f.is_dir()]
dir_list.append(my_documents_path)
for sub_dir in dir_list:
    print(sub_dir)
num_lines = [0,0,0,0]
print(len(dir_list))
for dir_name in dir_list:
    cppfileslist = []
    pythonfieslist = []
    cfileslist = []
    jsfileslist = []
    
    for file_name in os.listdir(dir_name):
        if file_name.endswith(".cpp"):
            cppfileslist.append(file_name)
        elif file_name.endswith(".py"):
            pythonfieslist.append(file_name)
        elif file_name.endswith(".c"):
            cfileslist.append(file_name)
        elif file_name.endswith(".js"):
            jsfileslist.append(file_name)
    
    '''
    now scan all lists one by one and count lines of code
    check if a line is comment or not.. and exclude it
    also check for a blank line :)
    '''            
    
    
    for file_name in cppfileslist:
        print(file_name)
        x = dir_name+ '\\' + file_name
        print(x.__str__())
        num_lines[0] = num_lines[0] + sum(1 for line in open(x,encoding='utf8'))
        print(num_lines)
    #count.append(num_lines)
    
    #num_lines = 0
    for file_name in pythonfieslist:
        print(file_name)
        num_lines[1] = num_lines[1] + sum(1 for line in open(dir_name+ '\\' + file_name,encoding='utf8'))
        print(num_lines)
    #count.append(num_lines)
    
    #num_lines = 0
    for file_name in cfileslist:
        print(file_name)
        num_lines[2] = num_lines[2] + sum(1 for line in open(dir_name+ '\\' + file_name,encoding='utf8'))
        print(num_lines)
    #count.append(num_lines)

    #num_lines = 0
    for file_name in jsfileslist:
        print(file_name)
        num_lines[3] = num_lines[3] + sum(1 for line in open(dir_name+ '\\' + file_name,encoding='utf8'))
        print(num_lines)
    #count.append(num_lines)
    

#plotting starts
plt.scatter(language,num_lines)
plt.xlabel('Language')
plt.ylabel('Lines Of Code')
plt.xticks([1,2,3,4],['C++','Python','C','Javascript'])
plt.show()
