import pandas as pd
import plotly.express as px

df = pd.read_csv('./datasets/loan_approval_dataset.csv')

grouped = df.groupby([' loan_status',' self_employed'])[' loan_status'].size().reset_index(name = 'count')

fig = px.bar(
    grouped,x = ' loan_status',
    y = 'count',
    color = ' loan_status',
    title='Loan Approval Status by Employment Status',
    labels={"count":"Number of Applicants",' loan_status':'Loan Status'},
    barmode='group',

    )

    
fig.write_html('first_figure.html', auto_open=True)

