# OpenAI Realtime AgentsでAzure OpenAIを使う

このガイドでは、OpenAI Realtime AgentsでAzure OpenAIを使う方法を説明します。

## Realtime Agentsとは？

Realtime Agentsは、AIとリアルタイム（すぐに）おしゃべりしながら一緒に作業ができるツールです。例えば、AIに「このボタンの色を青に変えて」と言うと、すぐにAIがプログラムを変更してくれます。

## Realtime Agentsのインストール方法

1. Pythonをインストールします（まだの人は[Pythonの公式サイト](https://www.python.org)からダウンロード）
2. コマンドプロンプト（WindowsのPowerShellやMacのターミナル）を開きます
3. 以下のコマンドを入力してインストールします：
   ```bash
   pip install openai-realtime-agents
   ```

## Azure OpenAIの設定方法

1. 新しいフォルダを作ります
2. その中に`.env`というファイルを作り、以下の内容を書きます：
   ```
   OPENAI_API_TYPE=azure
   OPENAI_API_KEY=自分のAPIキー
   OPENAI_API_BASE=自分のエンドポイント
   OPENAI_API_VERSION=2023-05-15
   OPENAI_MODEL=自分が使えるモデル名
   ```

## Realtime Agentsの使い方

### AIと一緒に作業を始める
1. Pythonファイル（例：`my_agent.py`）を作ります
2. 以下のようなコードを書きます：
   ```python
   from realtime_agents import Agent

   # AIエージェントを作ります
   agent = Agent(
       name="プログラミング助手",
       description="プログラミングを手伝ってくれるAI"
   )

   # AIと一緒に作業を始めます
   agent.start_session(
       task="簡単なゲームを作りたいです",
       language="日本語"  # 日本語で会話します
   )
   ```

### AIと会話する
1. プログラムを実行します：
   ```bash
   python my_agent.py
   ```
2. コンソールにメッセージを入力します（例：「じゃんけんゲームを作りたいです」）
3. AIがすぐに返事をして、プログラムを書いたり変更したりしてくれます

### AIに作業を頼む
以下のような作業をAIに頼むことができます：
- プログラムを書く（例：「ボタンを追加して」）
- プログラムを変更する（例：「文字を大きくして」）
- エラーを直す（例：「エラーの直し方を教えて」）
- 説明を聞く（例：「このコードの意味を教えて」）

## 用語解説

- **リアルタイム**：すぐに反応すること（待ち時間がほとんどない）です
- **エージェント**：特定の役割を持って働くAIのことです
- **セッション**：AIとの一連の会話のことです
- **コンソール**：コマンドを入力する画面のことです
