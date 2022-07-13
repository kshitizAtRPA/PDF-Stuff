# README

## Split and Rotate PDF document using Python PYPDF2

### Requires

- [Python3](https://python.org/downloads)
- PyPDF2 
- Install PyPDF by running the following command in your terminal.

    ```
    pip install PyPDF2
    ```

### Usage

- Clone or download the repo. 
- Copy the PDF file you want to split or rotate into the cloned repo directory.
- Use your favorite terminal to execute the python file.
- For splitting pdf file into individual pages use split.py
    
    ```
    py split.py
    ```

- For rotating, make sure its a splitted file and use rotate.py
- You'll have to specify the angle in clockwise direction in which you want the file rotated. I've not put any validation or exception handling so use wisely.
    ```
    py rotate.py
    ```