# LIDAR-DATA-SEGMENTATION-USING-IMPROVED-EUCLIDEAN-CLUSTERING-ALGORITHM

Segmentation of Lidar Data is an essential part of automatic tasks, such as object detection.
The segmentation results pose a direct impact on the further processing.
This project focuses on enhancing object detection capabilities in autonomous systems
through improved Euclidean clustering. The methodology involves VoxelGrid filtering of
point cloud data to remove noise and unwanted points followed by the application of a
RANSAC ground segmentation algorithm to remove ground points and isolate non-ground
points. Subsequently, Euclidean clustering is employed to segment the point cloud data
into distinct object clusters. Through extensive experimentation and evaluation, our project
demonstrates the effectiveness of the proposed approach in improving the accuracy of point
cloud segmentation and detecting objects. The results exhibit promising performance metrics,
highlighting the potential of our methodology for real-world applications such as autonomous
driving, surveillance, and urban planning.
This work also highlights the implementation using PYNQ-Z2
FPGA.
#LIDAR INPUT FILE

LiDAR point cloud data was obtained from kITTI dataset.The KITTI dataset, named after the
Karlsruhe Institute of Technology and the Toyota Technological Institute at Chicago, is a widely
used benchmark dataset for research in autonomous driving and computer vision. It comprises
high-resolution sensor data collected from a moving vehicle equipped with cameras, LiDAR,
and other sensors. The dataset includes various sequences recorded in urban environments,
covering diverse scenarios such as street scenes, highways, and intersections.Dataset Obtained
from KITTI dataset, which includes synchronized LiDAR point cloud data and camera images
captured in real-world urban scenarios.LiDAR point cloud data was obtained from kITTI dataset.The KITTI dataset, named after the
Karlsruhe Institute of Technology and the Toyota Technological Institute at Chicago, is a widely
used benchmark dataset for research in autonomous driving and computer vision. It comprises
high-resolution sensor data collected from a moving vehicle equipped with cameras, LiDAR,
and other sensors. The dataset includes various sequences recorded in urban environments,
covering diverse scenarios such as street scenes, highways, and intersections.Dataset Obtained
from KITTI dataset, which includes synchronized LiDAR point cloud data and camera images
captured in real-world urban scenarios.
The input LiDar data is plotted using python code. LiDAR data is plotted in open3d library.
This Python implementation allows us to load point cloud data from a .txt file and visualize it
using Open3D, a powerful library for 3D data processing and visualization. By following these
steps, we can quickly and easily explore and analyze point cloud data, which is often used in
various applications such as 3D reconstruction, object detection, and robotics.
This implementation is flexible and can be easily integrated into larger projects for further analysis or processing of point cloud data. Additionally, Open3D provides extensive documentation
and a rich set of functionalities for advanced 3D data manipulation, making it a valuable tool
for researchers and developers working with point cloud data

![Screenshot 2024-05-16 101144](https://github.com/abutha/LIDAR-DATA-SEGMENTATION-USING-IMPROVED-EUCLIDEAN-CLUSTERING-ALGORITHM/assets/75900173/f57a78eb-e20a-44be-b7e1-eb0b4cf140d9)


#OUTPUT

In this section, we delve into the implementation of our object tracking algorithms on
the PYNQ-Z2 FPGA board.Utilizing the capabilities of this board, which integrates ARM
Cortex-A9 processors with programmable logic, we explore how Python-based algorithms are
accelerated on the FPGA. Through the use of Jupyter Notebook, we demonstrate the seamless
integration of software and hardware for real-time object tracking applications.
1. Setup PYNQ-Z2 Board: The PYNQ-Z2 board was properly connected to the development
environment, including power, Ethernet, and required peripherals.
2. Accessed Jupyter Notebook: Jupyter Notebook was opened on the laptop, and the PYNQ-Z2
board was connected using its IP address, allowing access to the Python environment on the
board.
3. Imported Required Libraries: Necessary Python libraries for implementing VoxelGrid
filtering, including NumPy, Matplotlib, and any custom libraries, were imported.
4. Loaded FPGA Bitstream: The FPGA bitstream was loaded onto the PYNQ-Z2 board using
the appropriate commands in Jupyter Notebook, configuring the programmable logic part of
the FPGA with the required hardware design.
6. Uploaded Sensor Data: LiDAR pointcloud data in .txt format was uploaded into jupyter
notebook by clicking on Upload button on top of the window.
7. Applied Algorithms: The codes in python was developed and
were applied to the LiDAR point cloud data performing necessary computations accelerated on
the FPGA.
8. Visualized Results: Results of the algorithms were visualized using
Matplotlib library for the voxel grid value 0.5.
9. Execution time calculation : Execution time of code were performed on the
processor of PYNQ Z2 and was obtained to compare with previous implementations.


From the result it was observed that as Distance Threshold value increases the number
of clustered object decreases and number of points corresponding to a cluster increases. The
optimal value of Distance Threshold value was 0.5 for the dataset we used. The output obtained
for this optimal value is given
![0 5](https://github.com/abutha/LIDAR-DATA-SEGMENTATION-USING-IMPROVED-EUCLIDEAN-CLUSTERING-ALGORITHM/assets/75900173/cc7c6769-1abf-4628-8e24-e2bb9fe47d98)



