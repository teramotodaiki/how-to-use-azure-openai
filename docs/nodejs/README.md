# Node.jsでAzure OpenAIを使う

このガイドでは、Node.jsを使ってAzure OpenAIのAIと会話する方法を説明します。

## 必要なもの
- Node.js（バージョン14以上）
  - まだNode.jsをインストールしていない人は、[Node.jsの公式サイト](https://nodejs.org/)からダウンロードしてインストールしてください。
- openaiパッケージ
  - コマンドプロンプト（WindowsのPowerShellやMacのターミナル）で以下のコマンドを実行してインストールします：
    ```bash
    npm install @azure/openai
    ```

## サンプルプログラム

[hello_ai.js](../../samples/nodejs/hello_ai.js)を見てみましょう。このプログラムは、AIと簡単な会話をするプログラムです。

### プログラムの説明

1. まず、必要な道具（パッケージ）を用意します：
```javascript
const { OpenAIClient, AzureKeyCredential } = require("@azure/openai");
```

2. AIクライアントを準備します：
```javascript
const client = new OpenAIClient(
  "あなたのエンドポイント",
  new AzureKeyCredential("あなたのAPIキー")
);
```
※ エンドポイントとAPIキーは、自分のものに置き換えてください。

3. AIと会話する関数を作ります：
```javascript
async function chatWithAI() {
  const messages = [
    { role: "user", content: "こんにちは！私の名前は田中です。" }
  ];

  const result = await client.getChatCompletions(
    "gpt-4",
    messages
  );

  console.log("AI:", result.choices[0].message.content);
}
```
※ `gpt-4`は、自分が使えるモデル名に置き換えてください。

4. プログラムを実行します：
```javascript
chatWithAI().catch(console.error);
```

## プログラムの実行方法

1. プログラムを実行する前に、以下の3つの情報を自分のものに書き換えてください：
   - エンドポイント
   - APIキー
   - モデル名

2. コマンドプロンプトで以下のコマンドを実行します：
```bash
node hello_ai.js
```

## 会話を続ける方法

AIとの会話を続けたい場合は、`messages`配列に会話の履歴を追加していきます：

```javascript
const messages = [
  { role: "user", content: "こんにちは！私の名前は田中です。" },
  { role: "assistant", content: "こんにちは、田中さん！お会いできて嬉しいです。" },
  { role: "user", content: "好きな食べ物は何ですか？" }
];
```

## 用語解説

- **パッケージ**：プログラムを書くときに使える便利な道具箱のようなものです。
- **関数**：特定の作業をまとめた命令のかたまりです。
- **async/await**：非同期処理（時間がかかる作業）を扱うための特別な書き方です。
