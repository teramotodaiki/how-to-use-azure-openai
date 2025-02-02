# PythonでAzure OpenAIを使う

このガイドでは、Pythonを使ってAzure OpenAIのAIと会話する方法を説明します。

## 必要なもの
- Python（バージョン3.7以上）
  - まだPythonをインストールしていない人は、[Pythonの公式サイト](https://www.python.org/downloads/)からダウンロードしてインストールしてください。
- openaiライブラリ
  - コマンドプロンプト（WindowsのPowerShellやMacのターミナル）で以下のコマンドを実行してインストールします：
    ```bash
    pip install openai
    ```

## サンプルプログラム

[hello_ai.py](../../samples/python/hello_ai.py)を見てみましょう。このプログラムは、AIと簡単な会話をするプログラムです。

### プログラムの説明

1. まず、必要な道具（ライブラリ）を用意します：
```python
from openai import AzureOpenAI
```

2. AIクライアントを準備します：
```python
client = AzureOpenAI(
    api_key="あなたのAPIキー",
    api_version="2024-11-01-preview",
    azure_endpoint="あなたのエンドポイント"
)
```
※ `api_key`と`azure_endpoint`は、自分のものに置き換えてください。

3. AIと会話します：
```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "こんにちは！私の名前は田中です。"}
    ]
)
```
※ `model`は、自分が使えるモデル名に置き換えてください。

4. AIの返事を表示します：
```python
print("AI:", response.choices[0].message.content)
```

## プログラムの実行方法

1. プログラムを実行する前に、以下の3つの情報を自分のものに書き換えてください：
   - `api_key`：APIキー
   - `azure_endpoint`：エンドポイント
   - `model`：使用するモデル名

2. コマンドプロンプトで以下のコマンドを実行します：
```bash
python hello_ai.py
```

## 会話を続ける方法

AIとの会話を続けたい場合は、`messages`リストに会話の履歴を追加していきます：

```python
messages = [
    {"role": "user", "content": "こんにちは！私の名前は田中です。"},
    {"role": "assistant", "content": "こんにちは、田中さん！お会いできて嬉しいです。"},
    {"role": "user", "content": "好きな食べ物は何ですか？"}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
```

## 用語解説

- **ライブラリ**：プログラムを書くときに使える便利な道具箱のようなものです。
- **API**：コンピュータープログラム同士が会話するための約束事です。
- **クライアント**：サービス（この場合はAI）を利用するためのプログラムです。
