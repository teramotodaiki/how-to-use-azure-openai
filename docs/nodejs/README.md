# Node.js で Azure OpenAI を使う

このガイドでは、Node.js を使って Azure OpenAI の AI と会話する方法を説明します。

## 必要なもの

- Node.js（バージョン 14 以上）
  - まだ Node.js をインストールしていない人は、[Node.js の公式サイト](https://nodejs.org/)からダウンロードしてインストールしてください。
- openai パッケージ
  - コマンドプロンプト（Windows の PowerShell や Mac のターミナル）で以下のコマンドを実行してインストールします：
    ```bash
    npm install --save openai
    ```

## サンプルプログラム

[hello_ai.js](../../samples/nodejs/hello_ai.js)を見てみましょう。このプログラムは、AI と簡単な会話をするプログラムです。

## プログラムの実行方法

1. プログラムを実行する前に、以下の 3 つの情報を自分のものに書き換えてください：

   - エンドポイント
   - API キー
   - モデル名

2. コマンドプロンプトで以下のコマンドを実行します：

```bash
node hello_ai.js
```

## 会話を続ける方法

AI との会話を続けたい場合は、`messages`配列に会話の履歴を追加していきます：

```javascript
const messages = [
  { role: "user", content: "こんにちは！私の名前は田中です。" },
  {
    role: "assistant",
    content: "こんにちは、田中さん！お会いできて嬉しいです。",
  },
  { role: "user", content: "好きな食べ物は何ですか？" },
];
```

## 用語解説

- **パッケージ**：プログラムを書くときに使える便利な道具箱のようなものです。
- **関数**：特定の作業をまとめた命令のかたまりです。
- **async/await**：非同期処理（時間がかかる作業）を扱うための特別な書き方です。
