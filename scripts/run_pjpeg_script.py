#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 23:26:32 2021

@author: lepotatoguy

This script automates the compression of multiple JPEG images using the `jpegtran` command-line tool
with a predefined progressive scan script (`script_final.txt`). It builds a batch command to:
- Process images named '1.jpg' to '4.jpg'.
- Apply progressive JPEG optimization and save each output as '<N>_p.jpg'.

The full command is executed inside a new GNOME terminal window, keeping the terminal open upon completion.

Requirements:
- `jpegtran` must be installed and accessible from the command line.
- `gnome-terminal` is required (Linux GNOME desktop environment).
"""
# https://stackabuse.com/executing-shell-commands-with-python/

import os
command="jpegtran -optimize -progressive -script_final.txt -outfile 1_p.jpg 1.jpg && jpegtran -optimize -progressive -script_final.txt -outfile 2_p.jpg 2.jpg && jpegtran -optimize -progressive -script_final.txt -outfile 3_p.jpg 3.jpg && jpegtran -optimize -progressive -script_final.txt -outfile 4_p.jpg 4.jpg" 
os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")


    

