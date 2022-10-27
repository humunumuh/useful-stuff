## PYTORCH  
Follow this guide and it will install cuda and cudnn within the pytorch library (easy)  
https://pytorch.org/get-started/locally/  

Check everything worked:  
```
<import torch
print(torch.version.cuda) #Cuda must be compatible with the torch installation
print(torch.cuda.is_available()) #Should be True
print(torch.cuda.device_count()) #Should be 1
print(torch.cuda.current_device()) #Should be 0
```
Chech cudnn availability  
https://pytorch.org/docs/stable/backends.html#torch.backends.cudnn.version
print(torch.backends.cudnn.is_available()) # Should be True
print(torch.backends.cudnn.enabled) # Should be True
print(torch.backends.cudnn.version()) # Version number

## TENSORFLOW  
Use Anaconda, as TF is a nightmare to setup through PyPi
Follow any online guide for installing linux Anaconda, such as https://unixcop.com/how-to-install-anaconda-on-fedora-36/
In anaconda install tensorflow-gpu, which installs cuda and cudnn as dependencies

Check the installations has worked:  
import tensorflow as tf  
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU'))) # Should be 1  
If 1 is available, then this also confirms cuda and cudnn are working (https://stackoverflow.com/questions/48566505/how-can-i-check-if-keras-tensorflow-is-using-cudnn)  

A second, more detailed check can be performed with:  
tf.compat.v1.Session()
