import streamlit as st

class buttons:
   # def __init__(self,buttons_name):
        #if st.button(f"square of{buttons_name}"):
           # st.toast(int(buttons_name)**2)

#for i in range(10):
    #buttons(i)
    def __init__(self,num):
        if st.button(f"button number is {num}"):
            self.calc(num*num)
    def calc(self,num):
        if num%2==0:
            st.balloons()
        else:
            st.snow()
for i in range(10):
        buttons(i)

      
    