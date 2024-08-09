#!/usr/bin/env python3

# user-dir-getter v0.1.0
# made with <3 from moth.monster

# SPDX-License-Identifier: MIT-0

import sys

def getUserDir(name: str):
	validNames = ["desktop", "download", "documents", "music", "pictures", "videos"] # the folders that Linux and Windows have in common

	if name.lower() not in validNames: # validate input to fail gracefully
		print("Invalid directory name! Panicking...")
		exit()

	if sys.platform.startswith('linux'):
		import subprocess	

		result = subprocess.run("xdg-user-dir " + name.upper(), capture_output=True, shell=True) # needs to be uppercased for stupid shell reasons
		return result.stdout.decode().strip() # remove shell crap and return the actual result
	
	elif sys.platform.startswith('win'):
		from win32com.shell import shell, shellcon

		map = {"desktop":"FOLDERID_Desktop", "download":"FOLDERID_Downloads", "documents":"FOLDERID_Documents", "music":"FOLDERID_Music", "pictures":"FOLDERID_Pictures", "videos":"FOLDERID_Videos"} # map our values to KNOWNFOLDERID values
		return shell.SHGetKnownFolderPath(eval("shellcon." + map[name]), 0, 0) # TODO: remove these ugly eval shenanigans

if __name__ == '__main__': 
	print(getUserDir(input("directory name: "))) # simple testing CLI