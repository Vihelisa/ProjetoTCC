from PIL import Image
from io import BytesIO
import base64
import streamlit as st


def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


def topbar(titulo):
    image = Image.open("title.png")

    # HTML e CSS para o topo
    st.markdown(f"""
        <style>
            .header {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0px 20px;
                width: 100%;
            }}
            .divider {{
                border-bottom: 1px solid #ccc;
                margin-bottom: 20px;
            }}
            .logo {{
                height: 45px;
            }}
            .titulo-direita{{
                font-size: 35px;
                font-weight: bold;
                color: #0B046E;
            }}
        </style>

        <div class="header">
            <img src="data:image/png;base64,{image_to_base64(image)}" class="logo">
            <div class="titulo-direita">{titulo}</div>
        </div>
        
        <div class="divider"></div>
    """, unsafe_allow_html=True)