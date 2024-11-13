import pandas as pd
import yaml
import pickle
import json
from sklearn.metrics import mean_absolute_percentage_error, r2_score

with open("params.yaml") as f:
    params = yaml.safe_load(f)

data = pd.read_csv(params["processed_data_path"])
X = data.drop("price", axis=1)
y = data["price"]

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

predictions = model.predict(X)
mape = mean_absolute_percentage_error(y, predictions)
r2 = r2_score(y, predictions)

metrics = {
    "mape": mape,
    "r2_score": r2
}

with open("scores.json", "w") as f:
    json.dump(metrics, f)
