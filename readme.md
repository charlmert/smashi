

## Building and Packaging

If you would like to fork this package and build your own based off it

```bash
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo python3 -m pip install tqdm
sudo python3 -m pip install --user --upgrade twine
```

To build

```bash
python3 setup.py bdist_wheel
```
