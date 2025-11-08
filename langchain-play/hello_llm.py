from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")  # or "gpt-4-turbo" if you prefer
response = llm.invoke("Say hello from LangChain.")
print(response.content)