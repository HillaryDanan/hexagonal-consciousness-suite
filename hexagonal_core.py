{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww16680\viewh13180\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # hexagonal_core.py - Foundation for all demonstrations\
import numpy as np\
import matplotlib.pyplot as plt\
import networkx as nx\
from matplotlib.patches import RegularPolygon\
from matplotlib.collections import PatchCollection\
\
class HexagonalConsciousnessGrid:\
    """\
    Implements hexagonal grid architecture for consciousness modeling.\
    Based on nature's optimization principles seen in grid cells, \
    molecular structures, and neural organization.\
    """\
    \
    def __init__(self, layers=3, hex_size=1.0):\
        self.layers = layers\
        self.hex_size = hex_size\
        self.neurons = \{\}\
        self.connections = nx.Graph()\
        self._build_hexagonal_architecture()\
    \
    def _build_hexagonal_architecture(self):\
        """Creates multi-layer hexagonal grid mimicking cortical columns"""\
        # Axial coordinate system for efficient hexagonal addressing\
        for layer in range(self.layers):\
            for q in range(-layer, layer + 1):\
                for r in range(max(-layer, -q - layer), \
                              min(layer, -q + layer) + 1):\
                    # Each neuron has axial coordinates and layer\
                    neuron_id = f"L\{layer\}_q\{q\}_r\{r\}"\
                    x, y = self._axial_to_cartesian(q, r)\
                    \
                    self.neurons[neuron_id] = \{\
                        'position': (x, y + layer * 3),\
                        'layer': layer,\
                        'activation': 0.0,\
                        'bilateral_partner': self._get_bilateral_partner(q, r, layer)\
                    \}\
                    self.connections.add_node(neuron_id)\
        \
        # Create hexagonal connectivity patterns\
        self._create_hexagonal_connections()\
    \
    def _axial_to_cartesian(self, q, r):\
        """Convert axial hex coordinates to cartesian for visualization"""\
        x = self.hex_size * (3/2 * q)\
        y = self.hex_size * (np.sqrt(3)/2 * q + np.sqrt(3) * r)\
        return x, y\
    \
    def _get_bilateral_partner(self, q, r, layer):\
        """Maps neurons to bilateral partners for hemispheric processing"""\
        # Mirror across the midline for bilateral activation\
        return f"L\{layer\}_q\{-q\}_r\{-r\}"\
    \
    def _create_hexagonal_connections(self):\
        """Establishes 6-neighbor connectivity pattern"""\
        # Hexagonal neighbors in axial coordinates\
        hex_directions = [(1,0), (1,-1), (0,-1), (-1,0), (-1,1), (0,1)]\
        \
        for neuron_id, data in self.neurons.items():\
            layer = data['layer']\
            # Parse coordinates from ID\
            parts = neuron_id.split('_')\
            q = int(parts[1][1:])\
            r = int(parts[2][1:])\
            \
            # Connect to 6 neighbors in same layer\
            for dq, dr in hex_directions:\
                neighbor_id = f"L\{layer\}_q\{q+dq\}_r\{r+dr\}"\
                if neighbor_id in self.neurons:\
                    self.connections.add_edge(neuron_id, neighbor_id)\
            \
            # Connect to neighbors in adjacent layers\
            if layer > 0:\
                self._connect_between_layers(neuron_id, layer, q, r)\
    \
    def propagate_activation(self, source_neurons, steps=10):\
        """Simulates consciousness propagation through hexagonal network"""\
        # Initialize activation\
        for neuron in self.neurons:\
            self.neurons[neuron]['activation'] = 0.0\
        \
        # Set source activation\
        for source in source_neurons:\
            if source in self.neurons:\
                self.neurons[source]['activation'] = 1.0\
        \
        # Propagate through hexagonal network\
        history = []\
        for step in range(steps):\
            new_activations = \{\}\
            \
            for neuron_id in self.neurons:\
                # Hexagonal propagation rule\
                neighbors = list(self.connections.neighbors(neuron_id))\
                if neighbors:\
                    neighbor_sum = sum(self.neurons[n]['activation'] \
                                     for n in neighbors)\
                    # Sigmoid activation with hexagonal normalization\
                    new_act = 1 / (1 + np.exp(-neighbor_sum/np.sqrt(6)))\
                    new_activations[neuron_id] = new_act * 0.9  # Decay factor\
            \
            # Update activations\
            for neuron_id, activation in new_activations.items():\
                self.neurons[neuron_id]['activation'] = activation\
            \
            # Record history for visualization\
            history.append(self._get_activation_snapshot())\
        \
        return history\
    \
    def visualize(self, title="Hexagonal Consciousness Architecture", \
                  show_bilateral=True):\
        """Creates publication-quality visualization of the hexagonal grid"""\
        fig, ax = plt.subplots(figsize=(12, 10))\
        \
        # Create hexagon patches\
        patches = []\
        colors = []\
        \
        for neuron_id, data in self.neurons.items():\
            x, y = data['position']\
            hexagon = RegularPolygon((x, y), 6, radius=self.hex_size/2,\
                                    orientation=0, facecolor='none')\
            patches.append(hexagon)\
            colors.append(data['activation'])\
        \
        # Create collection with colormap\
        p = PatchCollection(patches, cmap='viridis', alpha=0.8)\
        p.set_array(np.array(colors))\
        ax.add_collection(p)\
        \
        # Draw connections\
        for edge in self.connections.edges():\
            pos1 = self.neurons[edge[0]]['position']\
            pos2 = self.neurons[edge[1]]['position']\
            ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], \
                   'gray', alpha=0.3, linewidth=0.5)\
        \
        # Highlight bilateral connections if requested\
        if show_bilateral:\
            for neuron_id, data in self.neurons.items():\
                partner = data['bilateral_partner']\
                if partner in self.neurons:\
                    pos1 = data['position']\
                    pos2 = self.neurons[partner]['position']\
                    ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], \
                           'red', alpha=0.2, linewidth=1, linestyle='--')\
        \
        ax.set_xlim(-10, 10)\
        ax.set_ylim(-2, 12)\
        ax.set_aspect('equal')\
        ax.axis('off')\
        ax.set_title(title, fontsize=16, pad=20)\
        \
        # Add colorbar\
        plt.colorbar(p, ax=ax, label='Neural Activation', shrink=0.6)\
        \
        return fig, ax}