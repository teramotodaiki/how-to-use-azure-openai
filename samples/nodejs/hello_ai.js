import { AzureOpenAI } from "openai";

// AIクライアントを準備します
const client = new AzureOpenAI({
  endpoint: "あなたのエンドポイント", // ⚠️ 自分のエンドポイントに置き換えてください
  apiKey: "あなたのAPIキー", // ⚠️ 自分のAPIキーに置き換えてください
  deployment: "gpt-4o-mini",
  apiVersion: "2024-12-01-preview",
});

// AIと会話する関数を作ります
async function chatWithAI() {
  // AIと会話します
  const result = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: "何か面白いことを言ってください" }],
  });

  // AIの返事を表示します
  console.log("AI:", result.choices[0].message.content);
}

// プログラムを実行します
chatWithAI().catch(console.error);
