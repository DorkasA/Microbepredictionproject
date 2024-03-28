import streamlit as st
import pandas as pd 
import warnings 
warnings.filterwarnings('ignore')
import joblib

st.markdown("<h1 style = 'color: #FB8B24; text-align: center; font-family: Helvetica'>PREDICTIVE MODELING FOR MICROBES CLASSIFICATION</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #76ABAE; text-align: center; font-family:cursive'> Built By: CHIMDINMA. D. AKPULONU</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('microbe-removebg-preview.png', use_column_width=True)
# st.header('Project Background Information', divider = True)
st.markdown("<h3 style = 'color: #4F6F52; text-align: center; font-family: Helvetica'>PREDICTIVE MODELING FOR MICROBES CLASSIFICATION</h3>", unsafe_allow_html = True)
st.write("Predictive modeling for Microbes aims to revolutionize microbial classification in the healthcare industry, thereby contributing to better disease prevention and treatment outcomes for patients worldwide.Machine learning creates a user friendly model that accurately classifies microbes, significantly speeding up diagnosis and improving healthcare outcomes through collaborative efforts among professionals across disciplines.")

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

df = pd.read_csv('microbes.csv')
st.dataframe(df)

st.sidebar.image('Screenshot_2024-03-28_160705-removebg-preview.png', caption='Welcome User')

st.sidebar.markdown("<br>", unsafe_allow_html= True)
st.sidebar.markdown("<br>", unsafe_allow_html= True)

# Decleare user input variables
st.sidebar.subheader('Input Variable', divider=True)
sel_cols = ['raddi', 'Orientation', 'Solidity', 'Perimeter',
            'Eccentricity', 'Extent', 'BoundingBox2', 'MinorAxisLength', 'MajorAxisLength', 'microorganisms']
raddi= st.sidebar.number_input('raddi')
Orientation= st.sidebar.number_input('Orientation')
Solidity= st.sidebar.number_input('Solidity')
Perimeter = st.sidebar.number_input('Perimeter')
Eccentricity = st.sidebar.number_input('Eccentricity')
Extent = st.sidebar.number_input('Extent')
BoundingBox2 = st.sidebar.number_input('BoundingBox2')
MinorAxisLength = st.sidebar.number_input('MinorAxisLengt')
MajorAxisLength = st.sidebar.number_input('MajorAxisLength')

# Display the users-input
input_var = pd.DataFrame()
input_var['raddi'] = [raddi]
input_var['Orientation'] = [Orientation]
input_var['Solidity'] = [Solidity]
input_var['Perimeter'] = [Perimeter]
input_var['Eccentricity'] = [Eccentricity]
input_var['Extent'] = [Extent]
input_var['BoundingBox2'] = [BoundingBox2]
input_var['MinorAxisLength'] = [MinorAxisLength]
input_var['MajorAxisLength'] = [MajorAxisLength]

st.markdown("<br>", unsafe_allow_html= True)
st.divider()
st.subheader('User Input Variables', divider=True)
st.dataframe(input_var, use_container_width=True)

# # Importing Transformers
# raddi = joblib.load('raddi_encoder.pkl')
# Orientation = joblib.load('Orientation_level_encoder.pkl')
# Solidity = joblib.load('Solidity_type_encoder.pkl')
# Perimeter = joblib.load('Perimeter_type_encoder.pkl')
# Eccentricity = joblib.load('Eccentricity_status_encoder.pkl')
# Extent = joblib.load('Extent_status_encoder.pkl')
# BoundingBox2 = joblib.load('BoundingBox2_status_encoder.pkl')
# MinorAxisLength = joblib.load('MinorAxisLength_status_encoder.pkl')
# MajorAxisLength = joblib.load('MajorAxisLength_status_encoder.pkl')

# microorganisms = joblib.load('microorganisms_status_encoder.pkl')
# model = joblib.load('Microbeprediction.pkl')



# # Applying transformations to the user's
# input_var['raddi'] = raddi.transform(input_var[['raddi']])
# input_var['Orientation'] = Orientation.transform(input_var[['Orientation']])
# input_var['Solidity'] = Solidity.transform(input_var[['Solidity']])
# input_var['Perimeter'] = Perimeter.transform(input_var[['Perimeter']])
# input_var['Eccentricity'] =  Eccentricity.transform(input_var[['Eccentricity']])
# input_var['Extent'] = Extent.transform(input_var[['Extent']])
# input_var['BoundingBox2'] = BoundingBox2.transform(input_var[['BoundingBox2']])
# input_var['MinorAxisLength'] = MinorAxisLength.transform(input_var[['MinorAxisLength']])
# input_var['MajorAxisLength'] = MajorAxisLength.transform(input_var[['MajorAxisLength']])

# input_var['microorganisms'] = microorganisms.transform(input_var[['microorganisms']])


# st.dataframe(input_var, use_container_width = True)

model = joblib.load('MicrobepredictionModel.pkl')
prediction = model.predict(input_var)

if st.button('MICROBE PREDICTION'):
    if prediction == 0:
        st.write(f'The predicted microorganism is Aspergillus sp')
    elif prediction == 1:
        st.write(f'The predicted microorganism is Diatom')
    elif prediction == 2:
        st.write(f'The predicted microorganism is Penicillum')
    elif prediction == 3:
        st.write(f'The predicted microorganism is Pithophora')
    elif prediction == 4:
        st.write(f'The predicted microorganism is Protozoa')
    elif prediction == 5:
        st.write(f'The predicted microrganism is Raizopus')
    elif prediction == 6:
        st.write(f'The predicted microorganism is Spirogyra')
    elif prediction == 7:
        st.write(f'The predicted microorganism is Ulothrix')
    elif prediction == 8:
        st.write(f'The predicted microorganism is Volvox')
    elif prediction == 9:
        st.write(f'The predicted microorganism is Yeast')



    else:
        st.write('Your Predicted Microrganism is not found')
        