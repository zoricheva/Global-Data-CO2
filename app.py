from flask import Flask, render_template, request
from process import get_prediction
from sklearn.preprocessing import MinMaxScaler
import pickle
import sklearn

app = Flask(__name__)
