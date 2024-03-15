# conversations-formatter

ChatGPTからエクスポートした会話履歴をMarkdown形式に整形して出力する。

## 使い方

data/にChatGPTからエクスポートした会話履歴ファイル(conversations.json)を配置する。

以下のコマンドを実行するとoutputs/以下に.mdファイルが生成される。

```bash
$ rye sync
$ rye run apps/format.py
```

