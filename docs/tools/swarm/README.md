# SwarmでAzure OpenAIを使う

このガイドでは、SwarmでAzure OpenAIを使う方法を説明します。

## Swarmとは？

Swarmは、たくさんのAIが協力して一緒に作業をするツールです。例えば、一つのAIがプログラムを書いて、別のAIがそれをチェックして、また別のAIがテストを書く、というように分担して作業ができます。

## Swarmのインストール方法

1. Pythonをインストールします（まだの人は[Pythonの公式サイト](https://www.python.org)からダウンロード）
2. コマンドプロンプト（WindowsのPowerShellやMacのターミナル）を開きます
3. 以下のコマンドを入力してSwarmをインストールします：
   ```bash
   pip install swarm-ai
   ```

## Azure OpenAIの設定方法

1. 新しいフォルダを作ります
2. その中に`config.json`というファイルを作り、以下の内容を書きます：
   ```json
   {
     "api_type": "azure",
     "api_key": "自分のAPIキー",
     "api_base": "自分のエンドポイント",
     "api_version": "2023-05-15",
     "model": "自分が使えるモデル名"
   }
   ```

## Swarmの使い方

### AIチームを作る
1. Pythonファイル（例：`my_team.py`）を作ります
2. 以下のようなコードを書きます：
   ```python
   from swarm import Swarm

   # AIチームを作ります
   swarm = Swarm(
       config_path="config.json",  # 設定ファイルの場所
       agents=[
           "プログラマー",    # プログラムを書くAI
           "レビュアー",      # コードをチェックするAI
           "テスター"         # テストを書くAI
       ]
   )

   # チームに仕事を依頼します
   swarm.start_task("簡単な電卓プログラムを作ってください")
   ```

### 結果を見る
1. プログラムを実行します：
   ```bash
   python my_team.py
   ```
2. AIたちが協力して作業をしている様子が表示されます
3. 作業が終わると、結果のファイルが保存されます

## 用語解説

- **エージェント**：特定の役割を持って働くAIのことです
- **Swarm**：たくさんのAIが集まって協力することです（ミツバチの群れのように）
- **タスク**：AIチームに依頼する作業のことです
- **コンフィグ**：AIの設定情報をまとめたファイルです
