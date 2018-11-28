#/usr/bin/python3

# Opens a video file with ffmpeg, outputs individual frames, does magic on the frames and outputs frames for Blender VSE or other video editor.

# usage: timecomp.py [--viddir 'video directory'] [--speed 'speed factor']
# [--blendstart 'frame blend start' (relative to current)] [--blendframes 'how many frames to blend']

# example:
# timecomp.py --viddir=~/video/vids --speed=2.0 --blendstart=-5 --blendframes=10
# outputs frames of vids sped up 2.0x, using 5 frames to either side of current
# frame for frame blending

# depends on ffmpeg and maybe imagemagick for frame blending

import os
import subprocess
import sys, argparse

if __name__ == "__main__":

    # take args to get vid dir, speed factor, frame blending variables
    parser = argparse.ArgumentParser()
    parser.add_argument('--viddir', default='', help='All vids in this directory will be processed')
    parser.add_argument('--speed', default='1', help='Speed factor for new frames')
    parser.add_argument('--blendstart', default='0', help='Starting frame relative to current that will be blended')
    parser.add_argument('--blendframes', default='0', help='Total number of frames to blend per final frame; 0 to disable')
    args = parser.parse_args()

    # make a temp dir to hold frames being worked on
    print(args.viddir)
    if (args.viddir == ''):
        args.viddir = os.getcwd()

    # set up temporary directory for working on frames little by little
    tempDir = args.viddir + '/temp'
    if (os.path.isdir(tempDir) == False):
        try:
            os.mkdir(tempDir)
        except OSError:
            print("Temp directory (%s) creation failed?!?" % tempDir)
        else:
            print(tempDir + " created successfully")


    print("Done!")
