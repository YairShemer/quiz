import streamlit as st

def hint(hint_title, hint_text, col, score, operation):
    if col.checkbox(hint_title):
        col.header(hint_text)
        score = score - 10
        operation.header(score)
    else:
        col.header('********')
    return score

st.title('חידה')
st.write('הוראות: עליך לנחש מי מחברי התחום כתב לך את החידה הזאת')
st.write('יש לך 100 נקודות לצורך כך')
st.write('כל ניחוש מוריד 30 נקודות')
st.write('כל רמז מוריד 10 נקודות (לחץ על הרמז שברצונך לקבל)')
score = 100
operation = st.sidebar.subheader('מספר הנקודות שנותרו לך')
operation = st.sidebar.header(score)
persons_list = ['איל', 'קובי', 'פוני', 'נדב', 'מאיה', 'מתן ג', 'מתן ב', 'אלון', 'אשרי', 'יאיר', 'תמר', 'בועז', 'משה', 'בוריס', 'מאיר']
defult_selection = ['לא ניחשת עדיין']
defult_selection.extend(persons_list)
selected_person = st.sidebar.radio('מי אני?', defult_selection)


pre_selected_person = str(selected_person)
if selected_person == 'יאיר':
    operation.header('כל הכבוד!!')

else:
    for person in persons_list:
        if selected_person == person:
            score = score - 50
            operation.header(score)
# elif selected_person == pre_selected_person:
#     pass
# elif selected_person != pre_selected_person:
#     score = score - 30
#     operation.header(score)
#     pre_selected_person = str(selected_person)

col1, col2 = st.beta_columns(2)

score = hint(hint_title='מספר הקילומטרים בין הבית שלך לבית שלי', hint_text='100', col=col1, score=score, operation=operation)
score = hint(hint_title='מספר האותיות המשותפות לשמות הפרטיים שלנו:', hint_text='1',col=col1, score=score, operation=operation)
score = hint(hint_title='מספר החדר שלך פחות מספר החדר שלי:', hint_text='',col=col1, score=score, operation = operation)
score = hint(hint_title='וצאפ ששלחת פעם אלי', hint_text='בפאטיו בצד ימין, מחכים רק לך',col=col2, score=score, operation = operation)
score = hint(hint_title='וצאפ ששלחתי פעם אליך', hint_text='ערערתי וקיבלתי אישור לא להיכנס לבידוד (:',col=col2, score=score, operation = operation)
score = hint(hint_title='מכר משותף שלנו', hint_text='המנהל שלי לשעבר למד איתך בתואר הראשון',col=col2, score=score, operation = operation)
# hint(hint_title='', hint_text='',col=col3, score=score, operation = operation)
# hint(hint_title='', hint_text='',col=col3, score=score, operation = operation)
# hint(hint_title='', hint_text='',col=col3, score=score, operation = operation)



