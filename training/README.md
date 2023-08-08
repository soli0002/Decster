# Training


There is a ready-trained model to use (`trained_model.pkl`), or you can train your own model.


# Generating your own model
The first script to run is `generate_data_with_spaces.py`, and then `generate_data_without_spaces.py`.
This is because `generate_data_without_spaces.py` is set to append to the training file by default, and running `generate_data_with_spaces.py` after it will result in overwriting the original data written by the other script


Next, you can either run `train.py` on your own computer or use the `.ipynb` notebook to run it in the cloud and get a link to download the generated file locally.
The final model file should be around 80-100mb.
