#Fully functional chatbot with RAG vector search of set local directory.
##llama 3 for llm, huggingface transformer/aws titan text embedding v2 for embedding




Directions to run:
For embedding_function.py, choose either AWS Bedrock or Huggingface. If using AWS Bedrock, first pip install awscli and run aws configure to set up AWS CLI.

To run llama3 locally
Download Ollama: https://ollama.com/
Run in terminal: ollama run llama3
Feel free to change the model in query_data.py, simply run the model in terminal for ollama (ex. for mistral: ollama run mistral)

Start flask server by running app.py, then cd rag_frontend and npm start.
