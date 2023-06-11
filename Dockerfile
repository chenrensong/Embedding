FROM python:3.11.3-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY ./model /code/model
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]