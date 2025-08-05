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

## 🧰 Tech Stack  

- **Frontend/UI**: Streamlit  
- **Backend & Logic**: Python  

### 🧪 Libraries Used:
- `pandas`, `numpy` – Data processing  
- `scikit-learn` – ML models and preprocessing utilities  
- `catboost` – Gradient boosting model used for final prediction  
- `joblib` – Model saving and loading  
- `matplotlib` – Data visualization during EDA  
- `streamlit` – Web interface for deployment  

---
## 🗂️ Project Structure  

```bash
BTCNextDay/
│
├── app.py                           # Streamlit interface
├── model.pkl                        # Trained CatBoost model
├── Bitcoin_Price_Prediction.ipynb  # Jupyter notebook for preprocessing + model training
├── requirements.txt                 # Dependencies
└── README.md                        # Project documentation
```


---

## ✨ Features  

- 🔮 **Next-Day Bitcoin Price Prediction**  
- 🧠 **Tested Multiple ML Models (Linear, RF, CatBoost)**  
- 📊 **Evaluation Metrics with High Accuracy**  
- 💡 **Single Input – Clean UI**  
- 💾 **Trained Model Saved and Loaded with Joblib**  
- 🛑 **Error Handling for Missing Files**  
- 🌐 **Ready for Web Deployment via Streamlit**

---

## 🔮 Future Enhancements

- Add more features: open, high, low, volume, technical indicators  
- Fetch real-time Bitcoin data via APIs  
- Add visualizations and price trend charts  
- Store user inputs and predictions for logging  
- Deploy full-stack with user authentication  
- Add daily alerts or notifications with predicted price

---


## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀 
