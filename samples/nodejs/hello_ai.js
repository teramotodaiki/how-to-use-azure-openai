import { AzureOpenAI } from "openai";

// 環境変数から大切な情報を取得します
const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
const apiKey = process.env.AZURE_OPENAI_API_KEY;

if (!endpoint || !apiKey) {
  console.error("環境変数 AZURE_OPENAI_API_KEY と AZURE_OPENAI_ENDPOINT を設定してください");
  process.exit(1);
}

// AIクライアントを準備します
const client = new AzureOpenAI({
  endpoint: endpoint,
  apiKey: apiKey,
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
