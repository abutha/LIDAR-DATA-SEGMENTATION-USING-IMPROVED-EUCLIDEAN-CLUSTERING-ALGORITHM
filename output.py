#The provided code includes point cloud data processing, voxelization, RANSAC-based ground segmentation,
#and custom Euclidean clustering. The data is loaded from a .txt file, which you want to adjust to load from a .bin file instead.



import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import RANSACRegressor

# Load point cloud data from .bin file
def load_point_cloud(filename):
    # Assuming the data consists of float32 (4 bytes per value) XYZ coordinates
    data = np.fromfile(filename, dtype=np.float32)
    # Reshape the data to a 2D array with columns (XYZ)
    data = data.reshape(-1, 3)
    return data

# Voxelization
def voxel_grid_downsample(points, voxel_size=0.1):
    # Calculate grid indices for each point
    grid_indices = np.floor(points / voxel_size).astype(int)
    
    # Map grid indices to unique voxel IDs
    voxel_ids = grid_indices[:, 0] + grid_indices[:, 1] * 10000 + grid_indices[:, 2] * 1000000
    
    # Find unique voxel IDs (representing occupied voxels)
    unique_voxel_ids, unique_indices = np.unique(voxel_ids, return_index=True)
    
    # Extract occupied voxel centers
    voxel_centers = points[unique_indices]
    
    return voxel_centers

# RANSAC ground segmentation
def ransac_ground_segmentation(points, max_distance=0.5, min_samples=3, max_trials=100):
    ransac = RANSACRegressor(min_samples=min_samples, max_trials=max_trials, residual_threshold=max_distance)
    X = points[:, :2]  # Considering only x and y coordinates for segmentation
    y = points[:, 2]   # Z coordinates as labels
    ransac.fit(X, y)

    # Inliers mask
    inlier_mask = ransac.inlier_mask_
    outliers_mask = np.logical_not(inlier_mask)

    # Ground points and outliers
    ground_points = points[inlier_mask]
    non_ground_points = points[outliers_mask]

    return ground_points, non_ground_points

# Custom Euclidean clustering
def custom_euclidean_clustering(points, distance_threshold=0.5):
    clusters = []
    cluster_labels = np.zeros(len(points), dtype=int)
    current_label = 1

    while len(points) > 0:
        seed_point = points[0]
        cluster = [seed_point]
        points = np.delete(points, 0, axis=0)

        i = 0
        while i < len(cluster):
            point = cluster[i]
            distances = np.linalg.norm(points - point, axis=1)
            neighbors = points[distances < distance_threshold]
            cluster.extend(neighbors)
            indices = np.where((points == neighbors[:, None]).all(-1))[1]
            cluster_labels[indices] = current_label
            points = np.delete(points, np.where(distances < distance_threshold), axis=0)
            i += 1

        clusters.append(cluster)
        current_label += 1

    return clusters, cluster_labels

# Example usage
if __name__ == "__main__":
    # Load point cloud data
    filename = "Raw_PointCloud_Totaltxt.bin"  # Change the file path as needed
    point_cloud_data = load_point_cloud(filename)

    # Voxelization
    voxel_size = 0.2
    voxel_centers = voxel_grid_downsample(point_cloud_data, voxel_size=voxel_size)

    # RANSAC ground segmentation using voxelized points
    _, non_ground_points = ransac_ground_segmentation(voxel_centers)

    # Perform custom Euclidean clustering on non-ground points
    clusters, _ = custom_euclidean_clustering(non_ground_points[:, :2], distance_threshold=2)  # Assuming only X, Y coordinates are used

    # Plotting clusters in 2D
    plt.figure(figsize=(8, 6))
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 1], cluster[:, 0], s=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Custom Euclidean Clustering of Non-Ground Point Cloud Data (2D)')
    plt.gca().invert_xaxis()  # Flip the x-axis
    plt.show()
