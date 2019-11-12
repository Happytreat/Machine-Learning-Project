#### vgg16 model 

Feature extraction using vgg16 combined with linear regression. Acheived an average of 81% average accuracy in predicting artists of paintings. 

#### Running the model
```python
# Installing all the dependencies
env/bin/pip3 install -r requirements.txt
# alternatively (use --user flag to install directly on localhost)
pip3 install -r requirements.txt

# Download images dataset (1.5GB) (see credits) into root directory
# IMPORTANT: Download from https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5 and placed model weights inside vGG_16_model/.keras/models/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5

# Split images into test and train sets (2:8 ratio)
python3 split_test_train.py
split_folders input --ratio .7 0.2 .1 --output data

# Extract features using vGG16 model
python3 compile.py

# Use weights to run linear regression on test set
python3 train.py

# See clasification report in stdout
```

#### Credits
- Method inspired by https://www.pyimagesearch.com/2019/05/20/transfer-learning-with-keras-and-deep-learning/
- Images from https://www.kaggle.com/ikarus777/best-artworks-of-all-time/
- vGG16 model adapted from https://github.com/fchollet/deep-learning-models/blob/master/vgg16.py
