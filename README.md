**Movie Rating and Metascore Prediction**

This is a machine learning project that aims to predict movie ratings and metascores based on given input parameters such as genre, director, and actors. The model is trained using IMDb data, and users can input the main genre of the movie, director's name, and names of up to four actors to obtain predicted movie ratings and metascores.

**Project Overview**

The project consists of the following main steps:

1. Data Collection: IMDb data with information about movie genres, directors, actors, ratings, and metascores is used as the dataset for this project.
2. Data Preprocessing: The collected data is preprocessed to handle missing values, convert categorical variables to numerical representations, and perform feature engineering.
3. Model Training: The preprocessed data is used to train a machine learning model that can predict movie ratings and metascores based on input parameters.
4. Model Deployment: The trained model is deployed as a web application using Flask, allowing users to input movie details and get predicted ratings and metascores.

**Requirements**

To run this project, you need the following libraries and tools:

- Python 3.x
- pandas
- numpy
- scikit-learn
- Flask

**Project Structure**

The project files are organized as follows:

1. **Data Collection**: Contains the code to scrap the data from IMDB website.
2. **Data Preprocessing**: Contains the code to preprocess the raw data.
3. **Exploratory Data Analysis**: Contains the code for graphs and plots to visualize the data.
4. **Model and Deployement**: The Flask web application to deploy the model and allow user input for movie details.


**Getting Started**

1. Clone the repository to your local machine:

      git clone <https://github.com/ajinkyavn/IMDB-Movie-Analysis.git>

      cd movie-rating-prediction

2. Install the required libraries:

      pip install pandas numpy scikit-learn Flask

3. Run the Jupyter notebook  to collect,preprocess and visualize the data. The trained model is saved in the Model_and_Deployement directory.
  
4. After training the model, run the Flask web application using the following command:

      python app.py

5. Open a web browser and go to **http://localhost:5000** to access the web application. Enter the main genre, director's name, and up to four actor names to get predicted movie ratings and metascores.

**Note**

- The accuracy of the model is around 85% on the test data, making it a decent predictor for movie ratings and metascores. However, keep in mind that predictions may vary based on the input data and inherent uncertainties in movie ratings.
- The project can be extended by exploring different machine learning models, feature engineering techniques, and experimenting with other data sources.
- For optimal user experience and improved predictions, consider deploying the application on a production server and optimizing the machine learning model based on real user feedback and usage patterns.

**Authors**

- Ajinkya Narkhede (ajinkyanarkhede013@gmail.com)
- Sanket Naitam (sanketnaitam2206@gmail.com)

