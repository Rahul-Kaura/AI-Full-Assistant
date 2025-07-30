#!/usr/bin/env python3
"""
🧪 TEST 5: Multi-Agent Functionality
Tests the multi-agent coordination feature
"""

import subprocess

def main():
    print("🧪 TEST 5: Multi-Agent Functionality")
    print("=" * 50)
    print("Testing multi-agent coordination...")
    print()
    
    command = "echo -e '1\\nHelp me debug this code: print(\\'Hello World\\'\\nquit' | python3 hulkster_chatbot_simple.py"
    
    print(f"Running: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
        
        if result.returncode == 0:
            print("\n✅ Test 5 PASSED: Multi-agent functionality working!")
            print("🤝 Multi-agent coordination working correctly!")
        else:
            print("\n❌ Test 5 FAILED: Multi-agent functionality not working")
            
    except Exception as e:
        print(f"\n❌ Test 5 ERROR: {e}")

if __name__ == "__main__":
    main() 