#!/usr/bin/env python3
"""
🧪 TEST 1: Basic Interactive Chat
Runs the interactive chat mode with a simple greeting
"""

import subprocess

def main():
    print("🧪 TEST 1: Basic Interactive Chat")
    print("=" * 50)
    print("Testing basic greeting functionality...")
    print()
    
    command = "echo -e '1\\nHello! What can you help me with?\\nquit' | python3 hulkster_chatbot_simple.py"
    
    print(f"Running: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
        
        if result.returncode == 0:
            print("\n✅ Test 1 PASSED: Basic chat working!")
        else:
            print("\n❌ Test 1 FAILED: Basic chat not working")
            
    except Exception as e:
        print(f"\n❌ Test 1 ERROR: {e}")

if __name__ == "__main__":
    main() 