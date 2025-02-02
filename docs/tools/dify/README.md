# Dify で Azure OpenAI を使う

このガイドでは、Dify で Azure OpenAI を使って AI アプリを作る方法を説明します。

## Dify とは？

Dify は、プログラミングをあまり知らなくても、AI を使ったアプリを簡単に作れるツールです。チャットボットや、文章を要約するアプリ、質問に答えるアプリなどを作ることができます。

## Dify の使い方

### アカウントを作る

1. [Dify のウェブサイト](https://dify.ai)にアクセスします
2. 「Sign Up」（新規登録）をクリックします
3. メールアドレスとパスワードを入力して登録します

### Azure OpenAI と接続する

1. 左側のメニューから「Settings」（設定）をクリックします
2. 「Model Provider」（モデル設定）をクリックします
3. 「Add Provider」（プロバイダーを追加）をクリックします
4. 「Azure OpenAI」を選びます
5. 以下の情報を入力します：
   - API Key: 自分の Azure OpenAI API キー
   - API Base: 自分の Azure OpenAI エンドポイント
   - Model: 自分が使えるモデル名（例：gpt-4）

### AI アプリを作る

https://docs.dify.ai/ja-jp/guides/application-orchestrate/creating-an-application を見てください。

## 用語解説

- **チャットボット**：AI とおしゃべりができるプログラムです
- **API**：他のプログラムが AI を使うための通信方法です
- **エンドポイント**：AI がいる場所（サーバー）のアドレスです
- **プロバイダー**：AI のサービスを提供している会社のことです
