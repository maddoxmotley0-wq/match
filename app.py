import streamlit as st
import random

st.title("Match Test 💚")
p1 = st.text_area("Person 1: ")
p2 = st.text_area("Person 2: ")

if st.button("[Test]"):
    match1 = random.randint(0,100)
    if match1 > 50 and match1 <= 70:
        match = f'{p1} and {p2} are Likley, {match1}%'
    elif match1 > 70:
        match = f'{p1} and {p2} are SUPER Likley, {match1}%'
    elif match1 < 50 and match1 >= 30:
        match = f'{p1} and {p2} are Unlikley, {match1}%'
    elif match1 < 30:
        match = f'{p1} and {p2} are HIGHLY Unlikley, {match1}%'
    elif match1 == 50:
        match = f'{p1} and {p2} are Undecided, {match1}%'
    st.write(match)
