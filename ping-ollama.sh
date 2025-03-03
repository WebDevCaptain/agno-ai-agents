# Ollama REST API

# curl http://localhost:11434/api/generate -d '{
#   "model": "deepseek-r1:8b",
#   "prompt":"Write a 10 line paragraph about the future of finance"
# }'


# curl http://localhost:11434/api/chat -d '{
#   "model": "deepseek-r1:8b",
#   "messages": [
#     { "role": "user", "content": "Write a 10 line paragraph about the future of finance" }
#   ]
# }'