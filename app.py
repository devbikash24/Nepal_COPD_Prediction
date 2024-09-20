import pandas as pd
import pickle
import streamlit as st
import os

# Define the base path to locate model files
base_path = os.path.dirname(os.path.abspath(__file__))

# Load models
pipe_path = os.path.join(base_path, 'models', 'pipeline2.pkl')
model_path = os.path.join(base_path, 'models', 'random_forest_model2.pkl')

try:
    with open(pipe_path, 'rb') as f:
        pipe = pickle.load(f)

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

except FileNotFoundError as e:
    st.error(f"Error: {e}")

# Set custom page configuration
st.set_page_config(page_title="COPD Prediction Dashboard", page_icon="🫁", layout="wide")

# Custom CSS to enhance the appearance
st.markdown(
    """
    <style>
        .stButton button {
            border-radius: 10px;
            background-color: #212121;
            color: white;
            font-weight: bold;
        }
        .css-18e3th9 {
            padding: 20px;
        }
        .css-1q8dd3e {
            padding-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Title and description
    st.title("🫁 COPD Prediction Dashboard")
    st.write("""
    Welcome to the COPD Prediction Dashboard. This tool predicts the likelihood of Chronic Obstructive Pulmonary Disease (COPD) based on various risk factors.
    """)

    # Main content layout
    with st.container():
        st.markdown("<div class='main-content'>", unsafe_allow_html=True)

        # Sidebar for user input with new layout and design
        st.sidebar.header("Customize Your Input")

        # Replacing some selectbox inputs with other widgets
        Respiratory_Infections_Childhood = st.sidebar.checkbox("🤧 Childhood Respiratory Infections", value=False)
        Occupational_Exposure = st.sidebar.checkbox("🏭 Occupational Exposure", value=False)
        Family_History_COPD = st.sidebar.checkbox("👪 Family History of COPD", value=False)
        BMI_category = st.sidebar.radio("⚖️ BMI Category", ['underweight', 'normal', 'overweight', 'obese', 'too_obese'])
        Air_Pollution_Level_category = st.sidebar.radio("🌫️ Air Pollution Level", ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe'])
        Gender_encoded = st.sidebar.radio("🚻 Gender", ['Male', 'Female'])

        Smoking_Status = st.sidebar.radio("🚬 Smoking Status", ["Current", "Former", "Never"])
        Location = st.sidebar.selectbox(
            "📍 Location", 
            ["Biratnagar", "Lalitpur", "Birgunj", "Chitwan", "Hetauda", "Dharan", "Butwal","Kathmandu", "Pokhara"]
        )
        Age_Category = st.sidebar.selectbox("📅 Age Category", ['young', 'adult', 'middle_aged', 'old', 'too_old'])
        # Age_Category = st.sidebar.slider("📅 Age Category", min_value=1, max_value=5, value=3, format="%d",
        #                                  help="1: young, 2: adult, 3: middle_aged, 4: old, 5: too_old")
        Biomass_Fuel_Exposure = st.sidebar.checkbox("🔥 Biomass Fuel Exposure", value=False)

        # Process the input data
        input_data = {
            'Smoking_Status': Smoking_Status,
            'Biomass_Fuel_Exposure': 1 if Biomass_Fuel_Exposure else 0,
            'Occupational_Exposure': 1 if Occupational_Exposure else 0,
            'Family_History_COPD': 1 if Family_History_COPD else 0,
            'Location': Location,
            'Respiratory_Infections_Childhood': 1 if Respiratory_Infections_Childhood else 0,
            # 'Age_Category': ['young', 'adult', 'middle_aged', 'old', 'too_old'][Age_Category - 1],
            'Age_Category': Age_Category,
            'BMI_category': BMI_category,
            'Air_Pollution_Level_category': Air_Pollution_Level_category,
            'Gender_encoded': 1 if Gender_encoded == 'Male' else 0
        }

        # Calculate interaction feature
        input_data['Occupation_Family_History_Interaction'] = (
            input_data['Occupational_Exposure'] * input_data['Family_History_COPD']
        )

        # Convert the input data to a dataframe
        input_df = pd.DataFrame([input_data])

        # Display user input summary with a cleaner table look
        st.subheader("📝 Your Input Summary:")
        st.table(input_df)

        # Prediction logic with customized output styling
        if st.button("🧪 Predict COPD Risk"):
            try:
                # Transform input using the pre-processing pipeline
                transformed_ip = pipe.transform(input_df)
                prediction = model.predict(transformed_ip)
                result = "Positive" if prediction[0] == 1 else "Negative"

                # Custom styling for result display
                if result == "Positive":
                    # Red background for positive results
                    st.markdown(
                        f"""
                        <div style="background-color:#ff4d4d;border-radius:10px;">
                        <h3 style="color:white;text-align:center;">Prediction Result: {result}</h3>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                else:
                    # Light green background for negative results
                    st.markdown(
                        f"""
                        <div style="background-color:#90ee90;border-radius:10px;">
                        <h3 style="color:black;text-align:center;">Prediction Result: {result}</h3>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )

            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
