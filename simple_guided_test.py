#!/usr/bin/env python3
"""
🤖 HULKSTER BOT - SIMPLE GUIDED TEST
Walks you through each test step by step with clear instructions
"""

import subprocess
import sys
import time

def run_basic_chat():
    """Test 1: Basic Chat"""
    print("\n🧪 TEST 1: Basic Chat")
    print("=" * 50)
    print("Let's test basic conversation!")
    print("I'll ask you to say hello to Hulkster.")
    print()
    
    input("Press Enter when ready to start...")
    
    command = "echo -e '1\\nHello! What can you help me with?\\nquit' | python3 hulkster_chatbot_simple.py"
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        print("✅ Basic chat test completed!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_search_test():
    """Test 2: Search Functionality"""
    print("\n🔍 TEST 2: Search Functionality")
    print("=" * 50)
    print("Let's test web search!")
    print("I'll ask Hulkster to search for latest AI news.")
    print()
    
    input("Press Enter when ready to start...")
    
    command = "echo -e '1\\nSearch for latest AI news\\nquit' | python3 hulkster_chatbot_simple.py"
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        print("✅ Search test completed!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_human_input_test():
    """Test 3: Human Input (Human-in-the-Loop)"""
    print("\n👥 TEST 3: Human Input (Human-in-the-Loop)")
    print("=" * 50)
    print("Let's test human-in-the-loop decision making!")
    print("I'll ask Hulkster for advice about Python vs JavaScript.")
    print()
    
    input("Press Enter when ready to start...")
    
    command = "echo -e '1\\nWhat do you think about Python vs JavaScript?\\nquit' | python3 hulkster_chatbot_simple.py"
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        print("✅ Human input test completed!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_debugging_test():
    """Test 4: Debugging (Multi-Agent)"""
    print("\n🐛 TEST 4: Debugging (Multi-Agent)")
    print("=" * 50)
    print("Let's test debugging capabilities!")
    print("I'll give Hulkster broken code to fix.")
    print("Code: print('Hello World'  (missing closing parenthesis)")
    print()
    
    input("Press Enter when ready to start...")
    
    command = "echo -e '1\\nHelp me debug this code: print(\\'Hello World\\'\\nquit' | python3 hulkster_chatbot_simple.py"
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        print("✅ Debugging test completed!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_creative_test():
    """Test 5: Creative Ideas (Multi-Agent)"""
    print("\n🎨 TEST 5: Creative Ideas (Multi-Agent)")
    print("=" * 50)
    print("Let's test creative multi-agent coordination!")
    print("I'll ask Hulkster for creative project ideas.")
    print()
    
    input("Press Enter when ready to start...")
    
    command = "echo -e '1\\nGive me creative ideas for a new project\\nquit' | python3 hulkster_chatbot_simple.py"
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        print("✅ Creative test completed!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def start_interactive_chat():
    """Start normal interactive chat"""
    print("\n💬 INTERACTIVE CHAT")
    print("=" * 50)
    print("Starting normal Hulkster chatbot!")
    print("You can chat normally with Hulkster.")
    print("Type 'quit' to exit.")
    print()
    
    input("Press Enter to start chatting...")
    
    try:
        result = subprocess.run("python3 hulkster_chatbot_simple.py", shell=True)
        print("✅ Chat session ended!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main guided test function"""
    print("🤖 HULKSTER BOT - SIMPLE GUIDED TEST")
    print("=" * 60)
    print("I'll walk you through each test step by step!")
    print("Just press Enter when you're ready for each test.")
    print("=" * 60)
    
    while True:
        print("\nChoose what you want to do:")
        print("1. 🧪 Test Basic Chat")
        print("2. 🔍 Test Search Functionality")
        print("3. 👥 Test Human Input (Human-in-the-Loop)")
        print("4. 🐛 Test Debugging (Multi-Agent)")
        print("5. 🎨 Test Creative Ideas (Multi-Agent)")
        print("6. 💬 Start Normal Interactive Chat")
        print("7. 🚀 Run All Tests in Sequence")
        print("0. ❌ Exit")
        print()
        
        choice = input("Enter your choice (0-7): ").strip()
        
        if choice == "0":
            print("🤖 Hulkster: Thanks for testing! See you later! 👋")
            break
        elif choice == "1":
            run_basic_chat()
        elif choice == "2":
            run_search_test()
        elif choice == "3":
            run_human_input_test()
        elif choice == "4":
            run_debugging_test()
        elif choice == "5":
            run_creative_test()
        elif choice == "6":
            start_interactive_chat()
        elif choice == "7":
            print("\n🚀 Running all tests in sequence...")
            print("=" * 60)
            tests = [run_basic_chat, run_search_test, run_human_input_test, run_debugging_test, run_creative_test]
            for i, test in enumerate(tests, 1):
                print(f"\n🔄 Running test {i}/{len(tests)}...")
                test()
                if i < len(tests):
                    print("\n⏳ Waiting 3 seconds before next test...")
                    time.sleep(3)
            print("\n🎉 All tests completed!")
        else:
            print("❌ Please enter a number between 0 and 7")

if __name__ == "__main__":
    main() 