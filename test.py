
from Core.GraphRAG import GraphRAG

import asyncio
if __name__ == "__main__":
    
    with open("./book.txt") as f:
        doc = f.read()
    graph_rag = GraphRAG(working_dir = "./results/hotpot")
    asyncio.run(graph_rag.insert([doc]))
    
    asyncio.run(graph_rag.query("Who is Scrooge?"))
   