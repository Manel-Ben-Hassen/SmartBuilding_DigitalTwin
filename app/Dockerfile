FROM python:3.10

WORKDIR /app
COPY streamlit_app.py .

RUN pip install streamlit requests

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]
