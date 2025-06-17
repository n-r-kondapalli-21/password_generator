import random
import streamlit as st
alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
  'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dig=['1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','&']
background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20230620/pngtree-secure-your-personal-data-with-3d-lock-and-password-field-a-image_3650162.jpg"

# Inject custom CSS for background with overlay for better readability
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    
    /* Add a semi-transparent overlay to make text more readable */
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 2rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("in this page you can generate password!!!")
letter_n=(st.number_input("enter how many letters u want in u'r password:",min_value=0,step=1))
dig_n=(st.number_input("enter how many digits u want in u'r password:",min_value=0,step=1))
if dig_n<2:
    st.text("the password must require minimus 2 digit for more pravacy!! ")
else:    
    sym_n=(st.number_input("enter how many symbols want in u'r password:",min_value=0,step=1))
    if sym_n<1:
        st.text("the password must require minimum 1 symbol for more privacy!!")
    else:
        total_size=letter_n+dig_n+sym_n
        if  total_size>=8:
            list=[]
            for i in range(1,letter_n+1):
                list+=random.choice(alp)
            for i in range(1,dig_n+1):
                list+=random.choice(dig)
            for i in range(1,sym_n+1):
                list+=random.choice(sym)    
            random.shuffle(list)
            password="" 
            for j in list:
                password+=j  
            st.success(f"here the generated password is :-{password}") 
        else:
            st.warning("THE PASSWORD MUST REQUIRE MINIMUM (8) ELEMENTS ")