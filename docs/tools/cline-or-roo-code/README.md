# Roo Code で Azure OpenAI を使う

このガイドでは、Roo Code で Azure OpenAI を使う方法を説明します。

## Roo Code とは？

Roo Code は、VSCode（プログラミングを書くためのソフト）の中で AI とおしゃべりしながらプログラミングができる便利なツールです。日本語で会話ができ、AI がプログラムを書いたり、エラーを直したり、質問に答えたりしてくれます。

## Roo Code のインストール方法

1. VSCode を開きます
2. 左側のパズルのピースみたいなマーク（拡張機能）をクリックします
3. 検索欄に「Roo Code」と入力します
4. 「Install」（インストール）ボタンをクリックします

## Azure OpenAI の設定方法

1. VSCode の中で Roo Code を開きます（左側のアイコンから）
2. 歯車マーク（⚙️）をクリックして設定を開きます
3. 以下の情報を入力します：
   - API Provider: OpenAI Compatible
   - Base URL:
     - https://eastus2.api.cognitive.microsoft.com/openai/deployments/gpt-4o/chat/completions?api-version=2025-01-01-preview または
     - https://swedencentral.api.cognitive.microsoft.com/openai/deployments/gpt-4o/chat/completions?api-version=2025-01-01-preview
   - OpenAI API Key: 自分の API キー
   - Model: gpt-4o または gpt-4o-mini
   - Use Azure: ✅️

## Roo Code の使い方

### AI とおしゃべりする

1. チャット画面を開きます
2. 日本語で質問や指示を入力します（例：「HTML でボタンの作り方を教えて」）
3. Enter キーを押すと、AI が答えてくれます

### プログラムを書いてもらう

1. やりたいことを日本語で説明します（例：「数当てゲームを作りたい」）
2. AI がプログラムを書いてくれます

### エラーを直してもらう

1. エラーが出ているコードを選びます
2. 右クリックして「Fix with Roo Code」を選びます
3. AI がエラーの原因と直し方を教えてくれます

### モード切り替え

Roo Code には 3 つの基本的なモードがあります：

1. Code（コード）モード：プログラムを書くときに使います
2. Architect（設計）モード：プログラムの設計を考えるときに使います
3. Ask（質問）モード：分からないことを質問するときに使います

モードは画面下のドロップダウンメニューから切り替えられます。

## 用語解説

- **VSCode**：プログラムを書くための無料のソフトです
- **拡張機能**：VSCode に新しい機能を追加するためのパーツです
- **API**：AI と話すための特別な通信方法です
- **モード**：AI の得意分野を切り替える機能です
