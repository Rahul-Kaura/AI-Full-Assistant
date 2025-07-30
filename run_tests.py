#!/usr/bin/env python3
"""
🚀 HULKSTER BOT - TEST RUNNER
Choose from numbered options to test different features
"""

import subprocess
import sys
import os

def run_test(test_number):
    """Run a specific test by number."""
    tests = {
        1: "test_1_basic_chat.py",
        2: "test_2_all_capabilities.py", 
        3: "test_3_search.py",
        4: "test_4_human_input.py",
        5: "test_5_multi_agent.py",
        6: "run_all_tests.py"
    }
    
    if test_number not in tests:
        print(f"❌ Invalid test number: {test_number}")
        return False
    
    test_file = tests[test_number]
    
    if not os.path.exists(test_file):
        print(f"❌ Test file not found: {test_file}")
        return False
    
    print(f"🚀 Running Test {test_number}: {test_file}")
    print("=" * 60)
    
    try:
        result = subprocess.run(f"python3 {test_file}", shell=True, timeout=60)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("❌ Test timed out after 60 seconds")
        return False
    except Exception as e:
        print(f"❌ Error running test: {e}")
        return False

def main():
    """Main function with numbered menu."""
    print("🤖 HULKSTER BOT - TEST RUNNER")
    print("=" * 60)
    print("Choose a test option:")
    print()
    print("1. 🧪 Test Basic Chat")
    print("2. 🎯 Test All Capabilities (4 LangGraph Lessons)")
    print("3. 🔍 Test Search Functionality")
    print("4. 👥 Test Human Input (Human-in-the-Loop)")
    print("5. 🤝 Test Multi-Agent Coordination")
    print("6. 🚀 Run ALL Tests (Complete Test Suite)")
    print("0. ❌ Exit")
    print()
    
    while True:
        try:
            choice = input("Enter test number (0-6): ").strip()
            
            if choice == "0":
                print("🤖 Hulkster: Thanks for testing! See you later! 👋")
                break
            
            if choice.isdigit():
                test_number = int(choice)
                if 1 <= test_number <= 6:
                    success = run_test(test_number)
                    if success:
                        print(f"\n✅ Test {test_number} completed successfully!")
                    else:
                        print(f"\n❌ Test {test_number} failed!")
                    
                    print("\n" + "="*60)
                    print("Choose another test or enter 0 to exit:")
                else:
                    print("❌ Please enter a number between 0 and 6")
            else:
                print("❌ Please enter a valid number")
                
        except KeyboardInterrupt:
            print("\n\n🤖 Hulkster: Interrupted! See you later! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 