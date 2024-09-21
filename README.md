# 🫁 COPD Prediction Dashboard

Welcome to the **COPD Prediction Dashboard**! This interactive tool predicts the likelihood of Chronic Obstructive Pulmonary Disease (COPD) based on various risk factors. The application uses a trained Random Forest model with a user-friendly interface built using Streamlit.

Live Demo: https://nepalcopd.streamlit.app/
## 🌟 Features

- **Interactive Inputs**: Customize your inputs using checkboxes, radio buttons, sliders, and text fields to personalize your predictions.
- **Real-time Predictions**: Get instant predictions based on your input values using a pre-trained Random Forest model.
- **Visual Input Summary**: View a table summary of your input data for verification before making a prediction.
- **Stylish Results**: The app displays results with customized styling, clearly indicating whether the prediction is positive or negative for COPD.

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

### Installation

Follow these steps to set up and run the application on your local machine:

1. **Clone the Repository**

   Clone the repository using the following command:

   ```bash
   git clone https://github.com/devbikash24/Nepal_COPD_Prediction.git
   cd copd-prediction-dashboard
   
2. **Create a Virtual Environment (Optional but Recommended)**

   Clone the repository using the following command:

   ```bash
    python -m venv venv
    # Activate the virtual environment
    source venv/bin/activate    # On Windows, use: venv\Scripts\activate
   
   
3. **Install Required Dependencies**

   pip install -r requirements.txt
   
   
### Installation

Follow these steps to set up and run the application on your local machine:

Model and Pipeline Setup

Ensure that the trained model (random_forest_model2.pkl) and preprocessing pipeline (pipeline2.pkl) are located in the models directory within the project folder. If not, place them in the appropriate folder.


### Running the App
Start the Streamlit app using the following command:

   ```bash
    streamlit run app.py


After running this command, the app will start, and you can access it in your browser     at http://localhost:8501.



 
