import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# 環境変数から大切な情報を取得します
api_key = os.getenv('AZURE_OPENAI_API_KEY')
endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

if not api_key or not endpoint:
    print("環境変数 AZURE_OPENAI_API_KEY と AZURE_OPENAI_ENDPOINT を設定してください")
    exit(1)

# AIクライアントを準備します
chat = AzureChatOpenAI(
    openai_api_key=api_key,
    openai_api_version="2024-02-15-preview",
    azure_endpoint=endpoint,
    deployment_name="gpt-4o-mini"
)

# AIと会話します
messages = [HumanMessage(content="こんにちは！私の名前は田中です。")]
response = chat(messages)
print("AI:", response.content)
