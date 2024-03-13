# Chatgpt-Retrieval  V1
#### Simple script to use ChatGPT on your own files. See data folder for storage of the data you wish to query. 

# Installation

Please review all the dependencies required for functional runtime of the app. You will find them in the requirements.txt file

## Python Version 

Tool was built with python 3.11.7 and relevant modules defined in the requirements.txt file. 

## Other requirements 

### C++ Build Tools
Install  C++ Build Tools to handle possible issues with ChromaDB and wheels: Microsoft C++ Build Tools - Visual Studio 
https://visualstudio.microsoft.com/visual-cpp-build-tools/
Issue discussed here
https://github.com/chroma-core/chroma/issues/163 
Here
https://gist.github.com/ashmalvayani/ab3f4a8469fe3a2e9904c3a2674ea947
And here 
https://learn.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-14-0-or-greater-is-requir

### CMake
You may be encountering problems with installation of unstructured[pdf] to resolve this, you will need to assure correct
installation of the windows SDK C++ components (build tools) but also correct installation of CMake with correctly updated
system variables (Path) and a system restart to apply any changes in case or installation:

Install CMake https://cmake.org/download/

### Python Packages 
Install [Langchain](https://github.com/hwchase17/langchain) and other packages, see requirements.txt.

Navigate to project repository and install modules form requirements.txt file:

```
pip install -r requirements.txt
```
Or attempt doing manually as below, try adding package versions for compatability. 
```
pip install langchain langchain-openai langchain-community sentence-transformers tiktoken unstructured python-dotenv chromadb-client chromadb unstructured[pdf]
```

### Credentials for LLM
Modify or create a `.env` file in a project path to use your own [OpenAI API key](https://platform.openai.com/account/api-keys).

### Data 
Place your own data into `data/data.txt`. Application handles all structured or semi structured files currently, 
excluding images  with non system generated text. 

### Example usage

#### Authentication check 

Use `AuthTest.py` to verify correctness of authentication with OpenAI

#### RAG
Test reading `data/data.txt` file.
```
cd C:\User\Project Path
```
Run app with first prompt
```
> python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.
```

Test reading `data/cat.pdf` file.
```
> python chatgpt.py "what is my cat's name"
Your cat's name is Muffy.
```
#### Data Scrap
Use underlying python file to scrap data from any URL. 