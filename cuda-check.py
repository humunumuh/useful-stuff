# INSTALL CUDA
# Install cuda for the venv:
# https://nvidia.github.io/cuda-python/install.html

# INSTALL PYTORCH
# Install compatible torch:
# https://pytorch.org/get-started/locally/

import torch

print(torch.version.cuda) #Cuda must be compatible with the torch installation
print(torch.cuda.is_available()) #Should be True
print(torch.cuda.device_count()) #Should be 1
print(torch.cuda.current_device()) #Should be 0

# INSTALL CUDNN (provides additional acceleration)
# https://pypi.org/project/nvidia-cudnn/
# pip install nvidia-pyindex
# pip install nvidia-cudnn

# Chech cudnn availability
# https://pytorch.org/docs/stable/backends.html#torch.backends.cudnn.version

print(torch.backends.cudnn.is_available())
print(torch.backends.cudnn.enabled)
print(torch.backends.cudnn.version())
