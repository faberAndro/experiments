import pathlib

"""
DRIVE_DIR is the folder where you'd like to store the model result. If you run this script on Google Colab,
    be sure to provide a relative path for "DRIVE_DIR", as in the sample values here below.
LOG_FILE is the csv file name where you will be able to see the model results
CHECKPOINT_FILE is the name of the file that will store a checkpoint of the computations
    you'll have a checkpoint

"""

DRIVE_DIR = "/content/drive/My Drive/Colab_files/happiness/"
LOG_FILE = "model_history_log.csv"
CHECKPOINT_FILE = "training_2/cp-{epoch:02d}.ckpt"

WORKING_DIR = pathlib.Path(__file__).parent.resolve()
CONFIG_FILE = WORKING_DIR / 'config.json'
SAVED_RNN_DIR = WORKING_DIR / 'saved_RNN_runs'
LOCAL_CHECKPOINT_FILENAME = 'cp-{epoch:04d}.ckpt'
LOG_FILENAME = LOG_FILE
CHECKPOINT_SUBFOLDER = 'checkpoints'
