const { OpenAIClient, AzureKeyCredential } = require("@azure/openai");

// AIクライアントを準備します
const client = new OpenAIClient(
  "あなたのエンドポイント",  // ⚠️ 自分のエンドポイントに置き換えてください
  new AzureKeyCredential("あなたのAPIキー")  // ⚠️ 自分のAPIキーに置き換えてください
);

// AIと会話する関数を作ります
async function chatWithAI() {
  const messages = [
    { role: "user", content: "こんにちは！私の名前は田中です。" }
  ];

  // AIと会話します
  const result = await client.getChatCompletions(
    "gpt-4",  // ⚠️ 自分の使えるモデル名に置き換えてください
    messages
  );

  // AIの返事を表示します
  console.log("AI:", result.choices[0].message.content);
}

// プログラムを実行します
chatWithAI().catch(console.error);
