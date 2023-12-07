# Use a imagem base do Python
FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./install.sh

CMD ["./install.sh"]