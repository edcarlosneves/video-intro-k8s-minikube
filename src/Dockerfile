FROM python:3.10.13-alpine3.19
ADD ./requirements/base.txt /requirements/base.txt
RUN pip install --upgrade pip
RUN pip install -r requirements/base.txt
WORKDIR /app
COPY /app /app
CMD ["uvicorn", "generate_order:app", "--host", "0.0.0.0", "--port", "8000"]