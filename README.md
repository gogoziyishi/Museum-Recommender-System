# Museum Recommender System

👉 [Experience the interactive app here!](https://museum-recommender-system-2024.streamlit.app/)


Welcome to the Museum Recommender System project! Click on the image below to watch the video on YouTube and discover the key features of our system:

[![Museum Recommender System Demo](https://raw.githubusercontent.com/gogoziyishi/Museum-Recommender-System/main/youtube_image.png)](https://youtu.be/lvWCA3LXktQ?si=hgPdO_cCTunxOPG0 "Click to Watch Introduction Video")


## Project Overview
This Museum Recommender System is designed to enhance the cultural and educational experience for visitors by providing personalized museum recommendations. Developed as part of the Text Analytics Project Spring 2024, it leverages data from TripAdvisor reviews to identify popular museums and analyze public sentiment. Our system offers tailored suggestions to tourists, helps tourism boards in adjusting marketing strategies, aids travel agencies in creating fulfilling tour packages, and enables museum managers to refine services based on feedback.

## Team Members
- Ziyi Shi
- Yvonne Wu
- Wenbo Nie

## Data Collection and Description
Data has been collected using `bs4` for web crawling and APIs to fetch museum images. The dataset covers 1006 museums across the United States and includes more than 11,800 reviews. The data encompasses various aspects such as general museum information, visitor categories, review ratings, tag clouds from reviews, and detailed review content. It is stored in multiple formats including JSON, CSV, and Excel sheets, ensuring comprehensive coverage and ease of access.

## Data Preprocessing
Data preprocessing involved merging tables with `Excel VLOOKUP`, cleaning data challenges, and handling various file types to prepare for the analysis phase.

## Data Analysis
Our analysis pipeline includes:
1. Converting text to lowercase.
2. Applying vectorization.
3. Removing redundant context and stemming words using `nltk`.
4. Employing cosine similarity distance from `sklearn` to identify similarities between museums.

## Recommender System
The core of our project, the recommender function, predicts similar museums based on user preferences. The data is managed using the `pickle` library and integrated into a Streamlit application for a user-friendly interface. The code snippet provided illustrates the creation of state-specific similarity matrices, which are vital to our recommender engine. The repository contains a similarity_matrices directory with these matrices, allowing for tailored recommendations across different states.

## Streamlit Web Application
Our system is operationalized through a `Streamlit` web application, allowing for interactive user engagement and personalized recommendations. Our Streamlit app provides a seamless UI for users to select a state, explore museum options, and receive personalized recommendations. It features a dynamic 'Museum Explorer Map' and detailed museum profiles, including rankings and descriptions.


## Evaluation
Our models are evaluated based on accuracy scores and silhouette coefficients, with manual sampling as a comparison benchmark.

## Repository Contents
- similarity_matrices: Contains the state-specific similarity matrices.
- Fordham-University-Logo-1907.png: The university's logo.
- Museums Recommendation System.ipynb: The full analysis notebook.
- README.md: Project documentation.
- Tags.csv: Dataset with museum-related tags.
- app.py: The Streamlit app script.
- museums.pkl, museums_dict.pkl, similarity.pkl, states.pkl: Serialized files for the recommender system.
- youtube_image.png: Thumbnail for the YouTube demo.

## Acknowledgements
Our sincere thanks to everyone who contributed to the success of this project, especially for the insight and support provided by our academic mentors and peer collaborators.

## Contact

Reach out to us with any questions:

- Ziyi Shi - [Email](mailto:ziyishi@fordham.edu)
- Yvonne Wu - [Email](mailto:swu180@fordham.edu)
- Wenbo Nie - [Email](mailto:wnie5@fordham.edu)

## Acknowledgements

This project was completed as part of the Text Analytics course at Fordham University, Spring 2024.

---

© 2024 Fordham University. All rights reserved.

