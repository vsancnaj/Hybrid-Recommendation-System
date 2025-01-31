# 🧴 Sephora Skincare Recommender

## 📌 Overview
A **Hybrid Recommendation System** for **Sephora skincare products**, combining:

1️⃣ **Item-Based Collaborative Filtering** – Recommends products based on user ratings.  
2️⃣ **Content-Based Filtering** – Recommends products based on ingredients, categories, and highlights.  

## 🎯 Purpose
- Help users find skincare products tailored to their **preferences, skin type, and concerns**.
- Provide **personalized recommendations** using **machine learning & NLP**.

## 🚀 Features
✅ **Hybrid Recommendation Model** (Item-Based CF + Content-Based Filtering)  
✅ **Flask API** – Serves recommendations dynamically  
✅ **Streamlit Web App** – User-friendly interface to explore recommendations  

## 📦 Structure
```
├── 📂 data/                     # Contains raw dataset files (ignored in Git)
│   ├── product_info.csv         # Product metadata (ID, name, brand, ingredients, categories, price, etc.)
│   ├── reviews_0-250.csv        # User reviews (ratings, skin type, feedback, etc.)
│   ├── ...                      # Other review datasets (split for large-scale handling)
│
├── 📂 metadata/                  # Stores processed data files
│   ├── products.csv              # Cleaned & processed product metadata
│   ├── hybrid_similarity.pkl     # Precomputed similarity matrix for recommendations
│
├── 📂 skincare/                  # Virtual environment (ignored in Git)
│
├── api.py                        # Flask API for serving recommendations
├── app.py                        # Streamlit Web App interface
├── model.ipynb                   # Jupyter Notebook for training & evaluating models
├── requirements.txt               # Dependencies for installing the project
├── .gitignore                     # Excludes unnecessary files (datasets, env, cache)
├── README.md                      # Project documentation (this file)
```

## 📂 Dataset
- **Product Data:** Contains product ID, brand, ingredients, categories, price, and highlights.  
- **Reviews Data:** User ratings, reviews, and skincare attributes (skin type, concerns).
### **1️⃣ Download the Dataset**
1.	Go to the [Sephora Skincare Reviews Dataset on Kaggle](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data)
2.	Click Download and extract the ZIP file.

### **2️⃣ Move Files to data/ Directory**
- After extraction, place the dataset files inside the data/ folder:
```
├── data/
│   ├── product_info.csv
│   ├── reviews_0-250.csv
│   ├── reviews_250-500.csv
│   ├── reviews_500-750.csv
│   ├── reviews_750-1250.csv
│   ├── reviews_1250-end.csv
```

## 🛠️ Installation & Setup
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the Flask API**
```bash
python api.py
```
- API will be available at: http://127.0.0.1:5000/recommend?product_id=P12345&num_recommendations=5

 ### **3️⃣ Run the Streamlit Web App** 
```bash
streamlit run app.py
```
- Open in browser: http://localhost:8501
  
## **📌 How It Works** 
1.	Users select a Sephora skincare product from the web app.
2.	The model generates recommendations using a combination of product similarity (content-based) and user ratings (collaborative filtering).
3.	Users receive recommendations with product details (brand, price, and rating).

## **🛠️ Future Improvements** 
- Improve recommendations using sentiment analysis on user reviews.
- Personalize results further based on skin type & concerns.
- Deploy API & Web App on AWS/Heroku for public access.










 








