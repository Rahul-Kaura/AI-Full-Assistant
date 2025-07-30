#!/usr/bin/env python3
"""
🤖 HULKSTER AI ASSISTANT
Your personal AI companion with advanced capabilities!
Implements all 4 LangGraph lessons in one powerful assistant.
"""

import os
from dotenv import load_dotenv
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment variables
load_dotenv()

# Define the state
class HulksterState(TypedDict):
    messages: Annotated[list, add_messages]
    mode: str  # 'chat', 'search', 'human_input', 'multi_agent'
    debug_info: dict

def create_hulkster():
    """Create the Hulkster AI assistant."""
    
    # Initialize LLM
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-8b-8192",
        temperature=0.7
    )
    
    # Hulkster's personality
    hulkster_system = SystemMessage(content="""
    You are HULKSTER, an advanced AI assistant with multiple superpowers:
    
    🎯 PERSONALITY:
    - Confident, knowledgeable, and slightly witty
    - Expert in technology, AI, and problem-solving
    - Always ready to help and learn
    - Use emojis and casual language
    - Think of yourself as a tech-savvy friend
    
    🚀 CAPABILITIES:
    1. BASIC CHAT: Answer questions and have conversations
    2. WEB SEARCH: Simulate searching for current information
    3. HUMAN-IN-THE-LOOP: Ask for human input when needed
    4. MULTI-AGENT: Coordinate with specialized agents
    
    Always start responses with "🤖 Hulkster:" and be engaging!
    """)
    
    def hulkster_node(state: HulksterState) -> HulksterState:
        """Main Hulkster node that handles all capabilities."""
        
        user_message = state["messages"][-1].content.lower()
        state["debug_info"]["mode"] = "chat"
        
        # Check for search requests
        if any(word in user_message for word in ["search", "find", "latest", "current", "news"]):
            state["mode"] = "search"
            state["debug_info"]["mode"] = "search"
            
            # Simulate search results
            search_query = user_message.replace("search for", "").replace("find", "").strip()
            search_context = f"""
            I searched for '{search_query}' and found some interesting information:
            
            Based on my knowledge, here are some relevant points about {search_query}:
            - This is a rapidly evolving field with many exciting developments
            - There are several key trends and innovations worth noting
            - The technology continues to advance at an impressive pace
            
            Would you like me to elaborate on any specific aspect?
            """
            
            search_msg = SystemMessage(content=f"Search simulation: {search_context}")
            all_messages = [hulkster_system, search_msg] + state["messages"]
            response = llm.invoke(all_messages)
        
        # Check for human input requests
        elif any(word in user_message for word in ["what do you think", "your opinion", "should I", "help me decide"]):
            state["mode"] = "human_input"
            state["debug_info"]["mode"] = "human_input"
            response = AIMessage(content="""
🤖 Hulkster: Great question! I'd love to help you with this decision. To give you the best advice, I need a bit more context:

What specific aspects are you considering? For example:
- Are you looking for technical recommendations?
- Do you want pros and cons?
- Are you asking about best practices?
- Do you need step-by-step guidance?

Just let me know what you're most interested in, and I'll tailor my response accordingly! 😊
            """)
        
        # Check for complex tasks (multi-agent simulation)
        elif any(word in user_message for word in ["complex", "multiple", "debug", "troubleshoot", "creative"]):
            state["mode"] = "multi_agent"
            state["debug_info"]["mode"] = "multi_agent"
            
            # Simulate multi-agent coordination
            agents = []
            if "code" in user_message or "programming" in user_message:
                agents.append("Tech Expert")
            if "creative" in user_message or "ideas" in user_message:
                agents.append("Creative Assistant")
            if "debug" in user_message or "problem" in user_message:
                agents.append("Debugging Agent")
            
            agent_context = f"I'm coordinating with {len(agents)} specialized agents: {', '.join(agents)}"
            agent_msg = SystemMessage(content=f"Multi-agent context: {agent_context}")
            all_messages = [hulkster_system, agent_msg] + state["messages"]
            response = llm.invoke(all_messages)
        
        # Default chat mode
        else:
            state["mode"] = "chat"
            all_messages = [hulkster_system] + state["messages"]
            response = llm.invoke(all_messages)
        
        # Add response to state
        state["messages"].append(response)
        return state
    
    # Create the graph
    workflow = StateGraph(HulksterState)
    workflow.add_node("hulkster", hulkster_node)
    workflow.set_entry_point("hulkster")
    workflow.add_edge("hulkster", END)
    
    return workflow.compile()

def interactive_chat():
    """Run interactive chat with Hulkster."""
    print("🤖 HULKSTER AI ASSISTANT")
    print("=" * 60)
    print("🚀 Your advanced AI companion with multiple capabilities!")
    print()
    print("💡 Try these commands:")
    print("   • 'Search for latest AI news'")
    print("   • 'What do you think about Python?' (triggers human input)")
    print("   • 'Help me debug this code' (multi-agent)")
    print("   • 'Give me creative ideas' (multi-agent)")
    print("   • 'quit' to exit")
    print("=" * 60)
    print()
    
    try:
        hulkster = create_hulkster()
        print("✅ Hulkster is ready! Let's chat! 🚀")
        print()
        
        messages = []
        
        while True:
            user_input = input("👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("🤖 Hulkster: Thanks for chatting! I had a blast helping you out! 👋")
                break
            
            if not user_input:
                continue
            
            messages.append(HumanMessage(content=user_input))
            
            state = {
                "messages": messages,
                "mode": "chat",
                "debug_info": {}
            }
            
            try:
                result = hulkster.invoke(state)
                ai_message = result["messages"][-1]
                print(f"{ai_message.content}")
                print()
                
                # Show debug info
                if result.get("debug_info", {}).get("mode"):
                    mode = result["debug_info"]["mode"]
                    if mode != "chat":
                        print(f"🔍 Debug: Used {mode} mode")
                        print()
                
                messages = result["messages"]
                
            except Exception as e:
                print(f"❌ Error: {e}")
                print("🤖 Hulkster: Let me try a different approach! 🔧")
                print()
                
    except Exception as e:
        print(f"❌ Failed to create Hulkster: {e}")

def test_capabilities():
    """Test all of Hulkster's capabilities."""
    print("🧪 Testing Hulkster's Capabilities")
    print("=" * 50)
    
    try:
        hulkster = create_hulkster()
        
        test_cases = [
            "Hello! What can you help me with?",
            "Search for latest AI developments",
            "What do you think about Python vs JavaScript?",
            "Help me debug this code: print('Hello World'",
            "Give me creative ideas for a new project"
        ]
        
        for i, test_input in enumerate(test_cases, 1):
            print(f"\n🧪 Test {i}: {test_input}")
            print("-" * 40)
            
            messages = [HumanMessage(content=test_input)]
            state = {
                "messages": messages,
                "mode": "chat",
                "debug_info": {}
            }
            
            result = hulkster.invoke(state)
            ai_message = result["messages"][-1]
            print(f"🤖 Hulkster: {ai_message.content[:200]}...")
            
            if result.get("debug_info", {}).get("mode"):
                print(f"🔍 Mode: {result['debug_info']['mode']}")
            
            print()
            
    except Exception as e:
        print(f"❌ Test failed: {e}")

def main():
    """Main function."""
    print("🤖 HULKSTER AI ASSISTANT")
    print("=" * 50)
    print("1. Start interactive chat")
    print("2. Test all capabilities")
    print("3. Exit")
    print()
    
    choice = input("Choose an option (1-3): ").strip()
    
    if choice == "1":
        interactive_chat()
    elif choice == "2":
        test_capabilities()
    elif choice == "3":
        print("🤖 Hulkster: See you later! 👋")
    else:
        print("Invalid choice. Starting interactive chat...")
        interactive_chat()

if __name__ == "__main__":
    main() 