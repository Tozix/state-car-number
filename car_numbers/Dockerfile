FROM python:3.10-slim
LABEL author='Tozix' version=0.0.1Beta
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "car_numbers.wsgi:application", "--bind", "0:8000" ]

