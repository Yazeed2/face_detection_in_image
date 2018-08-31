import os
import os.path
import shutil 

path = '.'
files = os.listdir(path)
i = 1
for file in files:	
    if file.endswith(".JPG"):	
    	os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.JPG'))
    	i = i+1
