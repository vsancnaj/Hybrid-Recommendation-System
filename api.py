from flask import Flask, request, jsonify
import pandas as pd
import pickle

"""
1️⃣ User sends a request with a product_id.
2️⃣ Hybrid Similarity Matrix finds the most similar products based on content similarity (ingredients, features) and collaborative filtering (ratings, user interactions).
3️⃣ Retrieves similar products sorted by similarity.
4️⃣ Returns product recommendations in JSON format.
"""

# Load pre-trained recommendation model
with open("hybrid_similarity.pkl", "rb") as file:
    hybrid_sim = pickle.load(file)

# Load product metadata
products_df = pd.read_csv("metadata/products.csv")

# Initialize Flask app
app = Flask(__name__)

def recommend_products(product_id, num_recommendations=5):
    product_id = str(product_id)  # Ensure product ID is a string

    # Check if product exists in the similarity matrix
    if product_id not in hybrid_sim.index:
        return []

    # Get similarity scores
    scores = hybrid_sim.loc[product_id].sort_values(ascending=False)

    # Exclude the input product itself
    recommended_products = scores.iloc[1:num_recommendations+1].index.astype(str)  # Convert index to string

    # Retrieve product details
    return products_df[products_df["product_id"].isin(recommended_products)][["product_name", "brand_name", "price_usd"]].to_dict(orient="records")

# API endpoint
@app.route("/recommend", methods=["GET"])
def recommend():
    product_id = request.args.get("product_id")
    num_recommendations = request.args.get("num_recommendations", default=5, type=int)
    
    if product_id is None:
        return jsonify({"error": "Please provide a valid product_id"}), 400

    print(f"Received request for product_id: {product_id}") 

    recommendations = recommend_products(product_id, num_recommendations)

    if not recommendations:
        return jsonify({"error": "No recommendations found, check product ID and similarity matrix"}), 404

    return jsonify({"recommendations": recommendations})


if __name__ == "__main__":

    app.run(debug=True)
