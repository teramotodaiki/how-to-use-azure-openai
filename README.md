# Azure OpenAI 入門ガイド

このリポジトリは、プログラミングを始めたばかりの小中高生向けに、Azure OpenAI の使い方をまとめた教材です。

## 目次

### プログラミング言語別ガイド

- [Python で始める Azure OpenAI](docs/python/README.md)
  - Python は初心者にもやさしいプログラミング言語です。たくさんの参考書やウェブサイトがあります。
- [Node.js で始める Azure OpenAI](docs/nodejs/README.md)
  - Node.js はウェブサイトを作るのによく使われる言語です。JavaScript という言語を使います

### 開発ツール別ガイド

- [Cursor で始める Azure OpenAI](docs/tools/cursor/README.md)
  - Cursor は、AI がプログラミングを手伝ってくれる特別なエディタです。コードを書くときに AI がアドバイスをくれます。
- [Roo Code で始める Azure OpenAI](docs/tools/roo-code/README.md)
  - Roo Code は VSCode（人気のコードエディタ）で使える拡張機能です。日本語で AI とおしゃべりしながらプログラミングができます。
- [Dify で始める Azure OpenAI](docs/tools/dify/README.md)
  - Dify は、プログラミングをあまり知らなくても、チャットボットなどの AI アプリを簡単に作れるツールです。

## モデルについて

Azure OpenAI で利用できるモデルの詳細な比較は[こちら](docs/models/README.md)をご覧ください。モデルによって得意な作業や料金が異なりますので、用途に合わせて選んでください。

## 用語解説

- **API**（エーピーアイ）: コンピュータープログラム同士が会話するための約束事です。Azure OpenAI の API を使うと、私たちのプログラムから AI と会話できるようになります。
- **エンドポイント**: API にアクセスするための住所のようなものです。
- **API キー**: API を使うための合言葉です。大切な情報なので、他の人に教えてはいけません。

## 環境変数の設定

サンプルコードを実行する前に、以下の環境変数を設定してください：

- `AZURE_OPENAI_API_KEY`: Azure OpenAI の API キー
- `AZURE_OPENAI_ENDPOINT`: Azure OpenAI のエンドポイント

これらの値は Azure ポータルで確認できます。

## 注意事項

このガイドでは、Azure OpenAI の API エンドポイントと API キーを既に持っていることを前提としています。
