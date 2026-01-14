**Tactical Profiling of Premier League Teams Using PCA & Unsupervised Clustering**

**Overview**

This project applies dimensionality reduction and unsupervised learning to uncover distinct tactical archetypes within Premier League team performance data. Using advanced metrics sourced from FBref’s StatHead database, the analysis focuses on seasons from 2017–18 onward, the earliest period where detailed event‑ and possession‑based statistics are consistently available. 
The workflow combines PCA to map underlying tactical dimensions with k‑means clustering to group teams into interpretable playstyle profiles. The goal is to move beyond raw metrics and reveal meaningful tactical identities—proactive vs reactive teams, efficient finishers vs high‑tempo pressers, and everything in between

**Data Source**

All data was collected through FBref’s StatHead database:
https://www.sports-reference.com/stathead/fbref/
Only seasons containing the advanced metrics required for feature engineering were included. These metrics (xG, xAG, shot quality, buildup indicators, possession structure, etc.) are consistently available beginning in 2017–18, which defines the scope of the dataset.


**Methodology** 

**1. Feature Engineering**

Metrics were selected to capture multiple dimensions of team behavior, including:
- Chance creation & shot quality
  
- Defensive pressure & concession patterns
  
- Possession structure & buildup tendencies
  
- Verticality, tempo, and transition behavior
  
- Finishing and assist efficiency
Custom metrics such as Finishing Efficiency and Assist Efficiency were engineered to quantify over/under‑performance relative to expected values.

**2. Dimensionality Reduction (PCA)**

PCA was used to reduce the feature space into interpretable tactical axes.
Key components captured:
- PC1: Proactivity vs reactivity (xG, goals, possession vs GA, verticality)
  
- PC2: Efficiency vs chaos (finishing/assist efficiency vs high‑tempo, low‑conversion play)
  
These axes form a 2D tactical map used for clustering and visualization.

**3. Clustering (k‑Means)**

Multiple values of k were tested to understand how cluster count affects tactical separation.
Evaluation metrics included:
- Silhouette Score
  
- Calinski–Harabasz Score
  
- Davies–Bouldin Score
  
While k=2 provides the strongest mathematical separation, it oversimplifies football into a binary.
The analysis identifies k=5 as the optimal balance between:
- Distinct tactical identities
  
- Realistic overlap between similar styles
  
- Interpretability of centroids
Beyond k=5, cluster quality declines sharply, indicating diminishing returns.

**Results**

**Tactical Archetypes**

The model identifies five distinct tactical profiles, each representing a coherent style of play derived from statistical behavior.

**Cluster Evaluation**

Silhouette scores show:
- Strong separation at k=2
- Gradual decline through k=5
- Sharp drop‑off beyond k=5
This pattern reflects the natural overlap of real football styles and supports the chosen baseline.

**Visualizations**

The project includes:
- PCA tactical maps
- Silhouette‑vs‑k plots
- Cluster scatterplots
- Centroid tables and tactical interpretations


**Data Limitations**

- Advanced metrics are only available from 2017–18 onward, limiting historical depth.
- Only Premier League seasons are included; cross‑competition tactical variation is not captured.
- Team‑season aggregates cannot reflect in‑match or player‑level tactical nuance.

**Future Work**

Potential extensions include:
- Expanding to other competitions (e.g., Champions League, top European leagues)
- Incorporating more seasons as advanced metrics become available
- Testing alternative clustering algorithms (GMM, HDBSCAN, spectral clustering)
- Adding player‑level or possession‑sequence data for deeper tactical granularity
- Building an interactive dashboard for exploring tactical maps and cluster identities

**Project Structure**

├── data/                  # Raw and processed datasets

├── notebooks/             # PCA, clustering, and analysis notebooks

├── src/                   # Feature engineering and modeling scripts

├── visuals/               # Plots and exported figures

└── README.md              # Project documentation

**Purpose**

This project demonstrates how statistical modeling can reveal meaningful tactical structure in football. It blends:
- rigorous machine learning
- thoughtful feature engineering
- domain‑specific tactical interpretation
- clear, portfolio‑ready storytelling


