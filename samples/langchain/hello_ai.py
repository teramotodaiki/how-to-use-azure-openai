from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# AIクライアントを準備します
chat = AzureChatOpenAI(
    openai_api_key="あなたのAPIキー",  # ⚠️ 自分のAPIキーに置き換えてください
    openai_api_version="2024-02-15-preview",
    azure_endpoint="あなたのエンドポイント",  # ⚠️ 自分のエンドポイントに置き換えてください
    deployment_name="gpt-4o-mini",  # ⚠️ 自分の使えるモデル名に置き換えてください
)

# AIと会話します
messages = [
    HumanMessage(content="こんにちは！私の名前は田中です。")
]

# AIの返事を受け取ります
response = chat(messages)

# AIの返事を表示します
print("AI:", response.content)
