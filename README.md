# CapDec-Recreation
A recreation of the paper "CapDec: SOTA Zero Shot Image Captioning Using CLIP and GPT2" by David Nukrai, Ron Mokady and Amir Globerson. This recreation derives from [the official repo for the paper](https://github.com/DavidHuji/CapDec/tree/main).


## Training prereqs

Install dependencies using conda, as below : 
```
git clone https://github.com/DavidHuji/CapDec && cd CapDec
conda env create -f others/environment.yml
conda activate CapDec
```

### Dataset
1. Download either COCO, Flickr30k or Flickr8k, and place it in the ./data/ folder
2. Download the respective annotations using the link here : [COCO and Flickr30k annotations](https://www.kaggle.com/datasets/shtvkumar/karpathy-splits)
3. Parse the annotation to the correct format using the script parse_karpathy.py - just make sure to edit json paths inside the script.
4. _(Optional)_ If you need to subset the data, call the file subset_gen.py as follows on the commandline :
```
python subset_gen.py --input_file (dir. to input file) --output_dir (directory for output) --dividing_factor (integer factor by which you want to shrink data)
```

## Training 

1. Extract Clip Features using the following script (-h tag is for help, remove to execute) : 
`
python embeddings_generator.py -h
`
2. _(Option 1)_ : If running locally, train the model using the following script :
```
python train.py --data (path to clip embeddings from previous step.pkl) --out_dir (output_directory) --noise_variance (set variance, as defined in report - default is 0.016)
```
3. _(Option 2)_ : If training on Colab, copy clip features to colab, and use the notebook train_script.ipynb in Colab_notebooks\ . Edit paths to the embeddings within the cell before running using the command in option 1.\

For the above commandline call, you can add the tag -h for a help menu, showing a list of configurable hyperparameters for training.

## Evaluation 

#### Generating Captions

Once you have the .pt file from training, use predictions_runner.py as follows : 
```
python predictions_runner.py  --checkpoint path_to_checkpoints.pt --dataset_mode 0
```
The different inputs for dataset_mode can be found inside the file.

#### Getting Scores

After getting the captions json from last step, we can then use the colab notebook eval_code.ipynb inside Colab_notebooks\ . A cell will ask for a reference json file, which is the annotations from the dataset, and a captions file, which is the generated captions from last step. Once you have uploaded both of these, the notebook will parse the json files to the required format and generate the various metrics. 
