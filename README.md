# 🪙 BTCNextDay - Predict Tomorrow's Bitcoin Price

---

## 🚀 Project Goal  
BTCNextDay is a machine learning-based application that predicts the **next day's closing price of Bitcoin** using current market data.  
This helps investors, traders, and enthusiasts to gain insights into Bitcoin trends with a simple, interactive, and explainable tool.

---

## 📄 Project Overview  
Due to the highly volatile nature of Bitcoin, predicting its price is a challenging task.  
This project uses historical closing price data to train multiple machine learning models and selects the best-performing one (CatBoost Regressor) for deployment.  
It features a **Streamlit-powered web app** for real-time price prediction.

---

## ⚙️ Project Workflow  

### 🔹 1. Data Preprocessing
- Loaded historical Bitcoin price data from CSV
- Selected `Close` price column as the main feature
- Created shifted target column (`Next Day Price`)
- Removed NaN rows due to shifting
- Split data into training and testing sets (80-20 split)

### 🔹 2. Model Building
Tested multiple regression models:
- **Linear Regression**
- **Support Vector Regression (SVR)**
- **Random Forest Regressor**
- **XGBoost Regressor**
- **LightGBM Regressor**
- **CatBoost Regressor** ✅ *(Best performer)*

Final Model:
- **Model Used**: `CatBoostRegressor(iterations=1000, learning_rate=0.1, depth=6)`
- **Test Set R² Score**: ~0.97.99  
- Saved using `joblib` for future inference

### 🔹 3. Evaluation Metrics
- **Mean Absolute Error (MAE)**: 79.81  
- **Mean Squared Error (MSE)**: 15351.32  
- **R² Score**: 0.9856 *(on test data)*

### 🔹 4. Deployment
- Developed frontend with **Streamlit**
- User inputs current closing price
- Model returns predicted next-day closing price
- Basic error handling for missing model file
- Fast, lightweight deployment — can be hosted on:
  - Streamlit Cloud
  - Hugging Face Spaces
  - Render / Heroku *(with minor adjustments)*

---



## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀 
