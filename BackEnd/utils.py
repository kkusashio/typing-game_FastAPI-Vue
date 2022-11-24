import pandas
import requests
import re
from api.models.word import Base

# データベースを初期化
def reset_database():
    from sqlalchemy import create_engine
    DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
    engine = create_engine(DB_URL, echo=True)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# API経由で単語を登録
def add_word_from_xlsx(file_path: str) -> None:
    df = pandas.read_excel(file_path)
    for index, row in df.iterrows():
        if (index == 10):
            break
        english_word = row['eng']
        japanese_word = row['jpn']
        level = 5

        requests.post('http://localhost:8000/word_list', json={
            'English_word': english_word,
            'Japanese_word': japanese_word,
            'level': level
        })


if __name__ == "__main__":
    # add_word_from_xlsx('./tmp/toeic990.xlsx')
    reset_database()
