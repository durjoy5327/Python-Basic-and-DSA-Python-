<<<<<<< HEAD
import numpy as np

def modified_z_score_condition(data, threshold=3.5):
    # Calculate the median of the data
    median = np.median(data)
    
    # Calculate the Median Absolute Deviation (MAD)
    mad = np.median(np.abs(data - median))
    
    # Constant to scale the MAD to be comparable to standard deviation
    constant = 0.6745
    
    # Calculate the Modified Z-scores
    modified_z_scores = constant * (data - median) / mad
    
    # Return True for values where Modified Z-score is greater than the threshold
    return modified_z_scores > threshold

# Example usage
data = np.array([10, 12, 12, 13, 12, 14, 15, 12, 10, 10, 100])  # 100 is an outlier
outliers_mask = modified_z_score_condition(data)

print("Outliers mask:", outliers_mask)
=======
import numpy as np

def modified_z_score_condition(data, threshold=3.5):
    # Calculate the median of the data
    median = np.median(data)
    
    # Calculate the Median Absolute Deviation (MAD)
    mad = np.median(np.abs(data - median))
    
    # Constant to scale the MAD to be comparable to standard deviation
    constant = 0.6745
    
    # Calculate the Modified Z-scores
    modified_z_scores = constant * (data - median) / mad
    
    # Return True for values where Modified Z-score is greater than the threshold
    return modified_z_scores > threshold

# Example usage
data = np.array([10, 12, 12, 13, 12, 14, 15, 12, 10, 10, 100])  # 100 is an outlier
outliers_mask = modified_z_score_condition(data)

print("Outliers mask:", outliers_mask)
>>>>>>> 6e7d3dbbe24263c3b15965585e6b69f34f465a2b
