import streamlit as st
import base64
from PIL import Image
import pandas as pd
import requests
from omegaconf import OmegaConf
import json
import os 

from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error
from omegaconf import OmegaConf


load_dotenv()
port_config = os.getenv("DB_IP")


# Load background images
#add_bg_from_local("storage/frontend/logo.jpeg")
image_id = Image.open("app/images/id.png")
image_stablediff = Image.open("app/images/butterfly.jpeg")
image_faceResto = Image.open("app/images/faceresto.jpeg")

# Page title
st.write("# ESCERCLOUD AI Computer Vision Services - Demo! 👋")
# Page description
st.sidebar.success("Select a demo above.")

app_mode = st.sidebar.selectbox(
    "Options",
    ["Info", "History"],
)
if app_mode == "Info":
    st.write("# Document Understanding")
    st.write(
    "###### Document understanding is the process of automatically extracting, classifying, interpreting, contextualising, and searching information from documents using machine learning, computer vision, and natural language processing technologies. Major use cases include KYC, KYB, reviewing text within legal contracts, leases, and other documents to automate business processes."
)
    st.image(image_id)
    st.markdown(
    """ # Stable Diffusion 
###### Stable Diffusion includes text-to-image,and image-to-image models that enables users to create stunning art within seconds. **Versions1**  and **Version 2** of Stable Diffusion generate images with resolutions of **512x512** and **768x768** pixels in turn, respectively, in a matter of seconds."""
)
    st.image(
    image_stablediff,
    caption=" image generated by stable  diffudion with the prompt of beautiful butterfly anatomy diagram, bold shūji, chart, schematics, infographic, scientific, measurements, abstract, surreal, collage, new media design, poster, colorful highlights, tarot card, glowing ruins, marginalia, 8k, extremely detailed, dark color palette + style of Katsuhiro Otomo + Masamune Shirow + pantone, on black canvas, typography annotations",
)
    st.markdown(
    """ # Face Restoration
###### Face restoration recovers high-quality faces from the low-quality counterparts suffering from unknown degradation, such as low-resolution, noise, blur, compression artifacts, etc."""
)
    st.image(
    image_faceResto,
    caption=" Comparisons of the quality of restored faces using state-o-the-art AI model.",
)
elif app_mode == "History":
    password = st.text_input("Enter a password", type="password")
    if password == "@idem0":
        db_req = requests.post(
                            f"http://{port_config}:8509/widgets"
                        )
        db_req = db_req.json()
        df = pd.DataFrame.from_records(db_req["data"])
        st.table(df)