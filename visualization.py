from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix


def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()

# Visualization:
# 1.Display DataFrame Head
'''
print(housing.head())
'''

# 2. Visualizing All Numerical Columns with Histograms
'''
housing.hist(bins=50, figsize=(20, 15))
plt.tight_layout()
plt.show()
'''

# 3. Scatter Matrix (Pair Plot) for Relationships Between Features
'''
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))
plt.show()
'''

# 4. Correlation Heatmap
'''
# Select only the numeric columns
numeric_housing = housing.select_dtypes(include=['float64', 'int64'])

# Plot a correlation matrix heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_housing.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title('Correlation Matrix of Housing Data')
plt.show()
'''
# 5. Box Plots for Outlier Detection
'''
housing.plot(kind="box", subplots=True, layout=(4,4), figsize=(20, 15), sharex=False, sharey=False)
plt.tight_layout()
plt.show()
'''
# 6. Scatter Plot of the Entire Dataset
'''
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
             s=housing["population"]/100, label="population", figsize=(10, 7),
             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)
plt.legend()
plt.show()
'''