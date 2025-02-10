import subprocess
import sys
import os

def test_hello_world_output():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(test_dir, '..', 'task1.py')
    
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True, 
        text=True
    )
    
    assert result.stdout == "Hello, World!\n"
    assert result.stderr == ''
    assert result.returncode == 0

    print("TASK 1 OK")

if(__name__ == "__main__"):
    test_hello_world_output()