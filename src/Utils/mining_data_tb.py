import pandas as pd
import numpy as np
import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import missingno
import time
import random
import json
import seaborn as sns
import matplotlib.pyplot  as plt

def none_values(df):

    if len(df[df.isnull().any(axis=1)] != 0):
        print("Preview of data with null values:")
        display(df[df.isnull().any(axis=1)].head(3))
        missingno.matrix(df)
        plt.show()
    else:
        print("No data with null values:")
        missingno.matrix(df)
        plt.show()

def show_duplicates(df):
    if len(df[df.duplicated()]) > 0:
        print("\n***Number of duplicated entries: ", len(df[df.duplicated()]))
        display(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)).head())
    else:
        print("\nNo duplicated entries found")


def remove_publisher(df):
    tmp_text = []

    for index,row in enumerate(df.text.values):
        try:
            record = row.split(" -", maxsplit=1)
            tmp_text.append(record[1])
        except:
            tmp_text.append(row)
    df["text"] = tmp_text
    return df