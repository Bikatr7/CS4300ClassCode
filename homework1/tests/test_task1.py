import subprocess

def test_hello_world_output():
    result = subprocess.run(['python', 'task1.py'], capture_output=True, text=True)
    
    assert result.stdout == "Hello, World!\n"
    assert result.stderr == ''
    assert result.returncode == 0 

    print("TASK 1 OK")