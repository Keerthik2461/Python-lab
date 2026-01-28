
import numpy as np 
import pandas as pd 
 
#Step 2: Create the Dataset 
data = { 
    "Attendance": [85, 90, 88, 92, 80], 
    "Internal": [78, 82, 79, 85, 75], 
    "Assignment": [80, 85, 78, 88, 72], 
    "EndSem": [75, 80, 77, 82, 70] 
} 
 
df = pd.DataFrame(data, index=["S1", "S2", "S3", "S4", "S5"]) 
print(df) 
 
#Step 3: Mean Centering the Data 
X = df.values 
mean = np.mean(X, axis=0) 
X_centered = X - mean 
 
print("Mean values:\n", mean) 
print("Mean-centered data:\n", X_centered) 
 
#Step 4: Compute Covariance Matrix using ( X^T X ) 
n = X_centered.shape[0] 
cov_matrix = (X_centered.T @ X_centered) / (n - 1) 
 
print("Covariance Matrix:\n", cov_matrix) 
 
#Step 5: Compute Eigenvalues and Eigenvectors 
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix) 
 
print("Eigenvalues:\n", eigenvalues) 
print("Eigenvectors:\n", eigenvectors) 
 
#Step 6: Select the First Principal Component (PC1) 
idx = np.argmax(eigenvalues) 
pc1 = eigenvectors[:, idx] 
 
# Normalize 
pc1 = pc1 / np.linalg.norm(pc1) 
print("Principal Component 1 (Eigenvector):\n", pc1) 
 
#Step 7: Compute PC1 Scores (Projection) 
pc1_scores = X_centered @ pc1 
 
df["PC1_Score"] = pc1_scores 
print(df) 
 
#Step 8: Variance Explained 
explained_variance = eigenvalues / np.sum(eigenvalues) 
print("Variance explained by PC1:", explained_variance[idx]) 
 
#Step 9: Scree Plot 
import matplotlib.pyplot as plt 
import numpy as np 
# Sort eigenvalues in descending order 
eigenvalues_sorted = np.sort(eigenvalues)[::-1] 
# Compute variance ratio 
variance_ratio = eigenvalues_sorted / np.sum(eigenvalues_sorted) 
# Scree plot 
plt.figure() 
plt.plot(range(1, len(variance_ratio) + 1), variance_ratio, marker='o') 
plt.xlabel("Principal Component") 
plt.ylabel("Variance Explained") 
plt.title("Scree Plot for PCA") 
plt.grid(True) 
plt.show()