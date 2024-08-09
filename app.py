from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

# ---- Use LOcal CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
    
# ---- LOAD ASSESTS ----
lottie_coding = load_lottieurl("https://lottie.host/85aa4d59-9369-4ba5-951d-3dbf2c65339b/XCyeuEJerb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Saif Anas :wave:")
    st.title("A Devops Engineer From India")
    st.write("I am passionate about finding ways to use Python and driven by the relentless pursuit of seamless integration and automation, fueling innovation and efficiency in every aspect of software development and deployment.")
    st.write("[Learn More >](https://github.com/saifanas)")
    
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
                DevOps Engineer might do in their daily life:            
                - Automating Workflows: Automate software deployment pipelines using tools like Jenkins or GitLab CI/CD, ensuring swift and reliable delivery of code changes.

                - Maintaining Infrastructure: They configure and manage cloud infrastructure using platforms like AWS or Azure, ensuring scalability, reliability, and cost-effectiveness.

                - Monitoring and Troubleshooting: DevOps Engineers monitor system performance using tools like Prometheus or Nagios, swiftly diagnosing and resolving issues to maintain optimal system health and availability.
            """
    )
    st.write("[Github Link >](https://github.com/saifanas)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")    
        
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("A simple distributed application running across multiple Docker containers.")
        st.write(
            """
            A front-end web app in Python which lets you vote between two options.
            A Redis which collects new votes.
            A .NET worker which consumes votes and stores them in.
            A Postgres database backed by a Docker volume.
            A Node.js web app which shows the results of the voting in real time.
            """
        )
        st.markdown("[Clone...](https://github.com/saifanas/sample-voting-app.git)")

# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do!
#             """
#         )
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)

# ---- CONTACT FORM ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    # Documentation:
    
    contact_form = """
    <form action="https://formsubmit.co/saifanas718@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" palceholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()