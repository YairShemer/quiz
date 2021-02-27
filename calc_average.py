import streamlit as st

st.title('מחשבון')
st.write('אנא הכנס שני מספרים')
#st.write('Please enter 2 numbers:')

number_1 = st.sidebar.number_input('המספר הראשון')
number_2 = st.sidebar.number_input('המספר השני')
operation = st.sidebar.selectbox('פעולה', ['+', '-', '*', ':'])

if st.button('בדיקה'):
    if operation == '+':
        st.write(number_1 + number_2)
    elif operation == '-':
        st.write(number_1 - number_2)
    elif operation == '*':
        st.write(number_1 * number_2)
    elif operation == ':':
        st.write(number_1 / number_2)