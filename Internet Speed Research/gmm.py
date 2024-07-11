# from sklearn.mixture import GaussianMixture
import pandas as pd

Internet = pd.read_csv("Internet Speed Interpretation.csv")

print(Internet["Upload"].describe())

# gmm = GaussianMixture(n_components=3)
# gmm.fit(multimodal_dist.reshape(-1, 1))

# means = Upload.mean

# # Conver covariance into Standard Deviation
# standard_deviations = gmm.covariances_**0.5  

# # Useful when plotting the distributions later
# weights = gmm.weights_  


# print(f"Means: {means}, Standard Deviations: {standard_deviations}")