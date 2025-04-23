from langgraph.graph import StateGraph, START, END
from state import State

graph_builder = StateGraph(State)

def my_first_node(state: State):
    messages = state.get("messages", [])

    new_message = "Hello, world!"
    
    return {
        "messages": messages + [new_message]
    }

graph_builder.add_node(my_first_node)

graph_builder.add_edge(START, "my_first_node")
graph_builder.add_edge("my_first_node", END)

graph = graph_builder.compile()