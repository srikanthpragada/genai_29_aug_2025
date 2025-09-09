import os
# Get key from OPENAI_KEY, which is environment variable in OS
OPENAIKEY = os.getenv("OPENAI_KEY")

if __name__ == '__main__':
    print(OPENAIKEY)

 