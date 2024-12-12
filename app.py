from flask import Flask, render_template,request,flash,redirect,url_for,send_file
from algorithms import *
import time
import matplotlib
import io
import base64 
from random_array import generate_random_array
import matplotlib.pyplot
from io import BytesIO

matplotlib.use('agg')  # Use the 'agg' backend (non-interactive) for Matplotlib

#selection sort, insertion sort, and merge sort

app = Flask(__name__)
app.secret_key = 'sort_and_sort'  # Required for flash messages


# Function to measure execution time
def measure_execution_time(algorithm, arr, iterations=10):
    total_time = 0
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.perf_counter()
        sorted_arr=algorithm(arr_copy)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    return (total_time / iterations),sorted_arr
 
@app.route('/download-text', methods=['POST'])
def download_retrieved_text():
    retrieved_text = request.form['results']
    return send_file(BytesIO(retrieved_text.encode()), as_attachment=True, download_name='results.txt', mimetype='text/plain')


# Plot function
def plot_line_graph(input_sizes, execution_times, title):
# Plot function
    fig, ax = matplotlib.pyplot.subplots(figsize=(10, 8))
    for alg_name, times in execution_times.items():
        ax.plot(input_sizes, times, label=alg_name, marker='o')
    ax.set_xlabel('Input Size')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    buf = io.BytesIO()
    matplotlib.pyplot.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    matplotlib.pyplot.close(fig)
    return plot_url

def plot_bar_graph(execution_times):
     # Plot the execution times
    fig, ax = matplotlib.pyplot.subplots(figsize=(10, 8))
    ax.bar(execution_times.keys(), execution_times.values(), width=0.4)
    ax.set_title("Execution Time Comparison")
    ax.set_xlabel("Algorithm")
    ax.set_ylabel("Execution Time (seconds)")
    matplotlib.pyplot.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    matplotlib.pyplot.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    matplotlib.pyplot.close(fig)
    return plot_url

@app.route('/view-results', methods=['POST'])
def view_results():
    results = request.form.get('results')
    return render_template('view_results.html', results=results)


# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        iterations=1
        input_array_sizes=None
        input_array = None
        #validations
        execution_type = request.form.get('execution_type')

        if execution_type=='array':
            if 'array' in request.form and request.form['array']:
                input_array = list(map(int, request.form['array'].split(',')))
                provided_input="array provided : "+str(input_array)
            elif 'array_size' in request.form and request.form['array_size']:
                size=(int(request.form['array_size']))
                input_array= generate_random_array(size)
                provided_input=f"random array generated of length : {len(input_array)}"
            elif 'file' in request.files and request.files['file']:
                file = request.files['file']
                file_content = file.read().decode('utf-8')
                input_array = list(map(int, file_content.strip().split(',')))
                provided_input=f"file uploaded containing array of length : {len(input_array)}"
            else:
                flash("Please provide an input array or upload a file or choose array_sizes",'danger')
                return redirect(url_for('home')) 
        if execution_type=='comparison':#validation for input arrays
            if 'input_array_sizes' in request.form and request.form['input_array_sizes']:
                input_array_sizes = list(map(int, request.form['input_array_sizes'].split(',')))
                input_array_sizes=sorted(input_array_sizes)
                provided_input="multiple random generated array of sizes "+str(input_array_sizes)
            else:
                flash('Please fill the input sizes', 'danger')
                return redirect(url_for('home')) 

        if 'iterations' in request.form and request.form['iterations']: 
            iterations=(int(request.form['iterations']))
        
        selected_algorithms = request.form.getlist('algorithms')

        algorithms = {
            'merge_sort': merge_sort,
            'insertion_sort': insertion_sort,
            'selection_sort': selection_sort,
            'bubble_sort': bubble_sort,
            'quick_sort': quick_sort
        }
            # Define input sizes
        
        execution_times = {}
        algorithms_selected={}
        for name in selected_algorithms:
            algorithms_selected[name] = algorithms[name]
        results=""
        if input_array is not None:
            results+=f"\n______________________________input array______________________________\n{input_array}\n"
            for alg_name,alg_func in algorithms_selected.items():
                avg_time,sorted_arr = measure_execution_time(alg_func, input_array,iterations)
                execution_times[alg_name] = avg_time
                results+=f"\n**************** {alg_name}  - execution time :{avg_time} *******************\n{sorted_arr}\n"
            plot_url=plot_bar_graph(execution_times)
        elif input_array_sizes is not None:
            execution_times = {alg_name: [] for alg_name in algorithms_selected.keys()}
            for size in input_array_sizes:
                generated_array = generate_random_array(size)
                results+=f"\n______________________________Generated Array Of Size : {size}______________________________\n{generated_array}\n"
                for alg_name, alg_func in algorithms_selected.items():
                    avg_time,sorted_arr = measure_execution_time(alg_func, generated_array,iterations)
                    execution_times[alg_name].append(avg_time)
                    results+=f"\n**************** {alg_name} - execution time :{avg_time} *******************\n{sorted_arr}\n"
                results+="\n\n"
            # Plotting 
            plot_url=plot_line_graph(input_array_sizes, execution_times, "Algorithm Performance vs Input Size")
        return render_template('result.html', plot_url=plot_url, execution_times=execution_times,results=results, input_array=provided_input,iterations=iterations)
    return render_template('index.html')




def run_flask_app():
    app.run(host='0.0.0.0',debug=True,)

if __name__ == '__main__':
    run_flask_app()