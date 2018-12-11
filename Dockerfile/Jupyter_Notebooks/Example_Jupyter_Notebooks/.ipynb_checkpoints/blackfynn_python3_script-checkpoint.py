from datetime import datetime

# time this process
time1 = datetime.now()

# IMPORTANT: change the "<collection id>" to the destination on blackfynn and the source "/folder/*" for your machine 

import os
os.system("bf upload --to=<collection id> /folder/*")

# print time
time_elapsed = datetime.now() - time1
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
print('------------------------------')
print("Finished!")

# write a file to indicate that this is finished
import os
if not os.path.exists('FINISHED.txt'):
    os.mknod('FINISHED.txt')