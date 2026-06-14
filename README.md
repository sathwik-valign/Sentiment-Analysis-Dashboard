# Sentiment Analysis Dashboard

An interactive web-based dashboard that performs sentiment analysis on short texts using the VADER lexicon-based model, providing visual insights and real-time testing capabilities.

## Problem Statement
Manual sentiment analysis of large text datasets is inefficient and prone to inconsistency. This project automates the analysis process, allowing users to quickly visualize sentiment trends and test individual sentences in real-time, improving data-driven decision-making.

## Setup Instructions
To set up this project on a fresh machine, ensure you have Python installed and follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sathwik-valign/Sentiment-Analysis-Dashboard.git
   cd sentiment-dashboard
   
2. **Create and activate a virtual environment:**

### On Windows
      python -m venv .venv
      .venv\Scripts\activate

3. **Install dependencies:**


    pip install -r requirements.txt

4. **Prepare Data:**

    Download your dataset (e.g., IMDB reviews) from Kaggle.

    Rename the file to movie_review.csv and place it in the data/ folder.

5. **Run the batch processor and dashboard:**


## Process the dataset
    python -m src.analyze

## Launch the dashboard
    streamlit run app.py

6. **Usage Examples**
    Input: "This movie was absolutely fantastic and I loved every minute of it!"
    Output: - Sentiment: Positive

    Score: 0.85 (Compound score)

**Screenshots of the user interface**
Figure 1: Sentiment Analysis Dashboard Interface with Stats
<img width="450" height="450" alt="image" src="https://github.com/user-attachments/assets/e61029eb-b578-4b5f-aaea-beabd49dd2d1" /></br>

Figure 2: Most Positive Reviews with score
<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/39ec8c36-4acd-40f7-b48d-84c11d44094e" /></br>


Figure 3: Entering the review and classifying it (positive)
<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/f5dfa478-cb8e-4078-9489-c44a46bc8011" /></br>


Figure 4: Entering the review and classifying it (negative)
<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/dfa63b4e-82a1-4837-86c6-0f537b8e3450" /></br
