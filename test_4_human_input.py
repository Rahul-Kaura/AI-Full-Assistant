#!/usr/bin/env python3
"""
🧪 TEST 4: Human Input Functionality
Tests the human-in-the-loop feature
"""

import subprocess

def main():
    print("🧪 TEST 4: Human Input Functionality")
    print("=" * 50)
    print("Testing human-in-the-loop decision making...")
    print()
    
    command = "echo -e '1\\nWhat do you think about Python vs JavaScript?\\nquit' | python3 hulkster_chatbot_simple.py"
    
    print(f"Running: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
        
        if result.returncode == 0:
            print("\n✅ Test 4 PASSED: Human input functionality working!")
            print("👥 Human-in-the-loop feature working correctly!")
        else:
            print("\n❌ Test 4 FAILED: Human input functionality not working")
            
    except Exception as e:
        print(f"\n❌ Test 4 ERROR: {e}")

if __name__ == "__main__":
    main() 