# 🤖 Hulkster AI Assistant

A custom AI assistant built with LangGraph that demonstrates all 4 LangGraph lessons:

1. **Basic Chatbot** - State management and LLM integration
2. **Human-in-the-Loop** - Interactive decision making
3. **Debugging with LangSmith** - Observability and monitoring
4. **Multi-Agent Systems** - Coordinated specialized agents

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Groq API key

### Installation

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Set up environment variables**
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

3. **Run the bot**
```bash
python3 chat.py
```

## 💬 Simple Commands

### **Just Start Chatting (Recommended)**
```bash
python3 chat.py
```
Start chatting with Hulkster immediately - no tests, no confusion!

### **Guided Testing**
```bash
python3 simple_guided_test.py
```
Walk through each test step by step with clear explanations.

### **Individual Test Commands**
```bash
# Test all 4 LangGraph lessons
python3 test_2_all_capabilities.py

# Test basic chat
python3 test_1_basic_chat.py

# Test search functionality
python3 test_3_search.py

# Test human input (human-in-the-loop)
python3 test_4_human_input.py

# Test multi-agent coordination
python3 test_5_multi_agent.py

# Run complete test suite
python3 run_all_tests.py
```

## 🧪 Testing Features

### **Guided Test Menu**
The guided test walks you through each feature:

1. **🧪 Test Basic Chat** - Say hello to Hulkster
2. **🔍 Test Search** - Ask for latest AI news
3. **👥 Test Human Input** - Ask for advice about Python vs JavaScript
4. **🐛 Test Debugging** - Give broken code to fix (missing parenthesis)
5. **🎨 Test Creative Ideas** - Ask for project ideas
6. **💬 Start Normal Chat** - Just chat normally
7. **🚀 Run All Tests** - Run everything in sequence

### **Example Test Commands**
- **Basic Chat**: `"Hello! What can you help me with?"`
- **Search**: `"Search for latest AI news"`
- **Human Input**: `"What do you think about Python vs JavaScript?"`
- **Debugging**: `"Help me debug this code: print('Hello World'"`
- **Creative Tasks**: `"Give me creative ideas for a new project"`

## 🎯 Features

- ✅ **Complete LangGraph Implementation** - All 4 lessons mastered
- ✅ **Real Web Search** - Live search using Tavily API
- ✅ **Human-in-the-Loop Integration** - Collaborative AI decision making
- ✅ **Multi-Agent Coordination** - Specialized agents working together
- ✅ **Debugging & Observability** - LangSmith tracing and monitoring
- ✅ **Smart Routing System** - Intelligent capability selection
- ✅ **Production-Ready Code** - Error handling and proper structure
- ✅ **Simple Commands** - Easy to use without confusion
- ✅ **Guided Testing** - Step-by-step explanations

## 🔑 Getting API Keys

### Groq API Key (Required)
1. Visit [Groq Console](https://console.groq.com/keys)
2. Sign up for a free account
3. Generate an API key
4. Add it to your `.env` file

### Tavily API Key (Required for Web Search)
1. Visit [Tavily](https://tavily.com/)
2. Sign up for a free account
3. Generate an API key
4. Add it to your `.env` file

### LangSmith API Key (Optional for Debugging)
1. Visit [LangSmith](https://smith.langchain.com/)
2. Sign up for a free account
3. Generate an API key
4. Add it to your `.env` file

### Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
```

## 📁 File Structure

```
CleanHulksterBot/
├── chat.py                    # Simple chat (recommended)
├── simple_guided_test.py      # Guided testing
├── hulkster_chatbot_simple.py # Main bot file
├── test_*.py                  # Individual test files
├── run_all_tests.py           # Complete test suite
├── requirements.txt           # Dependencies
├── README.md                  # This file
└── .env                       # API keys (create this)
```

## 🚀 Quick Commands

```bash
# Navigate to directory
cd /Users/hulkster/Pycharm/Agentic-LanggraphCrash-course/CleanHulksterBot

# Just start chatting (easiest)
python3 chat.py

# Guided testing
python3 simple_guided_test.py

# Test all capabilities
python3 test_2_all_capabilities.py
```

## 🎉 What's New

- **Simple Commands**: No more confusing test files
- **Guided Testing**: Step-by-step explanations
- **Clear Instructions**: Know exactly what each test does
- **Easy Chat**: Just run `python3 chat.py` to start chatting
- **All 4 LangGraph Lessons**: Still fully implemented

---

**🤖 Hulkster: Ready to help you with anything! Just run `python3 chat.py` to start! 💪**

*Built with ❤️ using LangGraph* 