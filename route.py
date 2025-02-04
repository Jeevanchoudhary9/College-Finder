from app import app
from flask import redirect,render_template, request, flash
import pandas as pd

@app.route('/')
def index():
    # return render_template('layout.html',nav="")
    return render_template('Dashboard.html',nav="dashboard")

@app.route('/data')
def data():
    df= pd.read_csv('data.csv', sep=',')
     
    # Convert the DataFrame to an HTML table
    table_html = df.to_html(classes='table table-striped', index=False)
    
    # Return the HTML table as the response
    return table_html

@app.route('/all_colleges')
def all_colleges():
    df= pd.read_csv('data.csv', sep=',')
    
    return render_template('all_colleges.html',nav='All Colleges')

@app.route('/submit_rank', methods=['POST'])
def submit_rank():
    rank = request.form.get('rank')
    if rank == '':
        return redirect('/')
    else:
        try:
            rank = int(rank)
        except:
            flash('Please enter a valid rank')
            return redirect('/')
        
        df= pd.read_csv('data.csv', sep=',')

        # Sort the DataFrame by 'GOPEN' in descending order
        df_sorted = df.sort_values(by="GOPEN", ascending=False).reset_index(drop=True)

        # Filter rows with GOPEN >= rank
        above_rank = df_sorted[df_sorted["GOPEN"] >= rank].tail(10)
        print(rank)
        print(above_rank)

        # Find 10 rows just below the rank
        below_rank = df_sorted[df_sorted["GOPEN"] < rank]

        # Combine the results
        result = pd.concat([above_rank, below_rank]).reset_index(drop=True)


        print(df.head())

        return result.to_html(classes='table table-striped', index=False)
