FROM python:3.9.5

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

ENV SQL_PATH="sqlite:///tecnocars.db"

COPY . .

CMD ["uvicorn", "config:app", "--host", "0.0.0.0", "--port", "8000"]
