# -*- coding: utf-8 -*-
"""

@author: joyanta.csebracu
"""

import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 18})


#data = pd.read_csv('data_desktop.csv')
data = pd.read_csv('data_mobile.csv')


# =============================================================================

# Here, we will compare desktop versions. 

# =============================================================================

# pic 1

#pic1 = data[['Picture','color.jpg','color_p_img1_1.jpg','color_p_img2_1.jpg','color_p_img3_1.jpg','color_p_img4_1.jpg',
#            'color_p_img5_1.jpg','color_p_img6_1.jpg','color_p_img7_1.jpg','color_p_img8_1.jpg',]]
#
#x_indexes = np.arange(len(pic1['Picture']))
#width = 0.1
#plt.bar(x_indexes-(width*3),pic1['color_p_img1_1.jpg'],width=width)
#plt.bar(x_indexes-(width*2),pic1['color_p_img2_1.jpg'],width=width)
#plt.bar(x_indexes-width,pic1['color_p_img3_1.jpg'],width=width)
#plt.bar(x_indexes,pic1['color_p_img4_1.jpg'],width=width)
#plt.bar(x_indexes+width,pic1['color_p_img5_1.jpg'],width=width)
#plt.bar(x_indexes+(width*2),pic1['color_p_img6_1.jpg'],width=width)
#plt.bar(x_indexes+(width*3),pic1['color_p_img7_1.jpg'],width=width)
#plt.bar(x_indexes+(width*4),pic1['color_p_img8_1.jpg'],width=width)
#
#plt.xticks(ticks=x_indexes, labels= pic1['Picture'])

# pic 2

# =============================================================================
# pic2 = data[['Picture','image3.jpg','image3_p_img1_1.jpg','image3_p_img2_1.jpg','image3_p_img3_1.jpg','image3_p_img4_1.jpg',
#             'image3_p_img5_1.jpg','image3_p_img6_1.jpg','image3_p_img7_1.jpg','image3_p_img8_1.jpg',]]
# 
# x_indexes = np.arange(len(pic2['Picture']))
# width = 0.1
# plt.bar(x_indexes-(width*3),pic2['image3_p_img1_1.jpg'],width=width)
# plt.bar(x_indexes-(width*2),pic2['image3_p_img2_1.jpg'],width=width)
# plt.bar(x_indexes-width,pic2['image3_p_img3_1.jpg'],width=width)
# plt.bar(x_indexes,pic2['image3_p_img4_1.jpg'],width=width)
# plt.bar(x_indexes+width,pic2['image3_p_img5_1.jpg'],width=width)
# plt.bar(x_indexes+(width*2),pic2['image3_p_img6_1.jpg'],width=width)
# plt.bar(x_indexes+(width*3),pic2['image3_p_img7_1.jpg'],width=width)
# plt.bar(x_indexes+(width*4),pic2['image3_p_img8_1.jpg'],width=width)
# 
# plt.xticks(ticks=x_indexes, labels= pic2['Picture'])
# =============================================================================


# pic 3


# pic3 = data[['Picture','image4.jpg','image4_p_img1_1.jpg','image4_p_img2_1.jpg','image4_p_img3_1.jpg','image4_p_img4_1.jpg',
#             'image4_p_img5_1.jpg','image4_p_img6_1.jpg','image4_p_img7_1.jpg','image4_p_img8_1.jpg',]]

# x_indexes = np.arange(len(pic3['Picture']))
# width = 0.1
# plt.bar(x_indexes-(width*3),pic3['image4_p_img1_1.jpg'],width=width)
# plt.bar(x_indexes-(width*2),pic3['image4_p_img2_1.jpg'],width=width)
# plt.bar(x_indexes-width,pic3['image4_p_img3_1.jpg'],width=width)
# plt.bar(x_indexes,pic3['image4_p_img4_1.jpg'],width=width)
# plt.bar(x_indexes+width,pic3['image4_p_img5_1.jpg'],width=width)
# plt.bar(x_indexes+(width*2),pic3['image4_p_img6_1.jpg'],width=width)
# plt.bar(x_indexes+(width*3),pic3['image4_p_img7_1.jpg'],width=width)
# plt.bar(x_indexes+(width*4),pic3['image4_p_img8_1.jpg'],width=width)

# plt.xticks(ticks=x_indexes, labels= pic3['Picture'])
# plt.xlabel("Mbps (picture-3 'image4.jpg')")


# pic 4

# pic4 = data[['Picture','image5.jpg','image5_p_img1_1.jpg','image5_p_img2_1.jpg','image5_p_img3_1.jpg','image5_p_img4_1.jpg',
#             'image5_p_img5_1.jpg','image5_p_img6_1.jpg','image5_p_img7_1.jpg','image5_p_img8_1.jpg',]]

# x_indexes = np.arange(len(pic4['Picture']))
# width = 0.1
# plt.bar(x_indexes-(width*3),pic4['image5_p_img1_1.jpg'],width=width)
# plt.bar(x_indexes-(width*2),pic4['image5_p_img2_1.jpg'],width=width)
# plt.bar(x_indexes-width,pic4['image5_p_img3_1.jpg'],width=width)
# plt.bar(x_indexes,pic4['image5_p_img4_1.jpg'],width=width)
# plt.bar(x_indexes+width,pic4['image5_p_img5_1.jpg'],width=width)
# plt.bar(x_indexes+(width*2),pic4['image5_p_img6_1.jpg'],width=width)
# plt.bar(x_indexes+(width*3),pic4['image5_p_img7_1.jpg'],width=width)
# plt.bar(x_indexes+(width*4),pic4['image5_p_img8_1.jpg'],width=width)

# plt.xticks(ticks=x_indexes, labels= pic4['Picture'])
# plt.xlabel("Mbps (picture-4 'image5.jpg')")


# pic 5


pic5 = data[['Picture','map_p_img1_1.jpg','map_p_img2_1.jpg','map_p_img3_1.jpg','map_p_img4_1.jpg',
            'map_p_img5_1.jpg','map_p_img6_1.jpg','map_p_img7_1.jpg','map_p_img8_1.jpg',]]

x_indexes = np.arange(len(pic5['Picture']))
width = 0.1
plt.bar(x_indexes-(width*3),pic5['map_p_img1_1.jpg'],width=width)
plt.bar(x_indexes-(width*2),pic5['map_p_img2_1.jpg'],width=width)
plt.bar(x_indexes-width,pic5['map_p_img3_1.jpg'],width=width)
plt.bar(x_indexes,pic5['map_p_img4_1.jpg'],width=width)
plt.bar(x_indexes+width,pic5['map_p_img5_1.jpg'],width=width)
plt.bar(x_indexes+(width*2),pic5['map_p_img6_1.jpg'],width=width)
plt.bar(x_indexes+(width*3),pic5['map_p_img7_1.jpg'],width=width)
plt.bar(x_indexes+(width*4),pic5['map_p_img8_1.jpg'],width=width)

plt.xticks(ticks=x_indexes, labels= pic5['Picture'])
plt.xlabel("Mbps (picture-5 'map.jpg')")



#plt.title("Scan Script Comparison")


#plt.xlabel("Mbps (picture-1 'color.jpg')")
#plt.xlabel("Mbps (picture-2 'image3.jpg')")






plt.ylabel("Seconds")
#plt.legend(["For scan 1", "For scan 2", "For scan 3", "For scan 4", "For scan 5", "For scan 6", "For scan 7", "For scan 8",])
plt.rcParams.update({'font.size': 13})
plt.legend(["Ss1 Sc1", "Ss2 Sc1", "Ss3 Sc1","Ss4 Sc1", "Ss5 Sc1", "Ss6 Sc1","Ss7 Sc1", "Ss8 Sc1"])

plt.subplots_adjust(left=0.147, right=0.955, top=0.947, bottom=0.154, hspace=0.2, wspace=0.2)



plt.show()