# import os
# res = os.system('ls -l')
from rich import inspect
import subprocess

res = subprocess.run( 
    [ "ping", "google.com", "-a" ]
  )

print(res)