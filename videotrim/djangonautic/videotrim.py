from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import re
from datetime import datetime
import moviepy.editor as mpe

"""
trim_start_points.append(start_time)
trim_end_points.append(end_time)
index += 1
"""

def videotrim(video_file_path, trimpoints):

    trim_start_points = []
    trim_end_points = []
    index = 0

    for i in trimpoints:
        if index%2 == 0:
            trim_start_points.append(float(i))
        else:
            trim_end_points.append(float(i))
        index += 1

    #trim video based off of start time and end time
    clip = mpe.VideoFileClip(video_file_path)
    #prevent moviepy from automatically converting portrait to landscape
    if clip.rotation == 90:
        clip = clip.resize(clip.size[::-1])
        clip.rotation = 0
    clip.ffmpeg_params = ['-noautorotate'] #doesn't seem to do anything
    # trim clips
    for i in range(int(index/2)):
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
