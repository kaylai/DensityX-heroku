import os, time, sys

path = os.path.dirname(os.path.dirname(os.path.abspath('media')))

now = time.time()

for f in os.listdir(path):
	if os.stat(os.path.join(path,f)).st_mtime < now - 7 * 86400:
  		if os.path.isfile(f):
   			os.remove(os.path.join(path, f))