#Deleting Unneeded Files

import os
from pathlib import Path
#import send2trash

directory = r'C:\Users\Dan\Downloads'

for folderName, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        filepath = Path(folderName) / filename
        filesize = os.path.getsize(filepath)
        if(filesize > 100000000):
            #os.unlink(filepath)
            #send2trash.send2trash(filepath)
            print('Delete: ' + str(filepath))
