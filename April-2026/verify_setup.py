#!/usr/bin/env python3
"""
Setup Verification Script
Run this to check if all dependencies are installed correctly.
"""

import sys

def check_import(module_name, package_name=None):
    """Check if a module can be imported."""
    try:
        __import__(module_name)
        print(f"✅ {package_name or module_name}")
        return True
    except ImportError:
        print(f"❌ {package_name or module_name} - Run: pip install {package_name or module_name}")
        return False

def main():
    print("🔍 Verifying Dependencies for April 2026 Challenges\n")
    
    all_good = True
    
    # Core dependencies
    print("📦 Core Dependencies:")
    all_good &= check_import("strands", "strands-agents")
    all_good &= check_import("strands.models.ollama", "strands-agents[ollama]")
    all_good &= check_import("strands_tools", "strands-agents-tools")
    
    # Memory
    print("\n🧠 Memory Dependencies:")
    all_good &= check_import("faiss", "faiss-cpu")
    
    # HTTP requests
    print("\n🌐 HTTP Dependencies:")
    all_good &= check_import("requests", "requests")
    
    # AWS
    print("\n☁️ AWS Dependencies:")
    all_good &= check_import("boto3", "boto3")
    
    # MCP
    print("\n🔌 MCP Dependencies:")
    all_good &= check_import("mcp", "mcp")
    
    # Summary
    print("\n" + "="*50)
    if all_good:
        print("✅ All dependencies installed correctly!")
        print("\n📋 Next Steps:")
        print("   1. For Challenge 1: Start Ollama with 'ollama serve'")
        print("   2. For Challenges 2-5: Configure AWS with 'aws configure'")
        print("   3. Run each challenge: cd challenge-X && python starter.py")
    else:
        print("❌ Some dependencies are missing.")
        print("\n🔧 Fix by running:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
