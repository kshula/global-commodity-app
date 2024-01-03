# Global Commodity Data Visualization App
![](img/globe.png)
A commodity market is a market that trades in the primary economic sector rather than manufactured products, such as cocoa, fruit and sugar. Commodity markets are global in character and interconnected both intra-regionally and within supply chains. There are several commodities on the globe and it is difficlut to analysis several at once. This app has data built on world bank commodities prices and allows seamless data analysis for all commodities in one place.

Welcome to the Global Commodity Data Visualization App! This Streamlit application allows you to explore and visualize global commodity data and index information. You can navigate through different pages to analyze specific datasets and create interactive visualizations.

## Features

- **Home Page:** Provides an overview of the app and displays energy and metal indice graphs showcasing specific columns from the index dataset.

- **Commodities Page:** Allows you to select commodities and visualize their data using Plotly Express line charts.

- **Index Page:** Enables you to choose index variables for visualization using Plotly Express line charts.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kshula/global-commodity-visualization-app.git
   cd global-commodity-visualization-app
   ```
2. Navigate to the project directory:

    ```bash
    cd global-commodity-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:

    ```bash
    streamlit run app.py
    ```

## Dependencies

- Streamlit
- Pandas
- Plotly

## App Structure
app.py: The main Streamlit application script.
data/: Folder containing CSV data files (data_commodity.csv and index.csv).
requirements.txt: List of Python dependencies.

## Screenshots
![](img/globe.png)

## Creator and Contact Information

- **Creator:** Kampamba Shula
- **Email:** kampambashula@gmail.com
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/kampamba-shula-03946633/)
- **GitHub:** [GitHub Profile](https://github.com/kshula)