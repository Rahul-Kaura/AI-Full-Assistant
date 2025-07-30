#!/usr/bin/env python3
"""
🧪 Test Script for Hulkster's New Features
Tests Tavily search and LangSmith integration
"""

import os
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
from langsmith import Client

# Load environment variables
load_dotenv()

def test_tavily():
    """Test Tavily search functionality."""
    print("🔍 Testing Tavily Search...")
    
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        print("❌ TAVILY_API_KEY not found in .env file")
        return False
    
    try:
        search_tool = TavilySearchResults(
            api_key=tavily_key,
            max_results=3
        )
        
        # Test search
        results = search_tool.invoke({"query": "LangGraph tutorial"})
        
        if results:
            print(f"✅ Tavily search working! Found {len(results)} results")
            print(f"📰 First result: {results[0].get('title', 'No title')}")
            return True
        else:
            print("❌ Tavily search returned no results")
            return False
            
    except Exception as e:
        print(f"❌ Tavily search error: {e}")
        return False

def test_langsmith():
    """Test LangSmith integration."""
    print("🔧 Testing LangSmith...")
    
    langsmith_key = os.getenv("LANGSMITH_API_KEY")
    if not langsmith_key:
        print("⚠️  LANGSMITH_API_KEY not found (optional)")
        return True  # LangSmith is optional
    
    try:
        client = Client()
        print("✅ LangSmith client initialized successfully")
        return True
        
    except Exception as e:
        print(f"❌ LangSmith error: {e}")
        return False

def main():
    """Run all tests."""
    print("🤖 Testing Hulkster's New Features\n")
    
    # Test Tavily
    tavily_ok = test_tavily()
    
    # Test LangSmith
    langsmith_ok = test_langsmith()
    
    print("\n📊 Test Results:")
    print(f"Tavily Search: {'✅ Working' if tavily_ok else '❌ Failed'}")
    print(f"LangSmith: {'✅ Working' if langsmith_ok else '❌ Failed'}")
    
    if tavily_ok:
        print("\n🎉 Your Hulkster bot now has real web search capabilities!")
    if langsmith_ok:
        print("🎉 Your Hulkster bot now has debugging and tracing!")
    
    print("\n🚀 Ready to run: python3 hulkster_chatbot.py")

if __name__ == "__main__":
    main() 