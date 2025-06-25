{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # data_generators.py - Simulated neuroscience data\
import numpy as np\
from scipy import signal\
\
def generate_bilateral_activation(duration=10, sampling_rate=1000):\
    """Generates realistic bilateral brain activation patterns"""\
    t = np.linspace(0, duration, duration * sampling_rate)\
    \
    # Base oscillations (alpha, beta, gamma bands)\
    alpha = np.sin(2 * np.pi * 10 * t) * np.random.rand()\
    beta = np.sin(2 * np.pi * 20 * t) * np.random.rand() * 0.7\
    gamma = np.sin(2 * np.pi * 40 * t) * np.random.rand() * 0.5\
    \
    # Left hemisphere\
    left_activation = alpha + beta + gamma\
    left_activation += np.random.normal(0, 0.1, len(t))  # Neural noise\
    \
    # Right hemisphere with slight delay and amplitude difference\
    delay_samples = int(0.01 * sampling_rate)  # 10ms interhemispheric delay\
    right_activation = np.roll(left_activation, delay_samples) * 0.9\
    right_activation += np.random.normal(0, 0.1, len(t))\
    \
    # Add bilateral synchronization events\
    sync_events = np.random.rand(len(t)) > 0.98\
    left_activation[sync_events] *= 2\
    right_activation[sync_events] *= 2\
    \
    return t, left_activation, right_activation\
\
def generate_semantic_embeddings(num_words=100, embedding_dim=300):\
    """Creates realistic word embeddings with semantic structure"""\
    # Create semantic clusters\
    num_clusters = 5\
    cluster_centers = np.random.randn(num_clusters, embedding_dim)\
    \
    embeddings = []\
    labels = []\
    \
    for i in range(num_words):\
        # Assign to cluster\
        cluster = i % num_clusters\
        labels.append(cluster)\
        \
        # Generate embedding near cluster center\
        noise = np.random.randn(embedding_dim) * 0.3\
        embedding = cluster_centers[cluster] + noise\
        \
        # Normalize\
        embedding = embedding / np.linalg.norm(embedding)\
        embeddings.append(embedding)\
    \
    return np.array(embeddings), labels\
\
def generate_consciousness_states(num_states=1000, state_dim=6):\
    """Generates time series of consciousness states"""\
    # Hidden Markov Model for consciousness states\
    transition_matrix = np.array([\
        [0.7, 0.2, 0.1],  # Awake\
        [0.3, 0.5, 0.2],  # Drowsy  \
        [0.1, 0.2, 0.7]   # Sleep\
    ])\
    \
    states = []\
    current_state = 0\
    \
    for _ in range(num_states):\
        # Generate observation for current state\
        if current_state == 0:  # Awake\
            observation = np.random.randn(state_dim) * 0.5 + 1\
        elif current_state == 1:  # Drowsy\
            observation = np.random.randn(state_dim) * 0.7\
        else:  # Sleep\
            observation = np.random.randn(state_dim) * 0.3 - 0.5\
        \
        states.append(observation)\
        \
        # Transition to next state\
        current_state = np.random.choice(3, p=transition_matrix[current_state])\
    \
    return np.array(states)}