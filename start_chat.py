#!/usr/bin/env python3
"""
💬 START CHAT - Normal Interactive Hulkster Chatbot
Simple script to start the normal chatbot without any testing
"""

import subprocess
import sys

def main():
    print("🤖 HULKSTER AI ASSISTANT")
    print("=" * 50)
    print("Starting normal interactive chatbot...")
    print("💡 Type 'quit' to exit")
    print("=" * 50)
    print()
    
    try:
        # Run the normal chatbot
        result = subprocess.run("python3 hulkster_chatbot_simple.py", shell=True)
        
        if result.returncode == 0:
            print("\n✅ Chat session ended successfully!")
        else:
            print("\n❌ Chat session ended with an error")
            
    except KeyboardInterrupt:
        print("\n\n🤖 Hulkster: Chat interrupted! See you later! 👋")
    except Exception as e:
        print(f"\n❌ Error starting chat: {e}")

if __name__ == "__main__":
    main() 