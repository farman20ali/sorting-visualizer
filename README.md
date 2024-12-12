# sorting-visualizer
 This Flask web app demonstrates the execution of sorting algorithms (Merge, Insertion, Selection etc.) Users can test algorithms on arrays provided directly, via files, or generated randomly, and compare performance on varying sizes. It features execution time visualizations (bar/line plots), result downloads, and aids in algorithm analysis.


# Sorting Algorithm Performance Visualizer

This Flask web application allows users to test and compare the performance of various sorting algorithms on arrays of different sizes and types. It includes features for result visualization and downloading.

## Features

- **Input Options**:
  - Directly enter an array.
  - Upload a file containing an array.
  - Generate a random array of a specified size.
  
- **Execution Modes**:
  - Test a single array with selected sorting algorithms.
  - Compare multiple algorithms on arrays of varying sizes.
  
- **Visualization**:
  - Bar chart to compare execution times for a single array.
  - Line graph to show algorithm performance trends for varying input sizes.

- **Download Results**: Retrieve execution results as a `.txt` file.

## Algorithms Supported

- Merge Sort
- Insertion Sort
- Selection Sort
- Bubble Sort
- Quick Sort

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sorting-visualizer.git
   cd sorting-visualizer



## Running the Application

### 1. Create a Virtual Environment  
Set up a Python virtual environment to isolate dependencies:
```bash
    python -m venv venv

```
Activate the environment:
- On **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```
- On **Windows (CMD)**:
  ```cmd
  venv\Scripts\activate
  ```
- On **Windows (PowerShell)**:
  ```powershell
  .\venv\Scripts\Activate
  ```

### 2. Install Dependencies  
Install the required Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Run the Application  
Start the Flask application:
```bash
python app.py
```


### 4. Access the Application  
Open your web browser and go to:
```
http://127.0.0.1:5000
```

---

## Tags
`Flask` `Sorting Algorithms` `Data Visualization` `Algorithm Comparison` `Python` `Bar Graph` `Line Graph` `Random Arrays`

---

## License
This project is licensed under the [MIT License](LICENSE).
```

You can copy and paste this directly into your README file. Let me know if you need further adjustments!
