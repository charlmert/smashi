import os
import shutil

def cp(src, dest):
    # Recursively copy directory to dest
    if (not os.path.isfile(src)):
        try:
            shutil.copytree(src, dest)
        # Directories are the same
        except shutil.Error as e:
            raise Exception('Could not copy directory: %s' % e)
        # Any error saying that the directory doesn't exist
        except OSError as e:
            raise Exception('Could not copy directory: %s' % e)
