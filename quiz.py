import streamlit as st

def hint(hint_title, hint_text, col, score, operation):
    if col.checkbox(hint_title):
        col.header(hint_text)
        score = score - 10
        operation.header(score)
    else:
        col.header('********')
    return score

def person_checkbox(person, score):
    if st.sidebar.checkbox(person):
        if  person!= 'יאיר':
            score = score - 30
            operation.header(score)
        else:
            st.sidebar.header('כל הכבוד!!')
    return score


def nice_text(text):
    return "<h2 style='text-align: center; color: blue;'>{}</h2>".format(text)

st.title('חידה')
st.write('הוראות: עליך לנחש מי מחברי התחום כתב לך את החידה הזאת')
st.write('יש לך 100 נקודות לצורך כך')
st.write(nice_text("כל ניחוש מוריד 30 נקודות"), unsafe_allow_html=True)
st.write(nice_text("כל רמז מוריד 10 נקודות (לחץ על הרמז שברצונך לקבל)"), unsafe_allow_html=True)
score = 100
operation = st.sidebar.subheader('מספר הנקודות שנותרו לך')
operation = st.sidebar.header(score)
persons_list = ['איל', 'קובי', 'פוני', 'נדב', 'מאיה', 'מתן ג', 'מתן ב', 'אלון', 'אשרי', 'יאיר', 'תמר', 'בועז', 'משה', 'בוריס', 'מאיר']
# selection_list = ['לא ניחשת עדיין']
# selection_list.extend(persons_list)
selection_list = persons_list
# selected_person = st.sidebar.radio('מי אני?', selection_list)


# pre_selected_person = str(selected_person)
# if selected_person == 'יאיר':
#     operation.header('כל הכבוד!!')
#
# else:
for person in persons_list:
    score = person_checkbox(person, score)

# elif selected_person == pre_selected_person:
#     pass
# elif selected_person != pre_selected_person:
#     score = score - 30
#     operation.header(score)
#     pre_selected_person = str(selected_person)

col1, col2 = st.beta_columns(2)

score = hint(hint_title='מספר הקילומטרים בין הבית שלך לבית שלי ', hint_text='37', col=col1, score=score, operation=operation)
col1.empty()
score = hint(hint_title='מספר האותיות המשותפות לשמותינו הפרטיים:', hint_text='1',col=col1, score=score, operation=operation)

# score = hint(hint_title='מספר החדר שלך פחות מספר החדר שלי:', hint_text='',col=col1, score=score, operation = operation)
score = hint(hint_title='וצאפ ששלחת פעם אלי', hint_text='בפאטיו בצד ימין, מחכים רק לך',col=col2, score=score, operation = operation)
col1.empty()
score = hint(hint_title='וצאפ ששלחתי פעם אליך', hint_text='ערערתי וקיבלתי אישור לא להיכנס לבידוד (:',col=col2, score=score, operation = operation)
col1.empty()
score = hint(hint_title='מכר משותף שלנו', hint_text='המנהל שלי לשעבר למד איתך בתואר הראשון',col=col2, score=score, operation = operation)
# hint(hint_title='', hint_text='',col=col3, score=score, operation = operation)
# hint(hint_title='', hint_text='',col=col3, score=score, operation = operation)
# hint(hint_title='', hint_text='',col=col3, score=score, operation = operation)



