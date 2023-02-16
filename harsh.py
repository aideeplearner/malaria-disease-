from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDRoundFlatButton
from tkinter import filedialog
from tkinter import *
import warnings
import os
import numpy as np
import numpy
import tensorflow as tf 
import cv2
from keras import layers
from kivy.uix.image import Image 

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")
from keras.models import load_model
model=load_model("malaria_mass.h5",compile=False)
classnames=["parasite","not parasite"]

class screen_manager(ScreenManager):
    pass

class app(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        Builder.load_file("load.kv")
        return screen_manager()

    def choose(self):
        root=Tk()
        root.title="siva"
        root.withdraw()
        self.root.filename=filedialog.askopenfilename(title="Select the image file ",filetypes=(("jpg files",".jpg"),("png files",".png ")))
        self.root.ids.img.source=self.root.filename
        return self.root.filename
    def pred(self):
        prediction=predict_malaria(self.root.filename)
        self.root.ids.result.text=prediction


        
def predict_malaria(img):
    image=cv2.imread(img)
    resize=tf.image.resize(image,(50,50))
    scale=np.expand_dims(resize/255,0)
    pred=model.predict(scale)
    if pred>0.5:
        result="DONT HAVE MALARIA"
    else:
        result="HAVE MALARIA"
    return result
 

app().run()