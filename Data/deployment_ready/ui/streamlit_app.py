
import requests
import streamlit as st

st.set_page_config(page_title='BlueStone ML UI', layout='wide')
st.title('BlueStone ML Deployment UI')
api_url = st.sidebar.text_input('API Base URL', 'http://127.0.0.1:8000')

tab1, tab2 = st.tabs(['Price Prediction', 'Inquiry SLA'])

with tab1:
    payload = {
        'property_type': st.selectbox('Property Type', ['single_family','condo','townhouse','multi_family']),
        'bedrooms': st.number_input('Bedrooms', min_value=0, value=3),
        'bathrooms': st.number_input('Bathrooms', min_value=0, value=2),
        'sqft': st.number_input('Square Feet', min_value=100.0, value=1800.0),
        'lot_size': st.number_input('Lot Size', min_value=0.0, value=5000.0),
        'year_built': st.number_input('Year Built', min_value=1800, max_value=2026, value=2010),
        'listing_status': st.selectbox('Listing Status', ['active','pending','sold']),
        'latitude': st.number_input('Latitude', value=37.7749),
        'longitude': st.number_input('Longitude', value=-122.4194),
        'data_quality_score': st.slider('Data Quality Score', 0, 100, 80),
    }
    if st.button('Predict Price'):
        st.json(requests.post(f'{api_url}/predict/price', json=payload, timeout=30).json())

with tab2:
    payload = {
        'inquiry_type': st.selectbox('Inquiry Type', ['info_request','viewing','offer']),
        'status': st.selectbox('Inquiry Status', ['responded','pending','cancelled','closed']),
        'inquiry_hour': st.slider('Inquiry Hour', 0, 23, 10),
        'inquiry_dayofweek': st.slider('Day of Week', 0, 6, 2),
        'has_property_id': st.selectbox('Has Property ID', [0,1], index=1),
        'user_type': st.selectbox('User Type', ['buyer','seller','agent','investor','renter']),
        'budget_mid': st.number_input('Budget Mid', value=300000.0),
        'budget_missing_flag': st.selectbox('Budget Missing Flag', [0,1], index=0),
        'property_type': st.selectbox('Property Type', ['single_family','condo','townhouse','multi_family'], key='pt2'),
        'bedrooms': st.number_input('Bedrooms', min_value=0, value=3, key='b2'),
        'bathrooms': st.number_input('Bathrooms', min_value=0, value=2, key='ba2'),
        'sqft': st.number_input('Square Feet', min_value=100.0, value=1800.0, key='sq2'),
        'listing_status': st.selectbox('Listing Status', ['active','pending','sold'], key='ls2'),
        'data_quality_score': st.slider('Data Quality Score', 0, 100, 80, key='dq2'),
        'office_location': st.text_input('Office Location', 'SAN FRANCISCO'),
        'agent_status': st.selectbox('Agent Status', ['active','inactive','on_leave']),
        'agent_experience_years': st.number_input('Agent Experience Years', min_value=0.0, value=5.0),
        'property_missing_flag': st.selectbox('Property Missing Flag', [0,1], index=0),
    }
    if st.button('Predict SLA'):
        st.json(requests.post(f'{api_url}/predict/inquiry-sla', json=payload, timeout=30).json())
