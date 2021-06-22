#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 23:26:32 2021

@author: joyanta.csebracu
"""
# https://stackoverflow.com/questions/43332703/open-terminal-run-command-python

import os
command="jpegtran -optimize -progressive -script_final.txt -outfile 1_p.jpg 1.jpg && jpegtran -optimize -progressive -script_final.txt -outfile 2_p.jpg 2.jpg && jpegtran -optimize -progressive -script_final.txt -outfile 3_p.jpg 3.jpg && jpegtran -optimize -progressive -script_final.txt -outfile 4_p.jpg 4.jpg" 

os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
    


    

