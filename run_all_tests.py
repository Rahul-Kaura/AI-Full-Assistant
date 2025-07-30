#!/usr/bin/env python3
"""
🚀 HULKSTER BOT - AUTOMATED TEST RUNNER
Runs all test options automatically without manual input
"""

import subprocess
import sys
import time

def run_command(command, description):
    """Run a command and display results."""
    print(f"\n{'='*60}")
    print(f"🧪 {description}")
    print(f"{'='*60}")
    print(f"Command: {command}")
    print("-" * 60)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("❌ Command timed out after 30 seconds")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all test options."""
    print("🤖 HULKSTER BOT - AUTOMATED TEST RUNNER")
    print("=" * 60)
    print("This script will automatically run all test options!")
    print("=" * 60)
    
    # Change to the correct directory
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    tests = [
        {
            "command": "echo '2' | python3 hulkster_chatbot_simple.py",
            "description": "TEST ALL CAPABILITIES - Option 2"
        },
        {
            "command": "echo -e '1\\nHello! What can you help me with?\\nquit' | python3 hulkster_chatbot_simple.py",
            "description": "INTERACTIVE CHAT - Basic greeting test"
        },
        {
            "command": "echo -e '1\\nSearch for latest AI news\\nquit' | python3 hulkster_chatbot_simple.py",
            "description": "INTERACTIVE CHAT - Search functionality test"
        },
        {
            "command": "echo -e '1\\nWhat do you think about Python vs JavaScript?\\nquit' | python3 hulkster_chatbot_simple.py",
            "description": "INTERACTIVE CHAT - Human input test"
        },
        {
            "command": "echo -e '1\\nHelp me debug this code: print(\\'Hello World\\'\\nquit' | python3 hulkster_chatbot_simple.py",
            "description": "INTERACTIVE CHAT - Multi-agent debugging test"
        },
        {
            "command": "echo -e '1\\nGive me creative ideas for a new project\\nquit' | python3 hulkster_chatbot_simple.py",
            "description": "INTERACTIVE CHAT - Multi-agent creative test"
        },
        {
            "command": "echo -e '1\\nHello\\nSearch for latest AI news\\nWhat do you think about Python?\\nHelp me debug this code\\nGive me creative ideas\\nquit' | python3 hulkster_chatbot_simple.py",
            "description": "FULL CONVERSATION TEST - All features in one chat"
        }
    ]
    
    results = []
    
    for i, test in enumerate(tests, 1):
        print(f"\n🔄 Running Test {i}/{len(tests)}...")
        success = run_command(test["command"], test["description"])
        results.append(success)
        
        if i < len(tests):
            print("\n⏳ Waiting 2 seconds before next test...")
            time.sleep(2)
    
    # Summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print(f"{'='*60}")
    
    for i, (test, success) in enumerate(zip(tests, results), 1):
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"Test {i}: {status} - {test['description']}")
    
    passed = sum(results)
    total = len(results)
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Your Hulkster bot is working perfectly!")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    print(f"\n{'='*60}")
    print("🤖 HULKSTER: Thanks for testing! Ready to help you with anything! 💪")
    print(f"{'='*60}")

if __name__ == "__main__":
    main() 