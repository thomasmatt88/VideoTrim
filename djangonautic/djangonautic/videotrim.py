from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import re
from datetime import datetime
import moviepy.editor as mpe
import tkinter as tk
from tkinter.filedialog import askopenfilename

video_file_path = ''

def open_file():
    global video_file_path
    video_file_path = askopenfilename()

#prompt user for video file
root = tk.Tk()
button = tk.Button(root, text = "open video file", command = open_file)
button.pack()
root.mainloop()

#extract metadata from video file
parser = createParser(video_file_path)
metadata = extractMetadata(parser)
print(metadata)

#extract creation date from metadata
metadata_string = str(metadata)
start = "Creation date: "
end = "\n"
time_string = re.search('%s(.*)%s'%(start, end), metadata_string).group(1)
#convert time_string to datetime object
video_creation_datetime = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

Trim = True
trim_start_points = []
trim_end_points = []
index = 0

while Trim == True:
    
    #prompt user for start/end points for video trimming
    start_time = input('Start Time %Y-%m-%d %H:%M:%S? ')                  
    end_time = input('End Time %Y-%m-%d %H:%M:%S? ')

    trim_start_points.append(start_time)
    trim_end_points.append(end_time)
    index += 1

    #prompt user if they want to Trim again
    answer = input("Do you want to trim another clip from video (True or False)?")
    if answer == "True":
        Trim = True
    elif answer == "False":
        Trim = False
    

try:
    #convert start_time and end_time strings to datetime objects
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    #subtract video creation date from data start date and end date in order to get elapsed times
    #convert elapsed timedelta objects into floats
    start_time = (start_time - video_creation_datetime).total_seconds()
    end_time = (end_time - video_creation_datetime).total_seconds()

except:
    #if user input not in datetime format, convert to int
    #for i in range(index):
        #start_time = int(trim_start_points[i])
        #end_time = int(trim_end_points[i])
    pass

#trim video based off of start time and end time
clip = mpe.VideoFileClip(video_file_path)
#prevent moviepy from automatically converting portrait to landscape
if clip.rotation == 90:
    clip = clip.resize(clip.size[::-1])
    clip.rotation = 0
clip.ffmpeg_params = ['-noautorotate'] #doesn't seem to do anything
# trim clips
for i in range(index):     
    edited_clip_one = clip.subclip(int(trim_start_points[i]), int(trim_end_points[i]))
    #edited_clip_two = clip.subclip(start_time_two, end_time_two)
    #concatentate clips
    if i == 0:
        final_edited_clip = edited_clip_one
    else:
        final_edited_clip = mpe.concatenate_videoclips([final_edited_clip, \
                                                           edited_clip_one])


final_edited_clip.ffmpeg_params = ['-noautorotate'] #doesn't seem to do anything
# recommended settings for youtube
final_edited_clip.write_videofile(filename = "utc_clip.mp4", \
                                  codec = "libx264", audio_codec = "aac")
                                #bitrate = 10 Mbps for 30 FPS and 15 Mbps for 60 fps
