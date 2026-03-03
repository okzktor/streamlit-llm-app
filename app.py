
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from openai import OpenAI

st.title("サンプルアプリ②: LLM機能を搭載したWebアプリ")

st.write("##### 動作モード1: レシピ提案")
st.write("料理名を入力するとレシピを提案します")
st.write("##### 動作モード2: トレーニングメニュー提案")
st.write("空き時間(分)を入力すると、その時間内で行えるトレーニングメニューを提案します")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["レシピ提案", "トレーニングメニュー提案"]
)

st.divider()

if selected_item == "レシピ提案":
    input_message = st.text_input(label="料理名を入力してください。")




else:
    time_limit = st.text_input(label="空き時間(分)を入力してください。")




if st.button("実行"):
    st.divider()
    if selected_item == "レシピ提案":
        if input_message:
            try:
                client = OpenAI()
                first_completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "あなたは料理研究家です。入力されたメニューのレシピを提案します。"},
                        {"role": "user", "content": input_message}
                    ],
                    temperature=0.5
                )
                answer = first_completion.choices[0].message.content
                st.write(f"{input_message}のレシピ: {answer}")
            except Exception as e:
                st.error(f"LLM呼び出しでエラーが発生しました: {e}")

        else:
            st.error("入力してから「実行」ボタンを押してください。")



    if selected_item == "トレーニングメニュー提案":
        if time_limit:
            try:
                client = OpenAI()
                first_completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "あなたは熟練のパーソナルトレーナーです。入力された分数でできるトレーニングメニューを提案します。"},
                        {"role": "user", "content": time_limit}
                    ],
                    temperature=0.5
                )
                answer = first_completion.choices[0].message.content
                st.write(f"{time_limit}分でできるトレーニングメニュー: {answer}")
            except Exception as e:
                st.error(f"LLM呼び出しでエラーが発生しました: {e}")

        else:
            st.error("入力してから「実行」ボタンを押してください。")
