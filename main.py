import streamlit as st
import time
from openai import OpenAI

client = OpenAI(api_key=st.secrets["API_KEY"])

# 코드스니펫 - 제목
st.title('[스파르타] 제품 홍보 포스터 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
    with st.spinner('생성 중입니다.'):
        chat_completion = client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": keyword + '라는 주제로 새로운 제품을 홍보할 수 있는 카피를  150자로 알려줘', 
            }],
            model="gpt-4o",
        )
        chat_result = chat_completion.choices[0].message.content

        response = client.images.generate(
            model="dall-e-3",
            prompt=keyword,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        st.write(chat_result)
        st.image(image_url)