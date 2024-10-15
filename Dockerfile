FROM python:3.10-slim

WORKDIR /code
COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run", "src/app.py", "--port", "80", "--reload"]