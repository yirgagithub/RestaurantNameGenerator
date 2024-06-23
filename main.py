import streamlit as st
from restaurant_name_generator import generate_restaurant_name
st.title("Restaurant Name Generator")

nationality = st.sidebar.selectbox('Pick a nationality', ('Indian', 'Arabic', 'Ethiopian', 'Eritrean', 'Italian', 'Greek', 'Estonia', 'Brazil'))

if nationality:
    response = generate_restaurant_name(nationality)
    st.header(response['restaurant_name'])

    menu_items = response['restaurant_menu'].strip().split(',')

    st.write('**Menu Items**')
    for item in menu_items:
        st.write('-', item)
