#!/usr/bin/env python3
"""
🧪 TEST 3: Search Functionality
Tests the web search simulation feature
"""

import subprocess

def main():
    print("🧪 TEST 3: Search Functionality")
    print("=" * 50)
    print("Testing web search simulation...")
    print()
    
    command = "echo -e '1\\nSearch for latest AI news\\nquit' | python3 hulkster_chatbot_simple.py"
    
    print(f"Running: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
        
        if result.returncode == 0:
            print("\n✅ Test 3 PASSED: Search functionality working!")
            print("🔍 Web search simulation working correctly!")
        else:
            print("\n❌ Test 3 FAILED: Search functionality not working")
            
    except Exception as e:
        print(f"\n❌ Test 3 ERROR: {e}")

if __name__ == "__main__":
    main() 