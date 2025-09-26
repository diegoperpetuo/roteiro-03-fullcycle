FROM python:3.10

WORKDIR /app

RUN pip install scipy
RUN pip install statsmodels

RUN pip install numpy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install matplotlib
RUN pip install seaborn

COPY script.py /app/script.py

CMD ["python", "/app/script.py"]