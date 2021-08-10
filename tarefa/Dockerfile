# Base
FROM python:3.8-slim

# copia tudo dentro do contexto para o diretorio /app dentro do container
COPY . /app  

# set o /app como diretorio base com WORKDIR
WORKDIR /app  

# installs do python com RUN
RUN pip install flask 
RUN pip install pandas
RUN pip install fastapi
RUN pip3 install fastapi uvicorn 

# requerimento para rodar o flask run
ENV FLASK_APP=flask_app.py  

# comando rodado ao iniciar o container
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080", "--reload"]
