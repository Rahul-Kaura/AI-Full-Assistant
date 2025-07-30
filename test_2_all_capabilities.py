#!/usr/bin/env python3
"""
🧪 TEST 2: All Capabilities Test
Runs the automated test suite for all 4 LangGraph lessons
"""

import subprocess

def main():
    print("🧪 TEST 2: All Capabilities Test")
    print("=" * 50)
    print("Testing all 4 LangGraph lessons automatically...")
    print()
    
    command = "echo '2' | python3 hulkster_chatbot_simple.py"
    
    print(f"Running: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
        
        if result.returncode == 0:
            print("\n✅ Test 2 PASSED: All capabilities working!")
            print("🎯 All 4 LangGraph lessons tested successfully!")
        else:
            print("\n❌ Test 2 FAILED: Some capabilities not working")
            
    except Exception as e:
        print(f"\n❌ Test 2 ERROR: {e}")

if __name__ == "__main__":
    main() 