import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Load the real-world Singapore HDB Resale dataset (2017-Onwards)
url = "https://raw.githubusercontent.com/kohjiaxuan/Predicting-HDB-Price-with-Machine-Learning/master/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv"
data = pd.read_csv(url)

# 2. Extract numeric feature vectors to prevent complex category encoding
# Clean 'storey_range' into a clean numeric floor column (takes the lower bound)
data["floor_level"] = data["storey_range"].str.split(" ").str[0].astype(float)

# Select our 3 core logical parameters
features = ["floor_area_sqm", "lease_commence_date", "floor_level"]
X = data[features]
y = data["resale_price"]

# 3. Partition data (80% training / 20% validation testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train the Linear Regression fitting line
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Serialize and freeze the model output
with open("house_model.pkl", "wb") as f:
    pickle.dump(model, f)

print(" HDB Resale Model trained successfully and saved as 'house_model.pkl'!")