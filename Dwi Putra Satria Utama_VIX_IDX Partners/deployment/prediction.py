import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load model
with open('dt_best.pkl', 'rb') as file:
    dt_best = pickle.load(file)

def run():

    with st.form('key=debtor_predict'):
        term_months = st.selectbox('The Number of Payments', ['36', '60'], help='The number of payments on the loan. Values are in months and can be either 36 or 60')
        grade = st.selectbox('Grade', ['A', 'B', 'C', 'D', 'E', 'F', 'G'], help='LC assigned loan grade')
        sub_grade = st.selectbox('Sub Grade', ['A1', 'A2', 'A3', 'A4', 'A5',
                                                'B1', 'B2', 'B3', 'B4', 'B5',
                                                'C1', 'C2', 'C3', 'C4', 'C5',
                                                'D1', 'D2', 'D3', 'D4', 'D5',
                                                'E1', 'E2', 'E3', 'E4', 'E5',
                                                'F1', 'F2', 'F3', 'F4', 'F5',
                                                'G1', 'G2', 'G3', 'G4', 'G5'], help='LC assigned loan subgrade')
        emp_length = st.selectbox('Employment Duration', ['< 1 year',
                                                           '1 year',
                                                           '2 years',
                                                           '3 years',
                                                           '4 years',
                                                           '5 years',
                                                           '6 years',
                                                           '7 years',
                                                           '8 years',
                                                           '9 years',
                                                           '10+ years',
                                                           'None'], help='Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years')
        emp_title = st.text_input('Employment Title', value='', help='Enter your employment title')
        home_ownership = st.selectbox('Home Ownership', ['Rent', 'Own',
                                                          'Mortage', 'Other',
                                                          'None', 'Any'], help='The home ownership status provided by the borrower during registration. Our values are: RENT, OWN, MORTGAGE, OTHER')
        verification_status = st.selectbox('Verification Status', ['Verified', 'Source Verified',
                                                                   'Not Verified'], help='A category provided by the borrower for the loan request')
        purpose = st.selectbox('Purpose', ['credit_card', 'car',
                                           'small_business', 'other',
                                           'wedding', 'debt_consolidation',
                                           'home_improvement', 'major_purchase',
                                           'medical', 'moving',
                                           'vacation', 'house', 'renewable_energy', 'educational'], help='A category provided by the borrower for the loan request')
        addr_state = st.selectbox('State', ['AZ', 'GA', 'IL', 'CA', 'OR', 'NC', 'TX', 'VA', 'MO', 'CT', 'UT', 'FL', 'NY', 'PA',
                                                             'MN', 'NJ', 'KY', 'OH', 'SC', 'RI', 'LA', 'MA', 'WA', 'WI', 'AL', 'CO', 'KS', 'NV',
                                                             'AK', 'MD', 'WV', 'VT', 'MI', 'DC', 'SD', 'NH', 'AR', 'NM', 'MT', 'HI', 'WY', 'OK',
                                                             'DE', 'MS', 'TN', 'IA', 'NE', 'ID', 'IN', 'ME'], help='The state provided by the borrower in the loan application')
        initial_list_status = st.selectbox('Listed', ['f', 'w'], help='The initial listing status of the loan. Possible values are – Whole, Fractional')
        annual_inc = st.number_input('Income', min_value=1896.0, max_value=7500000.0, value=1896.0, step=0.01, help='The self-reported annual income provided by the borrower during registration')
        int_rate = st.number_input('Interest Rate', min_value=5.42, max_value=26.06, value=5.42, step=0.01, help='Indicates if income was verified by LC, not verified, or if the income source was verified')
        dti = st.number_input('Debt to Income', min_value=0.00, max_value=39.99, value=0.00, step=0.01, help='A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income')
        loan_status = st.selectbox('Status', ['Fully Paid',
                                               'Charged Off',
                                               'Current',
                                               'Default',
                                               'Late (31-120 days)',
                                               'In Grace Period',
                                               'Late (16-30 days)',
                                               'Does not meet the credit policy. Status:Fully Paid',
                                               'Does not meet the credit policy. Status:Charged Off'], help='Current status of the loan')
        
        st.markdown('---')

        # Tambahkan tombol submit di dalam form
        submitted = st.form_submit_button('Predict')

    new_data = {
        'term_months': term_months,
        'grade': grade,
        'sub_grade': sub_grade,
        'emp_length': emp_length,
        'emp_title': emp_title,
        'home_ownership': home_ownership,
        'verification_status': verification_status,
        'purpose': purpose,
        'addr_state': addr_state,
        'initial_list_status': initial_list_status,
        'annual_inc': annual_inc,
        'int_rate': int_rate,
        'dti': dti,
        'loan_status': loan_status


    }

    new_data = pd.DataFrame(new_data, index=[0])
    st.dataframe(new_data)

    if submitted:
        pred = dt_best.predict(new_data)

        # Menampilkan hasil prediksi
        st.subheader('Hasil Prediksi')
        if pred == 1:
            st.write("Calon Debitur Memiliki Risiko Kredit")
        else:
            st.write("Calon Debitur Tidak Memiliki Risiko Kredit")

if __name__ == '__main__':
    run()