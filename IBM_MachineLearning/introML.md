# Introduction to Machine Learning - Course Summary

## Definition and High Level Overview

### AI, Machine Learning, and Deep Learning Hierarchy
- **AI (Artificial Intelligence)**: General field with broad scope including computer vision, language processing, creativity, and summarization
- **Machine Learning**: Branch of AI covering statistical aspects, teaches computers to solve problems by learning from examples
- **Deep Learning**: Subset of machine learning enabling computers to learn and make intelligent decisions independently with deeper automation

### Core Concepts
- **Machine Learning Motivation**: Enable machines to learn from experience without explicit programming
- **Data**: Input for all machine learning algorithms used to train model parameters
- **Common Languages**: Python, R, Julia, Scala, Java, JavaScript

### Important Distinctions
- **Classification vs Regression**: Classification works with discrete classes, regression with continuous variables
- **Supervised vs Unsupervised**: Supervised uses labeled data for training, unsupervised finds patterns without labels

## ML Model Lifecycle

### The Six Key Phases
1. **Problem Definition**: Align ML solution with client needs and clearly state the situation
2. **Data Collection**: Determine data types, identify sources, and gather relevant information
3. **Data Preparation**: Transform, wrangle, aggregate, join, merge, and map data onto central source (most time-consuming step)
4. **Model Development**: Leverage existing frameworks and resources to create suitable ML module
5. **Model Evaluation**: Tune model parameters and test performance on dataset
6. **Model Deployment**: Deploy model with potential for future retraining based on new information

## Techniques

### Supervised Learning
- **Definition**: "Teaching" a model to the machine using labeled data
- **Classification**: 
  - Predicts class labels or categories for predefined classes
  - Common algorithms: KNN, logistic regression, decision trees
  - Performance measured using confusion matrix
  - Key terms: classifier, feature, evaluation
- **Regression**: 
  - Predicts continuous variables showing relationship between dependent and independent variables
  - Performance measured using R-squared value (variance explanation)

### Unsupervised Learning
- **Definition**: Model works independently without supervision
- **Key Techniques**:
  - **Clustering**: Groups similar data points by characteristics
    - Used for discovering data structure, summarizing data, detecting anomalies
    - Most popular unsupervised learning technique
  - **Dimensionality Reduction**: Reduces redundant features to ease classification
  - **Market Basket Analysis**: Predicts item purchase patterns based on buying behavior
  - **Density Estimation**: Explores data to find structure

### Reinforcement Learning
- **Definition**: Reward-based learning system where machine learns through trial and error
- **Key Components**:
  - **Agent**: Algorithm that interacts with environment and selects actions to maximize reward
  - **Environment**: Surroundings containing states that agent operates in
  - **State**: Concrete situation agent finds itself in
  - **Reward**: Value returned by environment for agent's actions
  - **Policy**: Defines how agent acts in specific states (lookup table, function, algorithm, or probability)
- **Types**:
  - **Positive Reinforcement**: Increases behavior strength and frequency, maximizes performance
  - **Negative Reinforcement**: Strengthens behavior by avoiding negative conditions, sets minimum standards

## Deep Learning

### Historical Context and Definition
- **Term Origin**: Coined by Geoffrey Hinton in 2006, cognitive psychologist and computer scientist
- **Definition**: Subset of machine learning using mathematical models that mimic the human brain
- **Key Advantages**: Eliminates need for data pre-processing and automates feature extraction

### Neural Network Structure
- **Artificial Neural Network**: Group of connected nodes (neurons) in layers, loosely modeling human brain
- **Neuron**: Computation unit expressed as weighted sum of inputs
- **Three Layers**: Input layer, hidden layer(s), output layer
- **Requirements**: Large amounts of data for training

### Applications
- **DeepArt.io**: Website using deep learning for artistic style transfer, applying stylistic elements of one image to paint another image without requiring artistic skills
