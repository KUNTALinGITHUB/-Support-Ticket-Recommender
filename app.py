from flask import Flask, request, jsonify
import pickle
from flask import Flask, request, jsonify, send_from_directory



# Load saved model
from ticket_recommender import TicketRecommender

# Load pickled model
with open("recommender.pkl", "rb") as f:
    recommender = pickle.load(f)

# Create Flask app
app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()

    # Get query string and parameters
    query = data.get('customer_remark', '')
    top_n = data.get('top_n', 5)

    # Optional context data for enriched matching
    context_data = {
        'Product_category': data.get('Product_category', '')
    }

    # Run recommendation
    results = recommender.recommend(query, context_data=context_data, top_n=top_n)

    # Send JSON response
    return jsonify(results.to_dict(orient='records'))

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
    query = data.get('query', '')
    suggestions_df = recommender.recommend(query, top_n=5)
    hints = suggestions_df['Customer Remarks'].tolist()
    return jsonify(hints)


if __name__ == '__main__':
    app.run(debug=True)
