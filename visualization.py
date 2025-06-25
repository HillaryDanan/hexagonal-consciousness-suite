{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # visualization.py - Shared visualization utilities\
import matplotlib.pyplot as plt\
import numpy as np\
from matplotlib.animation import FuncAnimation\
import plotly.graph_objects as go\
\
def create_consciousness_animation(grid, activation_history):\
    """Creates animated visualization of consciousness propagation"""\
    fig, ax = plt.subplots(figsize=(12, 10))\
    \
    def animate(frame):\
        ax.clear()\
        \
        # Get activation state for this frame\
        activations = activation_history[frame]\
        \
        # Visualize hexagonal grid with activations\
        grid.visualize(ax=ax, activations=activations,\
                      title=f"Consciousness Propagation: Step \{frame\}")\
        \
        # Add timestamp\
        ax.text(0.02, 0.98, f"t = \{frame * 0.1:.1f\}s", \
               transform=ax.transAxes, fontsize=12,\
               verticalalignment='top',\
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\
    \
    anim = FuncAnimation(fig, animate, frames=len(activation_history),\
                        interval=100, blit=False)\
    \
    return anim\
\
def create_twitter_ready_visualization(data, title):\
    """Creates visualization optimized for Twitter sharing"""\
    # Twitter optimal: 16:9 aspect ratio\
    fig, ax = plt.subplots(figsize=(16, 9))\
    \
    # High contrast colors\
    colors = ['#1DA1F2', '#14171A', '#657786', '#AAB8C2', '#E1E8ED']\
    \
    # Large, clear fonts\
    plt.rcParams.update(\{'font.size': 14, 'font.weight': 'bold'\})\
    \
    # Create compelling visualization\
    # ... (visualization code specific to data type)\
    \
    # Add watermark\
    ax.text(0.98, 0.02, '@HillaryConsciousness', \
           transform=ax.transAxes, fontsize=10,\
           horizontalalignment='right', alpha=0.7)\
    \
    # Save in Twitter-friendly format\
    plt.savefig(f'\{title.replace(" ", "_")\}_twitter.png', \
               dpi=150, bbox_inches='tight', facecolor='white')\
    \
    return fig}