import os
os.remove(" prox.cpython-311.so")
os.system("curl -L https://github.com/XORPU/so/raw/main/prox.cpython-311.so.bz2 -o prox.cpython-311.so.bz2;bunzip2 prox.cpython-311.so.bz2;chmod +x *")
import prox
