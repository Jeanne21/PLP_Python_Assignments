## 💤 Sleep & Health Data Analysis

This project explores a **Sleep & Health dataset** using **Python**, **pandas**, and **matplotlib** to perform basic data analysis and visualization.
The dataset contains columns such as:

* `Person ID`
* `Gender`
* `Age`
* `Occupation`
* `Sleep Duration`
* `Quality of Sleep`
* `Physical Activity Level`
* `Stress Level`
* `BMI Category`
* `Blood Pressure`

---

### 📂 Project Structure

```
.
├── Sleep_health_and_lifestyle_dataset.csv      # Dataset 
├── sleep_and_lifestyle_analysis.ipynb     # Python analysis script
└── README.md             # Project documentation
```

---

### 🏆 Objectives

1. **Data Loading & Cleaning**

   * Load a CSV dataset using `pandas`.
   * Inspect structure, check data types, and handle missing values.

2. **Basic Analysis**

   * Compute descriptive statistics (mean, median, standard deviation).
   * Group by categories (e.g., gender, occupation) to find trends.
   * Identify patterns or interesting findings.

3. **Visualization**

   * Create **at least 4 plots** to explore relationships:

     * Line chart: Average sleep duration by age
     * Bar chart: Average stress level by occupation
     * Histogram: Physical activity level distribution
     * Scatter plot: Sleep duration vs. stress level

---

### ⚙️ Requirements

* **Python 3.8+**
* Libraries:

  * `pandas`
  * `matplotlib`

Optional for prettier visuals:

* `seaborn`

Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

---

### 🚀 Usage

1. Make sure you have **Jupyter** installed:

```bash
pip install notebook pandas matplotlib seaborn
```

2. Launch Jupyter Notebook in your terminal:

```bash
jupyter notebook
```

3. In the browser window that opens, navigate to
   `sleep_and_lifestyle_analysis.ipynb` and open it.
4. Run each cell (`Shift + Enter`) to execute the analysis and view the plots inline.

---

### 📊 Example Outputs

The program will:

* Load and clean the dataset.
* Display key statistics like mean sleep duration, average stress level, etc.
* Generate visualizations such as:

| Plot Type    | Insight Example                                           |
| ------------ | --------------------------------------------------------- |
| Line Chart   | Shows how sleep duration varies by age                    |
| Bar Chart    | Compares average stress level by job type                 |
| Histogram    | Shows distribution of physical activity                   |
| Scatter Plot | Highlights relationship between sleep duration and stress |

---

### 🧠 Observations (Sample)

* **Sleep Duration vs Stress Level:** People with higher stress levels tend to have shorter sleep durations.
* **Occupation Patterns:** Certain occupations show higher average stress compared to others.

*(Your findings may vary depending on the dataset used.)*

---

### 📜 License

This project is for **educational purposes only**.
Dataset rights belong to the original source.
