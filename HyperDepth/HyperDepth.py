import cv2
from cv2 import xfeatures2d_SIFT
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

import utilities as utils
import evaluations as evals
import PatchMatch as pm
import subpixel as sp

def get_dataset():
    images = glob.glob("C:/Users/Zoe/Documents/Thesis/CTD Data Test/**/ambient0_0.npy")
    disps = glob.glob("C:/Users/Zoe/Documents/Thesis/CTD Data Test/**/disp0_0.npy")
    images_all = [] 
    disps_all = []
    
    # make ndarrays of images, disps

    for i in images:
        #print(i)
        im = np.load(i)
        im = np.transpose(im, (1, 2, 0))
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        images_all.append(im_gray)

    for d in disps:
        disp = np.load(d)
        disps_all.append(disp)


    images_all = np.asarray(images_all)
    disps_all = np.asarray(disps_all)
    #reshape if necessary?
    X_train, X_test, y_train, y_test = train_test_split(images_all, disps_all, test_size = 0.33, random_state = 1234)

  #  print("done loading")

   # print(X_train.shape)
    #print(X_train[1])
   # test1 = X_train[10]
   # print(test1.shape)
    #test2 = (y_train[10])
    #print(test2.shape)
    #test1 = np.transpose(test1, (1, 2, 0))

   # plt.show()

    return X_train, X_test, y_train, y_test


def get_model(num_trees, forest_depth):

    rf = RandomForestClassifier(n_estimators = num_trees, max_features = 1, max_depth = forest_depth, criterion = 'entropy', 
                                        random_state = 1234, verbose = 0, n_jobs = 2)
    return rf


def eval_model():

    return

def signal_check():

    return

def prob_check():
    return

def winner_check():
    return

def disp_check():

    return

def invalidate():

    return

def main():
    #print("hello world")
    forest_depth = 12
    num_trees = 4
    img_h = 480
    img_w = 640

    X_train, X_test, y_train, y_test = get_dataset()
    print("done loading in dataset")

    # set up classifiers, one RF per line
    models = []
    for x in range(img_h):
        models.append(get_model(num_trees, forest_depth))

    # set up accuracy, rmse, and feature arrays

    training_acc = [0]*img_h
    test_acc = [0]*img_h
    training_rmse = [0]*img_h
    test_rmse = [0]*img_h
    kept_feats = [0]*img_h
    #print(type(X_train))
    print(len(X_train))
    print(len(y_train))
    # loop through individual lines of images, grab features (individual pixels)
    for img_idx in range (len(X_train)):

        imgX = X_train[img_idx]
        imgY = y_train[img_idx]
        featsX = utils.extract_image_feats(imgX, img_h, img_w, imgX.shape[0])
        featsY = utils.extract_image_feats(imgY, img_h, img_w, imgY.shape[0])

main()












##this file contains the primary code for the HyperDepth implementation
##CURRENTLY CONTAINS:
## --> RFC setup & training

##path to GT data [fill in later]
#data_path = "\data_path"
#labels_path = "\labels_path"

## for now assuming image resolution of 1920x1280 -- may change later
#num_pixels_x = 1280 # length of scanline
#num_pixels_y = 1920
#num_features = 64 # might change
#forest_depth = 12
#train_test_split_frac = 0.8
#num_trees = 4 # authors used 4 trees in paper
#pixel_radius = 15 # pixel radius for rand features

##calculate random number of line displacements
#displacement_idx = utils.generate_displacements(num_features, pixel_radius)

##get list of image filenames
#imgList = utils.list_images(data_path)

##grab samples from imgList
##imgList = imgList.sample(n=100) #n arbitrary for now

##reset indicies to reflect extracted samples
##imgList = imgList.reset_index(drop = True)
#line_idxs = np.arange(0, 1280) # indices of image to loop through -- WILL CHANGE

##extract features from images
#feat_vec, disp_vec, pixel_vec, ill_vec = utils.load_images(imgList, data_path, gt_path, line_idxs, 
#                                                           displacement_idx, pixel_radius, num_pixels_x-2*pixel_radius)

##loop through scanlines & train model

## set up models
#models = []
#for x in range(len(line_idxs)):
#    models.append(RandomForestClassifier(n_estimators = num_trees, max_features = 1, max_depth = forest_depth, criterion = 'entropy', 
#                                         random_state = 1234, verbose = 0, n_jobs = 2))

## set up temp vars
#train_acc = [0]*len(line_idxs)
#test_acc = [0]*len(line_idxs)
#train_rmse = [0]*len(line_idxs)
#test_rmse = [0]*len(line_idxs)
#kept_feats = [0]*len(line_idxs)

## loop through scanlines
#for idx in range(len(line_idxs)):
#    print("Calculating line " + idx + "of " + len(line_idxs))

#    # train-test split

#    # fit model

#    # calculate accuracy
















