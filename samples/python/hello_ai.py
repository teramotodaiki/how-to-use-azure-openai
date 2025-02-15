import os
from openai import AzureOpenAI


def get_client():
    api_key = os.getenv('AZURE_OPENAI_API_KEY')
    endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

    if not api_key or not endpoint:
        raise ValueError(
            "環境変数 AZURE_OPENAI_API_KEY と AZURE_OPENAI_ENDPOINT が必要です")

    return AzureOpenAI(
        api_key=api_key,
        api_version="2024-02-15-preview",
        azure_endpoint=endpoint
    )


def chat_with_ai(message, client=None):
    if client is None:
        client = get_client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # AIクライアントを準備します
    client = get_client()
    # AIと会話します
    response_text = chat_with_ai("こんにちは！私の名前は田中です。", client)
    print("AI:", response_text)
