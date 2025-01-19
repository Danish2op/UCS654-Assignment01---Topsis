# UCS654-Assignment01---Topsis

---

# 🧠 Topsis Assignment01

This repository contains a comprehensive implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method. The project is structured into multiple programs, each showcasing a unique aspect of the TOPSIS concept.

---

## 📂 Structure

### 📁 Program 1: Basic Application of TOPSIS

This folder contains a simple implementation of the **TOPSIS method** applied to a dataset. The code demonstrates how to calculate the TOPSIS scores for alternatives based on multiple criteria, using basic Python programming techniques.

---

### 📁 Program 2: TOPSIS Python Package

This folder contains the full implementation of the **Topsis102203633Danishsharma** Python package. The package provides advanced functionalities for performing TOPSIS analysis, including missing data handling, flexible distance metrics, and even voice control.

For details on how to install and use the package, refer to the README section below.

---

### 📁 Program 3: Hosted Website Using Streamlit

This folder contains the complete code for a **Streamlit-based web application** that utilizes the `Topsis102203633Danishsharma` package to perform TOPSIS analysis. The website allows users to upload datasets, configure weights and impacts, and view ranked alternatives with visualizations.

🔗 **Hosted Website**: [https://topsis102203633danishsharma.streamlit.app/](https://topsis102203633danishsharma.streamlit.app/)

---

# 🧠 TOPSIS Python Package by Danish Sharma 🚀

Welcome to the **Topsis102203633Danishsharma** package! 🐍 This Python package allows you to easily perform **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** analysis, a popular method in Multi-Criteria Decision Analysis (MCDA) to rank and evaluate alternatives based on multiple criteria.

## 📦 Installation

You can install the package via **pip**:

```bash
pip install topsis102203633Danishsharma
```

Alternatively, you can clone this repository and use it locally:

```bash
git clone https://github.com/Danish2op/voice-controlled-topsis-package.git
cd voice-controlled-topsis-package
python setup.py install
```

---

## 🎯 Features

- **TOPSIS Analysis**: Perform the **TOPSIS** algorithm on your dataset.
- **Handling Missing Data**: Fill missing values using various strategies like **mean**, **median**, **mode**, etc.
- **Voice Commands**: Use voice commands to run analysis, plot graphs, and more. 🎤
- **Flexible**: Supports different **distance metrics** and **criteria impacts**.
- **Easy to Use**: The interface is simple and intuitive for both beginners and experts. 😎

---

## 📂 Package Structure

Here’s an overview of the important parts of the package:

```
topsis102203633Danishsharma/
├── topsis102203633Danishsharma_core/
│   ├── __init__.py
│   ├── topsis.py
│   
├── README.md
├── setup.py
├── LICENSE
├── MANIFEST.in
```

---

## 🚀 Usage

Here’s a quick guide to using the **Topsis** class, including all available options.

### 🧑‍💻 Step 1: Import the package

```python
from topsis102203633Danishsharma_core.topsis import Topsis, fill_missing_data, VoiceControl
import pandas as pd

# Load your dataset
df = pd.read_csv('path/to/your/data.csv')

# Set weights and impacts
weights = [0.3, 0.2, 0.2, 0.1, 0.2] 
impacts = ['+', '-', '+', '-', '+']
```

### 🧑‍💻 Step 2: Create the TOPSIS Object

```python
topsis = Topsis(df, weights, impacts, distance_metric='euclidean', missing_data_strategy='mean', show_para=True, reverse_rank=False)
```

- **distance_metric**: Choose from `'euclidean'`, `'manhattan'`, `'chebyshev'`, `'minkowski'`, or `'cosine'`.
- **missing_data_strategy**: Choose from `'mean'`, `'median'`, `'mode'`, `'ffill'`, `'bfill'`, `'interpolate_linear'`, or `'interpolate_polynomial'`.
- **show_para**: Set to `True` to display the full results including all parameters.

### 🧑‍💻 Step 3: Run the TOPSIS Calculation

```python
result = topsis.calculate()
print(result)
```

This will give you the alternatives ranked according to the **TOPSIS** methodology.

### 🧑‍💻 Step 4: Plot the Results (Optional)

```python
topsis.plot_graph(result)
```

This will plot a bar graph with the alternatives and their respective TOPSIS scores.

---

## 🎤 Voice-Controlled Commands

You can also use voice commands to control the package. 

### Available Commands:
- **"start"**: Start the TOPSIS analysis.
- **"fill missing"**: Fill missing data in the dataset.
- **"graph"**: Plot the graph of results.
- **"exit"**: Exit the application.
- **"help"**: Show the list of available commands.

Example usage:

```python
voice_control = VoiceControl(df, weights, impacts)
voice_control.run()  # Start listening for commands
```

---

## 💡 Default Parameters and Options

Here are the **default parameters** that you can use:

- **Distance Metric**: `'euclidean'`
- **Missing Data Strategy**: `'mean'`
- **Show Parameters**: `False`
- **Reverse Rank**: `False` the alternative with maximum topsis score is on top.

---

## 🔧 Advanced Configuration

You can configure additional parameters to fit your needs:
- **weights**: A list of weights for each criterion.
- **impacts**: A list of impacts for each criterion, where `'+'` indicates a positive impact, and `'-'` indicates a negative impact.

---

## 🤝 Contributing

We welcome contributions! If you'd like to contribute to this project, please feel free to submit a pull request or open an issue.

---

## 🧑‍💻 License

This project is licensed under the MIT License.

---

For more information, please visit our [GitHub Repository](https://github.com/Danish2op/voice-controlled-topsis-package).
