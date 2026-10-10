"""
MVP — інтерфейс (стартовий шаблон)
курс «Інноваційні технології», заняття 10 (модуль «AI Startup Sprint»).
"""

import streamlit as st
from ai_function import main_ai_function
import os

# ---------------------------------------------------------------------------
# Streamlit-інтерфейс
# ---------------------------------------------------------------------------

# Крок 1: Назва та опис
st.set_page_config(page_title="Summer Map", page_icon="")
st.title("Summer Map")
st.caption("Создает карту с маршрутом, где больше тенька")

# Крок 3: Поле ввода (теперь просим конкретно город)
user_input = st.text_input("Введи название города:")

# Крок 4 и показ результата
if st.button("Запустити"):
    if user_input:
        with st.spinner("Зачекайте..."):
            result = main_ai_function(user_input)
            st.subheader("Результат")
            st.write(result)
    else:
        st.warning("Пожалуйста, введи название города!")

def get_secret(name):
    key = os.getenv(name)
    if key:
        return key
    try:
        return st.secrets[name]
    except Exception:
        return None