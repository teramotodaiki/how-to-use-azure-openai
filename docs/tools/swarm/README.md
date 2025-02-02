# SwarmでAzure OpenAIを使う

このガイドでは、SwarmでAzure OpenAIを使う方法を説明します。

## Swarmとは？

Swarmは、OpenAIが開発した実験的な教育用フレームワークです。複数のAIエージェント（AIロボット）が協力して作業を進める方法を学ぶことができます。

注意：Swarmは実験的なツールで、まだ開発中です。本番環境での使用は想定されていません。

## Swarmのインストール方法

1. Python 3.10以上をインストールします（まだの人は[Pythonの公式サイト](https://www.python.org)からダウンロード）
2. コマンドプロンプト（WindowsのPowerShellやMacのターミナル）を開きます
3. 以下のコマンドを入力してSwarmをインストールします：
   ```bash
   pip install git+https://github.com/openai/swarm.git
   ```

## Azure OpenAIの設定方法

1. 新しいフォルダを作ります
2. その中に`config.py`というファイルを作り、以下の内容を書きます：
   ```python
   from openai import AzureOpenAI

   client = AzureOpenAI(
       api_key="自分のAPIキー",  
       api_version="2024-11-01-preview",
       azure_endpoint="自分のエンドポイント"
   )
   ```

## Swarmの使い方

### AIチームを作る
1. Pythonファイル（例：`my_team.py`）を作ります
2. 以下のようなコードを書きます：
   ```python
   from swarm import Swarm, Agent
   from config import client

   # AIエージェントを作ります
   agent_a = Agent(
       name="プログラマー",
       instructions="あなたはプログラムを書くAIです。",
       client=client
   )

   agent_b = Agent(
       name="レビュアー",
       instructions="あなたはプログラムをチェックするAIです。",
       client=client
   )

   # Swarmを作ってエージェントたちを登録します
   swarm = Swarm(client=client)
   swarm.add_agent(agent_a)
   swarm.add_agent(agent_b)

   # チームに仕事を依頼します
   response = swarm.run(
       agent=agent_a,  # 最初にプログラマーから始めます
       messages=[{"role": "user", "content": "簡単な電卓プログラムを作ってください"}]
   )

   print(response.messages[-1]["content"])  # AIの返事を表示します
   ```

### 結果を見る
1. プログラムを実行します：
   ```bash
   python my_team.py
   ```
2. AIたちが協力して作業をしている様子が表示されます
3. 作業が終わると、結果が表示されます

## 用語解説

- **エージェント**：特定の役割を持って働くAIのことです
- **フレームワーク**：プログラムを作るための道具箱のようなものです
- **実験的**：まだ開発中で、テスト段階という意味です
- **クライアント**：AIサービスと通信するためのプログラムです
