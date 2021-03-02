import streamlit as st

st.title('חידה')
st.write('הוראות: עליך לנחש מי מחברי התחום כתב לך את החידה הזאת')
st.write('יש לך 100 נקודות לצורך כך')
st.write('כל ניחוש מוריד 30 נקודות')
st.write('כל רמז מוריד 10 נקודות (לחץ על הרמז שברצונך לקבל)')
x = 100
operation2 = st.sidebar.selectbox('מי אני?', ['לא ניחשת עדיין','איל','איל','איל','איל','איל','יאיר','איל','איל', 'מיה', 'אלון', 'בוריס'])
operation = st.sidebar.subheader('מספר הנקודות שנותרו לך')
operation = st.sidebar.header(x)

if operation2 == 'יאיר':
    st.sidebar.text('כל הכבוד!')
elif operation2 == 'לא ניחשת עדיין':
    pass
elif operation2:
    x = x - 30
    operation.header(x)

# num_of_km = '-'
# common_privet = '-'
#
# # st.text_area('1')
# # st.text_area('2')
col1, col2, col3 = st.beta_columns(3)
# col1.header('sdfsdf1')


# col2.header('sdfsdf2')
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write('data')

if col1.checkbox('מספר הקילומטרים בין הבית שלך לבית שלי'):
    col1.header('100')
    x = x - 10
    operation.header(x)
else:
    col1.header('-')

if col1.checkbox('מספר האותיות המשותפות לשמות הפרטיים שלנו:'):
    col1.header('1')
    x = x - 10
    operation.header(x)
else:
    col1.header('-')

if col2.checkbox('מספר האותיות המשותפות לשמות המשפחה שלנו:'):
    col2.header('1')
    x = x - 10
    operation.header(x)
else:
    col2.header('-')

if col2.checkbox('מספר החדר שלך פחות מספר החדר שלי:'):
    col2.header('2')
    x = x - 10
    operation.header(x)
else:
    col2.header('-')

if col3.checkbox('הודעה ששלחת אלי:'):
    col3.header('1')
    x = x - 10
    operation.header(x)
else:
    col3.header('-')

if col3.checkbox('הודעה ששלחתי אליך:'):
    col3.header('2')
    x = x - 10
    operation.header(x)
else:
    col3.header('-')
    # st.write('data2')

# if st.button('רמז: מספר הקילומטרים בין הבית שלך לבית שלי (בערך)'):
#     col1.subheader('sdfsdf1')
#
# if st.button('מספר האותיות המשותפות לשמות הפרטיים שלנו:'):
#     # common_privet = 1
#     col2.subheader('sdfsdf2')

