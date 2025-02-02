# OpenAI Realtime AgentsでAzure OpenAIを使う

このガイドでは、OpenAI Realtime AgentsでAzure OpenAIを使う方法を説明します。

## Realtime Agentsとは？

Realtime Agentsは、OpenAIが作った新しい形のAIアプリの見本です。音声でAIと会話しながら、一緒にプログラミングができます。例えば、「新しいボタンを作って」と話しかけると、AIがすぐにプログラムを変更してくれます。

注意：これは実験的なデモアプリで、まだ開発中です。

## 必要なもの

1. Node.js（JavaScriptを動かすためのソフト）
2. TypeScript（JavaScriptを書きやすくするツール）
3. Next.js（ウェブサイトを作るためのツール）

## インストール方法

1. GitHubからプログラムをダウンロードします：
   ```bash
   git clone https://github.com/openai/openai-realtime-agents.git
   cd openai-realtime-agents
   ```

2. 必要なプログラムをインストールします：
   ```bash
   npm install
   ```

## 設定方法

1. `.env.local`というファイルを作って、以下の内容を書きます：
   ```
   AZURE_OPENAI_API_KEY=自分のAPIキー
   AZURE_OPENAI_ENDPOINT=自分のエンドポイント
   AZURE_OPENAI_API_VERSION=2024-11-01-preview
   AZURE_OPENAI_MODEL=gpt-4o-mini
   ```

## 使い方

1. プログラムを起動します：
   ```bash
   npm run dev
   ```

2. ブラウザで `http://localhost:3000` を開きます

3. マイクボタンをクリックして、AIと話せます：
   - 「新しいボタンを作って」
   - 「背景の色を青に変えて」
   - 「文字を大きくして」

## どうやって動いているの？

1. **音声認識**：
   あなたの声を文字に変えます（「こんにちは」→テキスト）

2. **AIエージェント**：
   - プログラマー：コードを書くAI
   - デザイナー：見た目を整えるAI
   - レビュアー：チェックするAI

3. **リアルタイム応答**：
   AIがすぐに返事をして、画面が変わります

## 用語解説

- **デモ**：見本として作られたプログラムです
- **エージェント**：特定の仕事をするAIのことです
- **ローカルホスト**：自分のパソコンの中で動くウェブサイトです
- **音声認識**：声を文字に変える技術です
