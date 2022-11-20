FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
# コンテナ内で必要なパッケージをインストール
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt 

#  DBのマイグレーション
#  dbコンテナが起動していることを前提としている(docker-composeのdepend_onで指定)
# COPY ./api/ .
# RUN python migrate_db.py

COPY main.py .
EXPOSE 8000
# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]