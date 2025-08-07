#!/usr/bin/env python3
"""
Convenience script to run MCP client with optional weather server control
"""

import subprocess
import sys
import time
import signal
import os

def start_weather_server():
    """Start the weather server in background"""
    print("🌤️  Starting weather server...")
    try:
        # Start weather server in background
        process = subprocess.Popen(
            ["python", "servers/weather.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)  # Give it more time to start
        return process
    except Exception as e:
        print(f"❌ Failed to start weather server: {e}")
        return None

def stop_weather_server(process):
    """Stop the weather server"""
    if process:
        print("🌤️  Stopping weather server...")
        process.terminate()
        process.wait()

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python run_mcp.py math-only          # Run with math server only")
        print("  python run_mcp.py with-weather       # Run with both servers")
        print("  python run_mcp.py auto               # Auto-detect weather server")
        sys.exit(1)
    
    mode = sys.argv[1]
    weather_process = None
    
    try:
        if mode == "math-only":
            print("🧮 Running MCP client with math server only...")
            subprocess.run(["python", "clients/mcpclient.py"])
            
        elif mode == "with-weather":
            print("🌤️  Starting weather server...")
            weather_process = start_weather_server()
            if weather_process:
                print("🧮 Running MCP client with both servers...")
                subprocess.run(["python", "clients/mcpclient.py"])
            else:
                print("❌ Failed to start weather server, running math-only...")
                subprocess.run(["python", "clients/mcpclient.py"])
                
        elif mode == "auto":
            print("🤖 Auto-detecting available servers...")
            subprocess.run(["python", "clients/mcpclient.py"])
            
        else:
            print(f"❌ Unknown mode: {mode}")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user")
    finally:
        if weather_process:
            stop_weather_server(weather_process)

if __name__ == "__main__":
    main()
