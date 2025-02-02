from openai import AzureOpenAI

# AIクライアントを準備します
client = AzureOpenAI(
    api_key="あなたのAPIキー",  # ⚠️ 自分のAPIキーに置き換えてください
    api_version="2024-02-15-preview",
    azure_endpoint="あなたのエンドポイント"  # ⚠️ 自分のエンドポイントに置き換えてください
)

# AIと会話します
response = client.chat.completions.create(
    model="gpt-4",  # ⚠️ 自分の使えるモデル名に置き換えてください
    messages=[
        {"role": "user", "content": "こんにちは！私の名前は田中です。"}
    ]
)

# AIの返事を表示します
print("AI:", response.choices[0].message.content)
