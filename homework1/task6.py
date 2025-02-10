def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return len(content.split())

## counts the number of words in the file

def generate_test_functions():
    test_files = ['task6_read_me.txt']
    
    def test_template(filename):
        def test_func():
            assert count_words(filename) == 100
        return test_func
    
    for file in test_files:
        test_name = f'test_word_count_{file.replace(".", "_")}'
        globals()[test_name] = test_template(file)

generate_test_functions() 