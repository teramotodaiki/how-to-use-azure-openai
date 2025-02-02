import OpenAI from 'openai';

const client = new OpenAI({
    apiKey: 'あなたのAPIキー',
    baseURL: 'あなたのエンドポイント',
    defaultQuery: { 'api-version': '2024-11-01-preview' },
    defaultHeaders: { 'api-key': 'あなたのAPIキー' }
});

// AIと会話する関数を作ります
async function chatWithAI() {
  const messages = [
    { role: "user", content: "こんにちは！私の名前は田中です。" }
  ];

  // AIと会話します
  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: messages
  });

  // AIの返事を表示します
  console.log("AI:", response.choices[0].message.content);
}

// プログラムを実行します
chatWithAI().catch(console.error);
