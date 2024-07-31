import streamlit as st

st.header("Upload and Replace image")

uploadedfile = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

if st.button("Change image"):
    if uploadedfile:
        with open('logo.png', 'wb') as writename:
            writename.write(uploadedfile.getbuffer())
#getbuffer helps you to view the file contents as bytes/binary
#write helps you overwrite the content name as bytes/binary

        st.write("Image changed")

    else:
        st.write("upload image first")