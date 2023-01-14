import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from FILE_HAMII_X64 import main
    main()
elif bit == '32bit':
    from FILE_HAMII_X import main
    main()
