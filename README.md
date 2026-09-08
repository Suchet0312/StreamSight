# 🎬 StreamSight

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=plotly&logoColor=white)

**An end-to-end OTT analytics and recommendation platform built on MovieLens data**

[Overview](#-overview) •
[Features](#-features) •
[Installation](#-installation) •
[Project Structure](#-project-structure) •
[Results](#-results) •
[Roadmap](#-roadmap)

</div>

---

## 🎯 Overview

StreamSight is a comprehensive analytics and recommendation platform that demonstrates real-world OTT product analytics skills. Built on the MovieLens 1M dataset, it combines product analytics, user segmentation, and multiple recommendation approaches into a cohesive, interview-ready project.

### 🎪 Key Highlights

- 📊 **Product Analytics**: CTR, play rates, completion metrics, and retention proxies
- 👥 **User Segmentation**: K-Means clustering for behavioral personas
- 🤖 **Recommendation Systems**: Popularity, content-based, collaborative filtering, and hybrid models
- 📈 **Offline Evaluation**: Time-aware evaluation with Precision@K, Recall@K, MAP@K, and NDCG@K
- 🔍 **Deep Analysis**: Cold-start handling, popularity bias, and catalog coverage metrics

### ⚠️ Important Note

This project uses MovieLens interaction data as its foundation. **All OTT event telemetry (clicks, plays, completions, watch times) is explicitly simulated** for educational and demonstration purposes. These metrics are clearly labeled as synthetic throughout the codebase and documentation.

---

## ✨ Features

### 📊 Product Analytics & Metrics
- **Event Simulation Layer**: Realistic OTT events derived from MovieLens ratings
- **Product KPIs**: CTR, play rate, completion rate, watch hours
- **User Behavior Metrics**: Session analysis, engagement frequency, retention proxies
- **Content Performance**: Movie-level engagement and interaction patterns

### 👥 User Segmentation
- **Behavioral Features**: 38 user-level features combining MovieLens and simulated metrics
- **K-Means Clustering**: Data-driven user persona identification
- **Silhouette Analysis**: Systematic cluster number selection
- **Genre Preferences**: User-level content preference profiling

### 🎯 Recommendation Systems
- **Popularity Baseline**: Most-interacted items benchmark
- **Content-Based Filtering**: TF-IDF on movie titles and genres
- **Collaborative Filtering**: Item-item cosine similarity
- **Hybrid Approach**: Weighted combination with validation-based tuning
- **Cold-Start Handling**: Popularity fallback for low-history users

### 📈 Evaluation & Analysis
- **Time-Aware Splitting**: Chronological train/test to prevent data leakage
- **Ranking Metrics**: Precision@K, Recall@K, MAP@K, NDCG@K at multiple K values
- **Catalog Coverage**: Diversity and long-tail item analysis
- **Popularity Bias**: Recommendation concentration measurement
- **Cold-Start Performance**: Specific evaluation for edge cases

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Suchet0312/StreamSight.git
cd StreamSight
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Verify data files**
Ensure the MovieLens data files are present in `data/raw/`:
- `movies.dat`
- `ratings.dat`
- `users.dat`

---

## 📁 Project Structure

```
StreamSight/
│
├── 📂 data/
│   ├── 📂 raw/                          # Original MovieLens data
│   │   ├── movies.dat
│   │   ├── ratings.dat
│   │   └── users.dat
│   ├── 📂 day2/                         # Product analytics & segmentation outputs
│   │   ├── simulated_ott_events.csv.gz
│   │   ├── product_metrics.csv
│   │   ├── user_features.csv
│   │   ├── user_features_with_clusters.csv
│   │   ├── segmentation_cluster_profiles.csv
│   │   └── *.png (visualizations)
│   └── 📂 day3/                         # Recommendation system outputs
│       ├── model_comparison.csv
│       ├── recommendation_examples.csv
│       └── evaluation metrics...
│
├── 📂 notebooks/
│   ├── 01_data_understanding.ipynb      # Data exploration & EDA
│   └── 03_eda.ipynb                     # Extended analysis
│
├── 📄 requirements.txt                   # Python dependencies
├── 📄 README.md                         # This file
└── 📄 .gitignore                        # Git ignore rules
```

---

## 📊 Results

### Product Metrics (Simulated)

| Metric | Value |
|--------|-------|
| **Total Users** | 6,040 |
| **Total Movies** | 3,706 |
| **MovieLens Interactions** | 1,000,209 |
| **Simulated Events** | 1,859,876 |
| **Simulated Sessions** | 25,163 |
| **CTR** | 37.76% |
| **Play Rate (given click)** | 79.49% |
| **Completion Rate (given play)** | 60.56% |
| **Total Watch Hours** | 405,302.8 |
| **Avg Watch Time per Play** | 81.00 minutes |
| **D7 Retention Proxy** | ~29% |

> ⚠️ **Note**: All OTT metrics above are synthetic/derived project metrics, not factual production telemetry.

### User Segmentation

**K-Means Clustering Results** (K=2 selected via silhouette analysis)

| Cluster | Size | % of Users | Characteristics |
|---------|------|------------|-----------------|
| **Cluster 0** | 2,597 | 43% | Heavy Engagers - High activity, longer watch times |
| **Cluster 1** | 3,443 | 57% | Light Engagers - Lower activity levels |

**Silhouette Scores by K**:
- K=2: **0.3054** ⭐ (Selected)
- K=3: 0.2932
- K=4: 0.2143
- K=5: 0.2130

### User Features Generated

**38 comprehensive user-level features** including:
- **Factual MovieLens**: rating count, unique movies, average rating, recency, active span
- **Simulated OTT**: sessions, plays, completions, watch time, engagement frequency
- **Content Preferences**: Genre-level preference shares across 18+ genres

---

## 🛠️ Technologies Used

### Core Libraries
- **Pandas** (3.0.5) - Data manipulation and analysis
- **NumPy** (2.5.3) - Numerical computing
- **scikit-learn** (1.9.0) - Machine learning algorithms
- **Matplotlib** (3.11.1) - Data visualization
- **Seaborn** (0.13.2) - Statistical visualizations

### Analysis & Modeling
- K-Means clustering for user segmentation
- TF-IDF for content-based recommendations
- Cosine similarity for collaborative filtering
- Ranking metrics (Precision@K, Recall@K, MAP@K, NDCG@K)

---

## 🗺️ Roadmap

### ✅ Completed
- [x] **Day 1**: Data preprocessing, EDA, SQL foundation
- [x] **Day 2**: Event simulation, product metrics, user segmentation
- [x] **Day 3**: Recommendation systems with offline evaluation (In Progress)

### 🚧 In Progress
- [ ] Complete Day 3 recommendation system validation
- [ ] Verify all evaluation metrics and model comparison

### 📋 Planned
- [ ] **Day 4**: Deep recommendation analysis & improvements
  - Activity-segment performance
  - Popular vs long-tail analysis
  - Enhanced cold-start strategies
- [ ] **Day 5**: Reusable recommendation pipeline
  - Modular codebase structure
  - Configuration management
  - Model persistence
- [ ] **Day 6**: REST API layer (FastAPI)
  - Personalized recommendation endpoints
  - Analytics endpoints
  - Swagger documentation
- [ ] **Day 7**: Dashboard/UI
  - User recommendation interface
  - KPI visualization
  - Model performance comparison
- [ ] **Day 8+**: Production polish
  - Comprehensive testing
  - Docker deployment
  - Complete documentation
  - Interview preparation materials

---

## 🎓 Learning Outcomes

This project demonstrates:

1. **Product Analytics Thinking**
   - Event tracking and funnel analysis
   - Product KPI definition and measurement
   - User behavior pattern identification

2. **Data Science Pipeline**
   - End-to-end ML workflow from raw data to insights
   - Feature engineering for user understanding
   - Unsupervised learning for segmentation

3. **Recommendation Systems**
   - Multiple recommendation paradigms
   - Proper offline evaluation methodology
   - Time-aware data splitting to prevent leakage
   - Cold-start and bias analysis

4. **Software Engineering**
   - Clean, reproducible code structure
   - Git version control
   - Clear documentation and simulation disclosure

5. **Business Communication**
   - Honest representation of assumptions and limitations
   - Metrics interpretation and storytelling
   - Trade-off analysis (accuracy vs. diversity vs. complexity)

---

## 📝 Data Source

This project uses the [MovieLens 1M Dataset](https://grouplens.org/datasets/movielens/1m/):
- 1 million ratings from 6,000 users on 4,000 movies
- Released by GroupLens Research at the University of Minnesota
- Used for academic and educational purposes

### Citation
```
F. Maxwell Harper and Joseph A. Konstan. 2015. 
The MovieLens Datasets: History and Context. 
ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19.
```

---

## 🤝 Contributing

This is a personal portfolio project, but suggestions and feedback are welcome! Feel free to:
- Open an issue for bugs or suggestions
- Share ideas for improvements
- Fork the repo for your own learning

---

## 📧 Contact

**Suchet** - [GitHub Profile](https://github.com/Suchet0312)

Project Link: [https://github.com/Suchet0312/StreamSight](https://github.com/Suchet0312/StreamSight)

---

## 📄 License

This project is created for educational and portfolio purposes. The MovieLens dataset is provided by GroupLens Research and used under their terms.

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star!**

Built with 💙 for learning and demonstration

</div>
