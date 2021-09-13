FROM python:3.7

RUN apt-get update \
&& apt-get install --no-install-recommends unixodbc-dev gcc g++ default-jre -y

RUN pip install --upgrade pip setuptools wheel \
&& pip cache purge \
&& apt-get autoremove -y \
&& rm -rf /var/lib/apt/lists/* \
&& rm -rf /root/.cache/pip

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN bash install_heideltime_standalone.sh

EXPOSE 8501

CMD ["streamlit", "run", "ui.py"]