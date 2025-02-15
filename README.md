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

## プログラムの準備

サンプルプログラムを動かすには、2つの大切な情報を環境変数として設定する必要があります。
環境変数は、プログラムに情報を教えてあげる方法の1つです。

ターミナル（黒い画面）で、以下のように入力してください：

```bash
# Windowsの場合
set AZURE_OPENAI_API_KEY=あなたのAPIキー
set AZURE_OPENAI_ENDPOINT=あなたのエンドポイント

# Macの場合
export AZURE_OPENAI_API_KEY=あなたのAPIキー
export AZURE_OPENAI_ENDPOINT=あなたのエンドポイント
```

⚠️ `あなたのAPIキー` と `あなたのエンドポイント` の部分は、自分の持っている値に置き換えてください。

## 注意事項

このガイドでは、Azure OpenAI の API エンドポイントと API キーを既に持っていることを前提としています。
