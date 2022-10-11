
import streamlit
streamlit.title('My parents new Healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3  & Blueberry Oatmeal')
streamlit.text('🥗 Kale, spinach & Rocket smoothie')
streamlit.text('🐔Hard-Boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
