#___________________________________________________________________________________________________________________
import streamlit as st
import os 

#___________________________________________________________________________________________________________________

st.set_page_config(
    page_title="Pathfinder 🗺️",
    layout="centered"
)

#___________________________________________________________________________________________________________________

st.markdown("<h1 style='text-align: center;'>Pathfinder 🗺️</h1>", unsafe_allow_html=True)

#___________________________________________________________________________________________________________________

def find_file(filename, path):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)
    return None

#___________________________________________________________________________________________________________________

#We Dont Talk About This Part Of The Code


#___________________________________________________________________________________________________________________


a=st.text_input("Enter the link of github repository")
b=st.text_input("Enter the name of the file you wanna find in the repository")
k=st.button("Run")

#___________________________________________________________________________________________________________________
if a=='':
    st.write("Please Enter the link of the github repository")
else:
    if b=='':
        st.write("Please Enter the name of the file you wanna find in the repository")
    else:
        if k:
            os.system("git clone "+a)
        
            folder_name=a.split("/")[-1]
            os.system("cd "+folder_name)
            #look though each and every folders of the github repo and find the file asked for and show the path of it 
            st.markdown("___")
            # st.write(st.markdown("*You Can Find Your File At: *"),find_file(b,folder_name))
            st.write("Path Of The File: ",find_file(b,folder_name))
            st.markdown("___")
            st.write("The File Can Be Found Here: ")
            #make the link for the file 
            
            link=a+"/blob/main/"+find_file(b,folder_name).split("/")[-1]
            st.write(link)
            st.markdown("___")
            os.system("rm -rf "+folder_name)
            os.system("clear")
#___________________________________________________________________________________________________________________