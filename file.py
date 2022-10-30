import os
from os.path import basename
import shutil
from mutagen.mp3 import MP3





for subdir, dirs, files in os.walk(r'C:\Users\Anas\AppData\Local\osu!\Songs'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp3"):
            # Saving the length of the song property.
            audio = MP3(filepath)
            # Saving the directory name which we will use later to change
            # the name of the songs files(asthetically more pleasing.
            dirname = basename(os.path.dirname(filepath))
            dirname = dirname.split(' ', 1)[1]
            if audio.info.length > 29 :
                #Copying the file in the destination directory.
                shutil.copy(filepath,"D:\songs")
                destfile= os.path.join("D:\songs",file)
                dirname=os.path.join("D:\songs",dirname)
                # Renaming the files.
                os.rename(destfile,dirname + '.mp3')
