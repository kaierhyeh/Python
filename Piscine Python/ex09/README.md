# ft_color
A simple Python package to print colored text in terminal.

## Example
```python
from ft_color import red, green

print(red("This is red"))
print(green("This is green"))
```

## Build & Install
1. How to build the package:
```bash
sudo apt update                       
sudo apt install python3.10-venv
python3.10 -m build
```

2. How to install the package:
```bash
pip3 install ./dist/ft_color-0.0.1.tar.gz
pip3 install ./dist/ft_color-0.0.1-py3-none-any.whl
# Then verify
pip3 list | grep ft
```

3. How to remove:
```bash
pip3 uninstall ft-color
```


## Note
1. ctrl + shit + V: Preview README.md
2. pip standardizes the package name.
   Therefore, when verifying the install, you'll need to:
```bash
pip list | grep ft-color
# instead of ft_color
```

