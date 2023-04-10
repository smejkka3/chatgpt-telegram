# Basic bot for interacting with chatGPT

## To work locally
- install docker
- run

```bash
docker build --tag telegram_chat_gpt_bot .
docker run --env-file dev/.env -it telegram_chat_gpt_bot
```