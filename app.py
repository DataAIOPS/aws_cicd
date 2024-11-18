from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    try:
        bedrooms = data['bedrooms']
        bathrooms = data['bathrooms']
        sqft_living = data['sqft_living']
        floors = data['floors']
        yr_built = data['yr_built']
        
        features = np.array([[bedrooms, bathrooms, sqft_living, floors, yr_built]])
        prediction = np.round(model.predict(features))
        
        return jsonify({'predicted_price': prediction[0]})
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {e.args[0]}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
