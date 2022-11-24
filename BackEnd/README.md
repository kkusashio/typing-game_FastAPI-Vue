# BackEndの実装リポジトリ

## 環境構築

(前提：Dockerがインストールされていること)

`BackEnd`ディレクトリ内で以下を実行し、APIサーバおよびDBサーバ用のDockerイメージをビルドする。
(と同時にDockerコンテナを起動している)
```
docker-compose up
```

この状態ではまだDBコンテナ内にテーブルなどのデータが存在しないため、以下のコマンドを実行する。

（あまり美しくないため、他にいい方法がないか模索）
```
docker exec {api_containerのid} python -m api.migrate_db
```

ここまで実行すると、ホストマシンの8000番ポートにAPIサーバが開かれる。

http://127.0.0.1:8000/docs にアクセスすると、それぞれのAPIの動作確認ができる。
（なんかSwagger UIとかいうやつらしい？）

## APIエンドポイント仕様

<details>
<summary>単語関連のエンドポイント</summary>

### 全単語を取得
- HTTPメソッド：GET
- エンドポイント：`/word_list`
- レスポンス例

```
[
  {
    "id": 1,
    "English_word": "hello",
    "Japanese_word": "こんにちは",
    "level": 1
  },
  {
    "id": 2,
    "English_word": "world",
    "Japanese_word": "世界",
    "level": 2
  },
]
```

### 新しい単語を追加
- HTTPメソッド； POST
- エンドポイント： `/word_list`
- リクエストボディ例：
```
{
  "English_word": "hello",
  "Japanese_word": "こんにちは",
  "level": 1
}
```
- レスポンス例：

```
{
  "English_word": "hello",
  "Japanese_word": "こんにちは",
  "level": 1,
  "id": 1
}
```

### 既存の単語を編集（あまり使わないかも）
- HTTPメソッド； PUT
- エンドポイント： `/word_list/{word_id}`
- リクエストボディ例：
```
{
  "English_word": "update",
  "Japanese_word": "更新",
  "level": 1
}
```
- レスポンス例：

```
{
  "English_word": "update",
  "Japanese_word": "更新",
  "level": 1,
  "id": 1
}
```

### 単語を削除
- HTTPメソッド: DELETE
- エンドポイント： `/word_list/{word_id}`

### ゲーム用の単語セットを取得
- HTTPメソッド： GET
- エンドポイント： `/word_list/set`
- クエリパラメータ
  - `word_num`：返される単語の数。
  - `word_level`：返される単語のレベル(-1の場合、全レベルから選択)

**注意点**
現時点では、word_levelの実装でバグが取れていません。
word_levelを指定すると、500エラーが発生するので、まだ`word_level`は使わないでください。

</details>

## 参考ページ

[Dockerを使った軽量なFastAPIの開発環境を構築](https://qiita.com/satto_sann/items/fcd3832a1fea2c607b85)

[FastAPI入門](https://zenn.dev/sh0nk/books/537bb028709ab9)
