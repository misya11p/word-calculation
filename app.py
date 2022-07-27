import streamlit as st
from word2vec import word_calculation

def main():
    title()
    select_words()
    calculation()

def title():
    st.title('word2vecで遊ぶ')
    st.write('word2vecをweb上から簡単に扱うことができるアプリケーションです。\n')
    st.write('単語の足し引きします。以下の欄に単語をカンマ区切りで書いてください。')

def select_words():
    global add, subtract
    add = st.text_input('足す単語')
    subtract = st.text_input('引く単語')

def calculation():
    n = st.number_input('表示する候補の数', 10)
    if st.button('計算する'):
        if add or subtract:
            try:
                df = word_calculation(add, subtract, n)
                st.table(df)
            except:
                st.info('辞書に含まれていない単語が存在します')
        else:
            st.write('単語を入力してください。')


if __name__ == '__main__':
    main()