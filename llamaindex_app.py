from llama_index.embeddings.gemini import GeminiEmbedding  
from llama_index.llms.gemini import Gemini  
from llama_index.core import Settings,SimpleDirectoryReader,VectorStoreIndex,StorageContext,load_index_from_storage,SummaryIndex  
from llama_index.core.node_parser import SentenceSplitter  
import os  
from dotenv import load_dotenv
from llama_index.core import ServiceContext
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import RouterQueryEngine
# Load environment variables
load_dotenv()

# Set up your Google API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
 
gemini_embedding_model=GeminiEmbedding(model_name="models/embedding-001")  
llm=Gemini()  
Settings.llm=llm  
Settings.embed_model=gemini_embedding_model  
Settings.node_parser = SentenceSplitter(chunk_size=1000, chunk_overlap=100)
Settings.num_output = 1000
Settings.context_window = 3900

reader = SimpleDirectoryReader(input_dir="./data")
documents = reader.load_data()

vector_index = VectorStoreIndex.from_documents(documents)


summary_index = SummaryIndex.from_documents(documents)


vector_tool = QueryEngineTool(
    vector_index.as_query_engine(),
    metadata=ToolMetadata(
        name="vector_search",
        description="Useful for searching for specific facts."
    )
)

summary_tool = QueryEngineTool(
    summary_index.as_query_engine(response_mode="tree_summarize"),
    metadata=ToolMetadata(
        name="summary",
        description="Useful for summarizing an entire document."
    )
)



query_engine = RouterQueryEngine.from_defaults(
    [vector_tool, summary_tool],
    select_multi=True,
)

#Results = query_engine.query(Question)
strInput=""  
while strInput!="exit":  
   if strInput!="":  
     response=query_engine.query(strInput)  
     print(response)  
   strInput=input("Ask the question: ")  
