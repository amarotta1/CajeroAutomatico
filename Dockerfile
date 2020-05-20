  
FROM python:3



RUN git clone https://github.com/amarotta1/CajeroAutomatico.git



WORKDIR /CajeroAutomatico



RUN pip install -r requirements.txt



CMD ["python3", "./test_cajero_ex.py"]