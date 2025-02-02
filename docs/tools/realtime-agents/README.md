# OpenAI Realtime Agents で Azure OpenAI を使う

このガイドでは、OpenAI Realtime Agents で Azure OpenAI を使う方法を説明します。

## Realtime Agents とは？

Realtime Agents は、OpenAI が作った新しい形の AI アプリの見本です。音声で AI と会話しながら、一緒にプログラミングができます。例えば、「新しいボタンを作って」と話しかけると、AI がすぐにプログラムを変更してくれます。

注意：これは実験的なデモアプリで、まだ開発中です。

## 必要なもの

1. Node.js（JavaScript を動かすためのソフト）
2. TypeScript（JavaScript を書きやすくするツール）
3. Next.js（ウェブサイトを作るためのツール）

## インストール方法

1. GitHub からプログラムをダウンロードします：

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

3. マイクボタンをクリックして、AI と話せます：
   - 「新しいボタンを作って」
   - 「背景の色を青に変えて」
   - 「文字を大きくして」

## 用語解説

- **デモ**：見本として作られたプログラムです
- **エージェント**：特定の仕事をする AI のことです
- **ローカルホスト**：自分のパソコンの中で動くウェブサイトです
- **音声認識**：声を文字に変える技術です
