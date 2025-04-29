# pjpeg-research

This repository contains files related to the paper:

## Paper Name: Orchestrating Image Retrieval and Storage over A Cloud System
[Link](https://ieeexplore.ieee.org/abstract/document/9743811/)

### Group Members:
[Jannatun Noor](https://sites.google.com/site/jannatun0abigzero/)

[Md. Nazrul Huda Shanto](https://www.linkedin.com/in/nazrulhudashanto/)

[Joyanta Jyoti Mondal](https://lepotatoguy.github.io)

[Md. Golam Hossain](https://www.linkedin.com/in/mghossain)

[Sriram Chellappan](https://cse.usf.edu/~sriramc/)

[A. B. M. Alim Al Islam](https://sites.google.com/site/abmalimalislam/)

## Abstract:

Since massive numbers of images are now being communicated from, and stored in different cloud systems, faster retrieval has become extremely important. This is more relevant, especially after COVID-19 in bandwidth-constrained environments. However, to the best of our knowledge, a coherent solution to overcome this problem is yet to be investigated in the literature. In this paper, by customizing the Progressive JPEG method, we propose a new Scan Script to ensure Faster Image Retrieval. Furthermore, we also propose a new lossy PJPEG architecture to reduce the file size as a solution to overcome our Scan Script's drawback. In order to achieve an orchestration between them, we improve the scanning of Progressive JPEG's picture payloads to ensure Faster Image Retrieval using the change in bit pixels of distinct Luma and Chroma components (Y, Cb, and Cr). The orchestration improves user experience even in bandwidth-constrained cases. We evaluate our proposed orchestration in a real-world setting across two continents encompassing a private cloud. Compared to existing alternatives, our proposed orchestration can improve user waiting time by up to 54% and decrease image size by up to 27%. Our proposed work is tested in cutting-edge cloud apps, ensuring up to 69% quicker loading time.


## Abstract (For Beginners):

We all use Facebook to see people hanging out, celebrating their good times, asking for help, and so on. We also add images to some of the Facebook statuses. And when someone is trying to watch the image, it needs a bit of time to load up the image from the Facebook server if you notice (you will see this better when the internet speed is slower). So, we came up with a novel approach that will compress and save the image you uploaded to the server in such a way, when the image gets loaded up in front of you, it will be up to 69% faster than the current situation (even in slower internet).

Facebook also compresses images to show us images faster but those images get blurry while storing (you may know people saying "please send the picture on WhatsApp since it gets blurry on Facebook."). But our approach does not lose any quality of the images and on the other hand, gives a blazing fast loading time.

## Abstract in Bengali:

আমরা সবাই ই ফেসবুকে দেখি বিভিন্ন মানুষ বিভিন্ন জায়গায় যাচ্ছে, তাদের ভালো মূহুর্ত কাটাচ্ছে, খারাপ সময়ে সাহায্যের জন্য হাত বাড়াচ্ছ এবং এমন অনেক পোস্ট। তো আমরা অনেকসময় সেসব ফেসবুক স্ট্যাটাসে ছবি এড করে থাকি। এবং অন্যরা যখন সেই ছবিগুলো অন্য প্রান্ত থেকে দেখছে, তখন কিছুটা সময় লাগে ফেসবুক সার্ভার থেকে ডাউনলোড হয়ে ছবিটা লোড নেয়ার জন্য সেই ডিভাইসে (জিনিসটা আরও লক্ষণীয় যখন আমরা কম ইন্টারনেট স্পিড দেখতে পাই)। এজন্যে আমরা একটি সম্পূর্ণ নতুন ধরনের সমাধান নিয়ে এসেছি যা এমনভাবে ছবিটিকে কম্প্রেস করে সেইভ করবে সার্ভারে, পরবর্তীতে ছবিটি যখন লোড করা হবে, তখন স্বাভাবিকের তুলনায় সর্বোচ্চ ৬৯% দ্রুত ছবিটি লোড নিবে (এমনকি ধীরগতির ইন্টারনেটেও)। 

ফেসবুকও ইতোমধ্যে ছবি কম্প্রেস করে সেইভ করে আমাদের দেখানোর চেষ্টা করে থাকে কিন্তু তারা তাদের মত রাখতে গিয়ে ছবিগুলো তুলনামূলক ঘোলা করে ফেলে (এজন্য আমরা কমবেশি দেখি অনেককেই বলতে "ছবিগুলো প্লিজ হোয়াটসএপে পাঠান। ফেসবুকে ছবিগুলো ঘোলা হয়ে যায়।")। আমরা সেই সমস্যার ও সমাধান করে ছবিগুলো সেইভ করে রাখি যাতে ছবির কোয়ালিটি নষ্ট না হয় এবং একইসাথে দ্রুতগতিতে ছবিগুলো লোড নেয়। 

## Citation

If you use this work, please cite the following paper:

[1] J. Noor, M. N. H. Shanto, J. J. Mondal, M. G. Hossain, S. Chellappan and A. B. M. A. Al Islam, "Orchestrating Image Retrieval and Storage Over a Cloud System," in IEEE Transactions on Cloud Computing, vol. 11, no. 2, pp. 1794-1806, 1 April-June 2023, doi: 10.1109/TCC.2022.3162790. 

```bibtex
@ARTICLE{9743811,
  author={Noor, Jannatun and Shanto, Md. Nazrul Huda and Mondal, Joyanta Jyoti and Hossain, Md. Golam and Chellappan, Sriram and Al Islam, A. B. M. Alim},
  journal={IEEE Transactions on Cloud Computing}, 
  title={Orchestrating Image Retrieval and Storage Over a Cloud System}, 
  year={2023},
  volume={11},
  number={2},
  pages={1794-1806},
  doi={10.1109/TCC.2022.3162790}}

```
