# A script which install the vim plugins and configuration on the current system.
# This script assumes that vim is already installed, with the appropriate python and ruby
# additions. 

# This installation is done by symlinking the .vim folder and the .vimrc file
# This will create a backup folder for the previous vim stuff, so the user can return
# to the previous state if anything goes wrong.

import os
import os.path
import shutil


home = os.path.expanduser("~")
vimfolder = os.path.dirname(os.path.realpath(__file__))
backupfolder = vimfolder + "_bak"

# Backup the .vim folder and the .vimrc file if they exist.
def backupPrevious():
    if not os.path.exists(home + "/.vim"):
        return
    if os.path.exists(backupfolder):
        shutil.rmtree(backupfolder)
        os.makedirs(backupfolder)
    shutil.copytree(home + "/.vim", backupfolder + "/.vim") 
    if os.path.exists(home + "/.vimrc"):
        shutil.copy2(home + "/.vimrc", backupfolder + "/.vimrc")

def removePrevious():
    folder = home + "/.vim"
    if os.path.exists(folder):
        if os.path.islink(folder):
            os.unlink(folder)
        else:
            shutil.rmtree(folder)


backupPrevious()

