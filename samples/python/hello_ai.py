import os
from openai import AzureOpenAI

# 環境変数から大切な情報を取得します
api_key = os.getenv('AZURE_OPENAI_API_KEY')
endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

if not api_key or not endpoint:
    print("環境変数 AZURE_OPENAI_API_KEY と AZURE_OPENAI_ENDPOINT を設定してください")
    exit(1)

# AIクライアントを準備します
client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-02-15-preview",
    azure_endpoint=endpoint
)

# AIと会話します
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "こんにちは！私の名前は田中です。"}
    ]
)

# AIの返事を表示します
print("AI:", response.choices[0].message.content)
