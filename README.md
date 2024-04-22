# Museum Recommender System

## Project Overview
This Museum Recommender System is designed to enhance the cultural and educational experience for visitors by providing personalized museum recommendations. Developed as part of the Text Analytics Project Spring 2024, it leverages data from TripAdvisor reviews to identify popular museums and analyze public sentiment. Our system offers tailored suggestions to tourists, helps tourism boards in adjusting marketing strategies, aids travel agencies in creating fulfilling tour packages, and enables museum managers to refine services based on feedback.

## Team Members
- Ziyi Shi
- Yvonne Wu
- Wenbo Nie

## Data Collection
Data has been collected using `bs4` for web crawling and APIs to fetch museum images. The dataset covers 1006 museums across the United States and includes more than 11,800 reviews.

## Data Description
The data encompasses various aspects such as general museum information, visitor categories, review ratings, tag clouds from reviews, and detailed review content. It is stored in multiple formats including JSON, CSV, and Excel sheets, ensuring comprehensive coverage and ease of access.

## Data Preprocessing
Data preprocessing involved merging tables with `Excel VLOOKUP`, cleaning data challenges, and handling various file types to prepare for the analysis phase.

## Data Analysis
Our analysis pipeline includes:
1. Converting text to lowercase.
2. Applying vectorization.
3. Removing redundant context and stemming words using `nltk`.
4. Employing cosine similarity distance from `sklearn` to identify similarities between museums.

## Recommender System
The core of our project, the recommender function, predicts similar museums based on user preferences. The data is managed using the `pickle` library and integrated into a Streamlit application for a user-friendly interface.

## Streamlit Web Application
Our system is operationalized through a `Streamlit` web application, allowing for interactive user engagement and personalized recommendations.


## Evaluation
Our models are evaluated based on accuracy scores and silhouette coefficients, with manual sampling as a comparison benchmark.

## Repository Contents
- `Museums Recommendation System.ipynb`: Jupyter notebook with the complete analysis and system model.
- `README.md`: This file, describing the project.
- `Tags.csv`: Dataset containing tags related to each museum.
- `app.py`: The Streamlit application for deploying the recommender system.
- `museums.pkl`, `museums_dict.pkl`, `similarity.pkl`: Serialized files containing processed museum data and similarity metrics for the recommender system.

## Acknowledgements
Our sincere thanks to everyone who contributed to the success of this project, especially for the insight and support provided by our academic mentors and peer collaborators.

## Contact
For any queries regarding this project, please reach out to:
- Ziyi Shi - [ziyishi@fordham.edu]
- Yvonne Wu - [swu180@fordham.edu]
- Wenbo Nie - [wnie5@fordham.edu]

---

Project completed as part of the Text Analytics course, Spring 2024.
