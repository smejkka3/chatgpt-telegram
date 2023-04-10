# Basic bot for interacting with chatGPT

## To work locally
- create file called .env in your dev/ folder and put int your API keys for openai and telegram named BOT_TOKEN and GPT_TOKEN respectively
- install docker
- run

```bash
docker build --tag telegram_chat_gpt_bot .
docker run --env-file dev/.env -it telegram_chat_gpt_bot
```