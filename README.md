# Fake-News-Detection-System
Fake News Detection in Python

In this project, we have used various natural language processing techniques and machine learning algorithms to classify fake news articles using sci-kit libraries from python.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them:

1. Python 3.6

  • This setup requires that your machine has python 3.6 installed on it. you can refer to this url https://www.python.org/downloads/ to download python. Once you have python downloaded and installed, you will need to setup PATH variables (if you want to run python program directly, detail instructions are below in how to run software section). To do that check this: https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/.
  
  • Setting up PATH variable is optional as you can also run program without it and more instruction are given below on this topic.

2. Second and easier option is to download anaconda and use its anaconda prompt to run the commands. To install anaconda check this url https://www.anaconda.com/download/
3. You will also need to download and install below 3 packages after you install either python or anaconda from the steps above
  
  • Sklearn (scikit-learn)  
  • numpy  
  • scipy

• if you have chosen to install python 3.6 then run below commands in command prompt/terminal to install these packages

```
pip install -U scikit-learn
pip install numpy
pip install scipy
```

• if you have chosen to install anaconda then run below commands in anaconda prompt to install these packages

```
conda install -c scikit-learn
conda install -c anaconda numpy
conda install -c anaconda scipy
```

### Dataset used
The data source used for this project is Fake-Real News Dataset uploaded on Kaggle platform:- https://www.kaggle.com/techykajal/fakereal-news which contains one .csv file named New Task.csv. Below is some description about the data file used for this project.
This dataset is having 6 attributes among which News_Headline is the most important to us in order to classify news as FALSE or TRUE. As you notice the Label attribute clearly, there are 6 classes specified in it. So, it's totally up-to you whether you want to use my dataset for multi-class classification or convert these class labels into FALSE or TRUE and then, perform binary classification. Although, for your convenience, I will write a notebook on how to convert this dataset from multi-class to binary-class. To deal with the text data, you need to have good hands on practice on NLP & Data-Mining concepts.

  
  • **News_Headline** - contains piece of information that has to be analysed.  
  
  • **Link_Of_News** - contains url of News Headlines specified in very first column.
  
  • **Source** - this column contains author names who has posted the information on facebook, instagram, twitter or any other social-media platform.
  
  • **Stated_On** - This column contains date when the information is posted by the authors on different social-media platforms.
  
  • **Date** - This column contains date when this piece of information is analysed by politifact team of fact-checkers in order to labelize as FAKE or REAL.
  
  • **Label** - This column contains 5 class labels : True, Mostly-True, Half-True, Barely-True, False, Pants on Fire.
  
 So, you can either perform multi-class classification on it or convert Mostly-True, Half-True, Barely-True as True and drop Pants on Fire and perform Binary-class classification.
 
 
 ### File Descriptions
 
 **Dataset**
 
 This folder contains dataset named **News.csv**. You can also access this dataset using Kaggle platform:- https://www.kaggle.com/techykajal/fakereal-news and download it for your use.
 
 **Data Pre-processing**
 
 This folder contains two files one is a python script named "**Text Pre-processing with stopwords.ipynb**" and another is a Dataset obtianed after pre-processing of the original dataset. The pre-processed dataset is stored in file named "**Cleaned_Data.csv**". Now this cleaned dataset is in ready to use form for implementing further steps of Pipeline.
 
 **Data Visualization**
 
 This folder contains one python script named "**Visualization_with_Stopwords.ipynb**". Run this file to see the exploratory data analysis of the Dataset, how many columns are there, which feature is valuable, importance of each feature in the problem statement that you want to solve, data distribution per each label, Word cloud for instances that labeled as Fake News, Word cloud for instances that labeled as Real News, finding frequent word counters in both Real news instances and Fake news instances.
 
 **ML Pipeline & Deployment**
 
 This folder contains two python script named "**Fake_News_Det.py**" and "**Modelling With Stopwords.ipynb**". **Modelling** file contains script of forming machine learning pipeline and deciding on the best ML models to use for the deployment purpose. **Fake_News_Det** file contains code for the deployment purpose. You can see the demonstartion here , just enter any piece of News and it will return you with the result whether the news is **Fake** or **Real**.
 **model.pkl** file contains the final best model that was selected for the production in the deployed stage. **requirements.txt** is the file that conatains all the necessary library that is needed for the project to work.
 
 Look at the screenshots below to understand the end result precisely.
 - After running the " **Fake_News_Det.py** " file, it will return with the link to the interactive dashboard like below:-
 
 ![alt text](https://github.com/techykajal/Fake-News-Detection-System/blob/50d5f3f55da4d1aacffff84bb632beaf7cd03cc9/Fake_News_Detector.png)
 
 - Enter the piece of news you want to see results for:-
 
 ![alt text](https://github.com/techykajal/Fake-News-Detection-System/blob/50d5f3f55da4d1aacffff84bb632beaf7cd03cc9/Fake_News_Detector_with_News.png)
 
 - The below screenshot will show the result for the entered piece of news, whether it is a fake news or real news.
 
 ![alt text](https://github.com/techykajal/Fake-News-Detection-System/blob/50d5f3f55da4d1aacffff84bb632beaf7cd03cc9/Fake_News_Detector_Result.png)
 
 
 
 Here is the link to the interactive session of Fake News Detector:- http://127.0.0.1:5000/, Note:- it might not work directly from here. To atain this step follow few more stepps on your terminal.
 
 ### You can achieve this link to interactive session by following the below commands:-
 - Open Command prompt
 - Change directory and go to the path where your **Fake_News_Det.py** is saved.
 - create virtual environment.
 - Run command " **Python Fake_News_Det.py** ", if it shows error for some packages that has not been installed.
 - Install necessary packages and libraries using **pip** command.
 - After meeting all requirements.
 - Run this command " **Python Fake_News_Det.py** " again, it will share the link to the interactrive window as shown in the below screenshot after highlighting.

![alt text](https://github.com/techykajal/Fake-News-Detection-System/blob/50d5f3f55da4d1aacffff84bb632beaf7cd03cc9/Interactive_Detector_URL.png)

 - copy paste the link into the browser and enter.
 - Now insert any piece of news from your dataset and check the results.
 
 
 
