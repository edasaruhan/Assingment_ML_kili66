import joblib
import streamlit as st 
import streamlit_option_menu
from streamlit_option_menu import option_menu 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Log an info message
logging.info('User accessed the app.')

# Log an error message
try:

    #load the models

    #diabetes_model= pickle.load(open('diabetes_model.sav','rb'))
    # heart_model= pickle.load(open('mymodels/heart_model.sav','rb'))
    # parkinson_model= pickle.load(open('mymodels/parkinson_model.sav','rb'))
    diabetes_model= joblib.load(open('diabetes_model.joblib','rb'))
    heart_model= joblib.load(open('heart_model.joblib','rb'))
    parkinson_model= joblib.load(open('parkinson_model.joblib','rb'))
    with st.sidebar:
        selected= option_menu('Multiple Chronic Disease Prediction System',
                            ['Diabetes Disease Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Disease Prediction'
                            ], icons=['activity','heart-pulse','person'], default_index= 0)
    ### Diabetes Disease-----------------------------------------------
    if selected=='Diabetes Disease Prediction':
        st.title(':medical_symbol: Diabetes Disease Prediction') # page title
        st.subheader('Please Read the Medical describtion below before entering the values :exclamation:')
        # User inputs
        col1, col2, col3=st.columns(3)
        
        with col1:
            Pregnancies= st.text_input("Number of times pregnant")
        with col2:
            Glucose=  st.text_input(" glucose concentration")
        with col3:
            BloodPressure= st.text_input("blood pressure (mm Hg)")
        with col1:
            SkinThickness= st.text_input("Triceps skin fold thickness (mm)")
        with col2:
            Insulin=st.text_input(" insulin (mu U/ml)")
        with col3:
            BMI= st.text_input("Enter Body mass index of Patient")
        with col1:
            DiabetesPedigreeFunction= st.text_input("Diabetes pedigree function value")
        with col2:
            Age= st.text_input("Enter the age of the patient")
        #Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
        # Prediction for diabets disease
        diab_diagnosis=''

    #if st.button("Diabetes Test result"):
        
    #     diabete_pred=diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    #     if (diabete_pred[0]==1):
    #         diab_diagnosis="The person is diabetic"
    #     else:
    #         diab_diagnosis="The person is not diabetic"
    # st.success(diab_diagnosis)
    # Prediction

        if st.button("Diabetes Test result"):
            try:
            # Convert input features to numeric values
                features = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
                features = [float(feature) for feature in features]

                # Predict using XGBoost model
                diabete_pred = diabetes_model.predict([features])

                # Update diagnosis based on prediction
                if diabete_pred == 1:
                    diab_diagnosis = "The person has a high probability to be Diabetic"
                else:
                    diab_diagnosis = "The person has less chance to be Diabetic"

            except Exception as e:
                st.error(f"Error predicting diabetes: {e}")
                diab_diagnosis = "Prediction error"

        st.success(diab_diagnosis)
        #st.plotly_chart(features)
        st.header('Attention! Please follow the values given in the range') 
        st.markdown("""
            * **Pregnancies**: Number of times pregnant, range: [0-17]
            * **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test, range: [30.46-199]
            * **BloodPressure**: Diastolic blood pressure (mm Hg), range: [24-122]
            * **SkinThickness**: Triceps skin fold thickness (mm), range: [7-99]
            * **Insulin**: 2-Hour serum insulin (mu U/ml), range: [89.10-846]
            * **BMI**: Body mass index (weight in kg/(height in m)^2), range: [18, 67]
            * **DiabetesPedigreeFunction**: Diabetes pedigree function. The range value is [0-2.5]
            * **Age**: Age (years)
            
    """)
    ### Heart Disease-----------------------------------------
    if selected=='Heart Disease Prediction':
        st.title(":heartpulse: Heart Disease Prediction ") #page TiTLE
        st.subheader("Please read the Medical descriptions below before entering the values :exclamation:")
        #user inputs
        col1, col2, col3=st.columns(3)
        #age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
        with col1:
            age= st.text_input("Age of the person")
        with col2:
            sex=  st.text_input("sex: 0 or 1?")
        with col3:
            cp= st.text_input("cheast pain value")
        with col1:
            trestbps= st.text_input("resting blood pressure(trestbps)value")
        with col2:
            chol=st.text_input("serum cholestoral in mg/dl value")
        with col3:
            fbs= st.text_input("fasting blood sugar")
        with col1:
            restecg= st.text_input("resting electrocardiographic results (0,1,2)")
        with col2:
            thalach= st.text_input("Enter the maximum heart rate achieved")
        with col3:
            exang= st.text_input("exercise induced angina value")
        with col1:
            oldpeak= st.text_input("Enter the oldpeak ")
        with col2:
            slope= st.text_input("Enter the slope of the peak exercise ")
        with col3:
            ca= st.text_input("number of major vessels (0-3)")
        with col1:
            thal= st.text_input("thal: 0, 1 or 2")
        heart_diagnosis=' '
        if st.button("Heart Disease Test result"):
            
            try:
            # Convert input features to numeric values
                features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
                features = [float(feature) for feature in features]

                # Predict using XGBoost model
                heart_pred = heart_model.predict([features])

                # Update diagnosis based on prediction
                if heart_pred == 1:
                    heart_diagnosis = "The person is more likely affected by heart disease"
                else:
                    heart_diagnosis = "The person shows low probability for having heart disease"

            except Exception as e:
                st.error(f"Error predicting diabetes: {e}")
                heart_diagnosis = "Prediction error"

        st.success(heart_diagnosis)
        st.header('Attention! Follow the values given in the range please!') 
        st.markdown("""
            * **Age**
            * **Sex**: 0 represents Male and 1 represents Female
            * **Chest pain type**: [0-1-2-3]
            * **Resting blood pressure**: range[94-200]
            * **Serum cholestoral** : in mg/dl, range: [126-564]
            * **Fasting blood sugar** > 120 mg/dl Normal: 99 milligrams per deciliter (mg/dL) or lower,
                Prediabetes: 100 to 125 mg/dL,
                Diabetes: 126 mg/dL or higher.
                These levels represent the amount of sugar in your blood after fasting (typically not eating for at least 8 hours).
            * **Resting electrocardiographic results** (values 0,1,2)
            * **Maximum heart rate achieved:**: range[71-202]
            * **Exercise induced angina**: Binary value, range: 0 or 1
            * **Oldpeak** = Depression induced by exercise relative to rest, range: [0-6.2]
            * **The slope of the peak exercise ST segment**: range: [0-1-2]
            * **Number of major vessels** range: [0-3] colored by flourosopy
            * **Thal**: 0 = normal; 1 = fixed defect; 2 = reversable defect
    """)
            
            
    ## Parkinson---------------------------------------------     
    if selected=='Parkinson Disease Prediction':
        st.title(":person_frowning: Parkinson Disease Prediction ") #PAGE TILE
        st.subheader("Please read the Medical descriptions below before entering the values :exclamation:")
        col1, col2, col3, col4, col5=st.columns(5)
        #MDVP:Fo(Hz)         0
            # MDVP:Fhi(Hz)        0
            # MDVP:Flo(Hz)        0
            # MDVP:Jitter(%)      0
            # MDVP:Jitter(Abs)    0
            # MDVP:RAP            0
            # MDVP:PPQ            0
            # Jitter:DDP          0
            # MDVP:Shimmer        0
            # MDVP:Shimmer(dB)    0
            # Shimmer:APQ3        0
            # Shimmer:APQ5        0
            # MDVP:APQ            0
            # Shimmer:DDA         0
            # NHR                 0
            # HNR                 0
            # status              0
            # RPDE                0
            # DFA                 0
            # spread1             0
            # spread2             0
            # D2                  0
            # PPE 
        with col1:
            MDVP_Fo= st.text_input("MDVP_Fo-Avg vocal fund freq")
        with col2:
            MDVP_Fhi=  st.text_input("MDVP:Fhi-Max vocal fund freq")
        with col3:
            MDVP_Flo= st.text_input("MDVP:Flo-Min vocal fund freq")
        with col4:
            MDVP_Jitter= st.text_input("MDVP:Jitter-mesr1 of var in fund. freq.")
        with col5:
            MDVP_Jitter_Abs=st.text_input("MDVP_Abs-mesr2 of var in fund. freq.")
        with col1:
            MDVP_RAP= st.text_input("DVP_RAP-mesr3 of var in fund. freq.")
        with col2:
            MDVP_PPQ= st.text_input("MDVP:PPQ-mesr4 of var in fund. freq.")
        with col3:
            Jitter_DDP= st.text_input("Jitter:DDP-mesr5 of var in fund. freq.")
        with col4:
            MDVP_Shimmer= st.text_input("MDVP_Shimmer-mesr1 of var in amp")
        with col5:
            MDVP_Shimmer_dB= st.text_input("MDVP_Shimmer_dB-mesr2 of var in amp")
        with col1:
            Shimmer_APQ3= st.text_input("slopeShimmer_APQ3-mesr3 of var in amp")
        with col2:
            Shimmer_APQ5= st.text_input("Shimmer:APQ5_mesr4 of var in amp")
        with col3:
            MDVP_APQ= st.text_input("MDVP:APQ_mesr6 of var in fund. freq.")
        with col4:
            Shimmer_DDA= st.text_input(" Shimmer:DDA-mesr5 of var in amp")
        with col5:
            NHR = st.text_input("NHR-mesur1 of the ratio of noise in voice")
        with col1:
            HNR = st.text_input("HNR- measure2 of the ratio of noise to tonal comp in the voice")
        with col2:
            RPDE= st.text_input("RPDE-nonlinear dynamic complex mesr1")
        with col3:
            DFA= st.text_input("DFA-nonlinear dynamic complex meas2")
        with col4:
            spread1= st.text_input("spread1-nonlinear mesr1 of fund. freq.var")
        with col5:
            spread2= st.text_input("spread2-nonlinear mesr2 of fund. freq.var")
        with col1:
            D2= st.text_input("nonlinear dynamic complex mesr2")
        with col2:
            PPE= st.text_input("nonlinear mesr3 of fund freq var")
            
        park_diagnosis=' '
        if st.button("Parkinson Disease Test result"):
            
            try:
            # Convert input features to numeric values
                features = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
                features = [float(feature) for feature in features]

                # Prediction
                park_pred = parkinson_model.predict([features])

                # Update diagnosis based on prediction
                if park_pred == 1:
                    park_diagnosis = "The person has high probavility to have Parkinson disease"
                else:
                    park_diagnosis = "The person has less probability to have Parkinson disease"

            except Exception as e:
                st.error(f"Error predicting diabetes: {e}")
                park_diagnosis = "Prediction error"

        st.success(park_diagnosis)
        #-----------------------------------------
    
        st.markdown("""
            
            * **MDVP:Fo(Hz)** - Average vocal fundamental frequency. range: [88.33-260.10]
            * **MDVP:Fhi(Hz)** - Maximum vocal fundamental frequency. range: [103-593]
            * **MDVP:Flo(Hz)** - Minimum vocal fundamental frequency. range: [65.5-240]
            * **MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP** - Several measures of variation in fundamental frequency. range: [0.002-0.05]
            * **MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA** - Several measures of variation in amplitude. range: [0.000007-0.000260]
            * **HNR**: Harmonics-to-Noise Ratio. The range  could be between 10 and 30 or higher
            * **NHR** - Noise-to-Harmonics Ratio. range: [0-0.5]
            * **Status** - The health status of the subject (one) - Parkinson's, (zero) - healthy. range: [0.001-1.5]
            * **RPDE, D2** - Two nonlinear dynamical complexity measures. The range is typically between 0 and 1.
            * **DFA** - Signal fractal scaling exponent. range: [0-2]
            * **Spread1, Spread2** -  Nonlinear measures of fundamental frequency variation. range:[ -10 to 10.]
            * **PPE**:-Nonlinear Measure of Fundamental Frequency Variation.The range for PPE can vary and might be between 0 and 1.
    """)
except Exception as e:
    logging.error(f'An error occurred: {e}')
