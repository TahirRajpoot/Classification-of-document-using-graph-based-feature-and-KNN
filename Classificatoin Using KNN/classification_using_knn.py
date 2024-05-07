
import nltk
import networkx as nx
import numpy as np
from nltk.tokenize import word_tokenize
import pandas as pd
import re
from collections import defaultdict
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
import seaborn as sns
import os
import gravis as gv


def create_graph(text):    
    G = nx.DiGraph()
    previous_word = None
    for word in list(text):
        if word not in G:
            G.add_node(word)
        if previous_word:
            if G.has_edge(previous_word, word):
                G[previous_word][word]['weight'] += 1
            else:
                G.add_edge(previous_word, word, weight=1)
        previous_word = word
    return G

def k_nearest_neighbour(train_data, test_instance, k):
    
    distances = []
    for train_instance, category in train_data:
        distance = mcs_distance(test_instance, train_instance)
        distances.append((category, distance))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    class_counts = defaultdict(int)
    for neighbor in neighbors:
        class_counts[neighbor[0]] += 1
    predicted_class = max(class_counts, key=class_counts.get)
    return predicted_class


def find_mcs(graph_list):
   
    mcs_graph = nx.Graph()
    common_nodes = set.intersection(*[set(g.nodes) for g in graph_list])
    mcs_graph.add_nodes_from(common_nodes)
    for node1 in common_nodes:
        for node2 in common_nodes:
            if all(g.has_edge(node1, node2) for g in graph_list):
                mcs_graph.add_edge(node1, node2)
    return mcs_graph


def mcs_distance(graph1, graph2):

    mcs = find_mcs([graph1, graph2])
    return 1 - len(mcs.edges) / max(len(graph1.edges), len(graph2.edges))

def main():


    
    # # Read the CSV files
    # data1 = pd.read_csv('updated_science_and_education_data.csv')
    # data2 = pd.read_csv('updated_health_and_fitness_data.csv')
    # data3 = pd.read_csv('updated_travel_data.csv')

    # # Preprocess and update the dataframes
    # data1 = preprocess_and_update(data1)
    # data2 = preprocess_and_update(data2)
    # data3 = preprocess_and_update(data3)

    # # Save the updated dataframes to CSV files
    # data1.to_csv('updated_science_and_education_data.csv', index=False)
    # data2.to_csv('updated_health_and_fitness_data.csv', index=False)
    # data3.to_csv('updated_travel_data.csv', index=False)

    

    # Lists to store train and test data
    train_data = []
    test_data = []

    # List of CSV file names
    csv_files = ['updated_science_and_education_data.csv',
                'updated_health_and_fitness_data.csv',
                'updated_travel_data.csv']

    # Iterate over each CSV file
    for file_name in csv_files:
        # Read the CSV file
        data = pd.read_csv(file_name)
        # Split the data into train and test
        train_data.extend(data[['preprocessed_text', 'Topic']][:12].values)
        test_data.extend(data[['preprocessed_text', 'Topic']][12:15].values)
        

    # Example: Print length of train and test data
    print("Train data length:", len(train_data))
    print("Test data length:", len(test_data))
    # for row in test_data: 
    #     print(row[1])
    train_graphs = [(create_graph(str(row[0])), str(row[1])) for row in train_data]
    test_graphs = [(create_graph(str(row[0])), str(row[1])) for row in test_data]

    graph = train_graphs[0]
    gv.d3(graph).display() 

    k = 5
    predictions = []
    true_labels = []
    for test_instance, category in test_graphs:
        predicted_class = k_nearest_neighbour(train_graphs, test_instance, k)
        predictions.append(predicted_class)
        true_labels.append(category)
        print(f'Predicted class: {predicted_class}, Actual Class: {category}')

    print("Classification Report:")
    print(classification_report(true_labels, predictions))


if __name__ == "__main__":
    main()
