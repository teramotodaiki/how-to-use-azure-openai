# LangChainでAzure OpenAIを使う

このガイドでは、LangChainを使ってAzure OpenAIのAIと会話する方法を説明します。LangChainは、AIアプリケーションを簡単に作るためのツールです。

## 必要なもの
- Python（バージョン3.7以上）
  - まだPythonをインストールしていない人は、[Pythonの公式サイト](https://www.python.org/downloads/)からダウンロードしてインストールしてください。
- openaiとlangchainライブラリ
  - コマンドプロンプト（WindowsのPowerShellやMacのターミナル）で以下のコマンドを実行してインストールします：
    ```bash
    pip install openai langchain
    ```

## サンプルプログラム

[hello_ai.py](../../samples/langchain/hello_ai.py)を見てみましょう。このプログラムは、LangChainを使ってAIと簡単な会話をするプログラムです。

### プログラムの説明

1. まず、必要な道具（ライブラリ）を用意します：
```python
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
```

2. AIクライアントを準備します：
```python
chat = AzureChatOpenAI(
    openai_api_key="あなたのAPIキー",
    openai_api_version="2024-02-15-preview",
    azure_endpoint="あなたのエンドポイント",
    deployment_name="gpt-4o-mini"
)
```
※ `openai_api_key`と`azure_endpoint`は、自分のものに置き換えてください。

3. AIと会話します：
```python
messages = [
    HumanMessage(content="こんにちは！私の名前は田中です。")
]
```

4. AIの返事を受け取って表示します：
```python
response = chat(messages)
print("AI:", response.content)
```

## プログラムの実行方法

1. プログラムを実行する前に、以下の3つの情報を自分のものに書き換えてください：
   - `openai_api_key`：APIキー
   - `azure_endpoint`：エンドポイント
   - `deployment_name`：使用するモデル名（gpt-4o-mini）

2. コマンドプロンプトで以下のコマンドを実行します：
```bash
python hello_ai.py
```

## 用語解説

- **LangChain**：AIアプリケーションを簡単に作るためのツールです。
- **HumanMessage**：人間からAIへのメッセージを表すLangChainの機能です。
