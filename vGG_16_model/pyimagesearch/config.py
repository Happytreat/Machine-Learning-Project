# import the necessary packages
import os

# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "data"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "data"

# define the names of the training, testing, and validation
# directories
TRAIN = "train"
TEST = "test"
VAL = "val"

# initialize the list of class label names
# CLASSES = ['Vincent_van_Gogh', 'Edgar_Degas', 'Pablo_Picasso', 'Pierre-Auguste_Renoir', 'Albrecht_Dürer', 'Paul_Gauguin',
#             'Francisco_Goya', 'Rembrandt', 'Alfred_Sisley', 'Titian', 'Marc_Chagall']

CLASSES = ['Leonardo_da_Vinci', 'Jackson_Pollock', 'Albrecht_Dürer', 'Diego_Velazquez', 'Camille_Pissarro', 'El_Greco', 'Gustav_Klimt', 'Georges_Seurat', 'Giotto_di_Bondone', 'Marc_Chagall', 'Pieter_Bruegel', 'Frida_Kahlo', 'Jan_van_Eyck', 'Edgar_Degas', 'Michelangelo', 'Henri_de_Toulouse-Lautrec', 'Pierre-Auguste_Renoir', 'Henri_Matisse', 'Piet_Mondrian', 'Titian', 'Andrei_Rublev', 'Edouard_Manet', 'Edvard_Munch', 'Paul_Klee', 'Amedeo_Modigliani', 'Alfred_Sisley', 'Andy_Warhol', 'Gustave_Courbet', 'Paul_Gauguin', 'Claude_Monet', 'Mikhail_Vrubel', 'Francisco_Goya', 'William_Turner', 'Salvador_Dali', 'Pablo_Picasso', 'Peter_Paul_Rubens', 'Joan_Miro', 'Eugene_Delacroix', 'Kazimir_Malevich', 'Vasiliy_Kandinskiy', 'Paul_Cezanne', 'Raphael', 'Diego_Rivera', 'Rene_Magritte', 'Hieronymus_Bosch', 'Caravaggio', 'Rembrandt', 'Sandro_Botticelli', 'Henri_Rousseau', 'Vincent_van_Gogh']

# set the batch size
BATCH_SIZE = 32

# initialize the label encoder file path and the output directory to
# where the extracted features (in CSV file format) will be stored
LE_PATH = os.path.sep.join(["output", "le.cpickle"])
BASE_CSV_PATH = "output"

# set the path to the serialized model after training
MODEL_PATH = os.path.sep.join(["output", "model.cpickle"])
