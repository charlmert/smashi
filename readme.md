# Smashi

<p align="center">
(Smashi = Beast from X-Men)[https://github.com/charlmert/smashi/raw/master/assets/beast.jpg]
</p>

Smashi is a python3 library with some useful utilities.

- cmd.py - Running commands from python
- copy.py - Copy recursively for e.g.
- file.py - Some file manipulation routines
- gui.py - Terminal whiptail gui for things like install scripts
- log.py - Some basic logging
- module.py - Load modules from script files
- net.py - Get your host ip, check internet
- password.py - Generate passwords
- proxmox.py - Provision proxmox lxc containers

## Howto install

Install via pip3 using this git repo

```bash
pip3 install git+ssh://git@github.com/charlmert/smashi.git@master#egg=smashi
```

## Howto use

```python
import smashi.cmd
smashi.cmd.output('ls -1')
# example output (0, 'assets\nbuild\ndist\nreadme.md\nsetup.py\nsmashi\nsmashi.egg-info\n', '')

You can also tail command output
smashi.cmd.tail('ls -1')
```

## Building and packaging

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
