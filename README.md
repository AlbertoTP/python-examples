# Python Examples

Examples of python

* Proy 1 Calculator:
    * import re
    * re.sub()
    ```{r, engine='python', count_lines}
    num = re.sub(r'abc', '', input)              # Delete pattern abc
    num = re.sub(r'abc', 'def', input)           # Replace pattern abc -> def
    num = re.sub(r'\s+', '\s', input)            # Eliminate duplicate whitespaces
    num = re.sub(r'abc(def)ghi', '\1', input)    # Replace a string with a part of itself
    ```
    * eval()
