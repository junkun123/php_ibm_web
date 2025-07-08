FROM python:3.11-slim

RUN apt-get update && apt-get install -y gcc g++ python3-dev libaio1 wget unzip && rm -rf /var/lib/apt/lists/*

RUN wget https://public.dhe.ibm.com/ibmdl/export/pub/software/data/db2/drivers/odbc_cli/linuxx64_odbc_cli.tar.gz && \
    mkdir -p /opt/ibm/db2_cli_odbc_driver && \
    tar -xzf linuxx64_odbc_cli.tar.gz -C /opt/ibm/db2_cli_odbc_driver && \
    rm linuxx64_odbc_cli.tar.gz

ENV IBM_DB_HOME=/opt/ibm/db2_cli_odbc_driver/clidriver
ENV LD_LIBRARY_PATH=$IBM_DB_HOME/lib
ENV PATH=$PATH:$IBM_DB_HOME/bin:$IBM_DB_HOME/adm

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
