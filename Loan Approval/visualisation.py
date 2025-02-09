import pandas as pd
import plotly.express as px
from joblib import load


feature_importance = load('models/feaure_importance.joblib')


df = pd.read_csv('./datasets/loan_approval_dataset.csv')


fe = px.bar(
    feature_importance,
    y = 'Feature',
    x  = 'Importance',
    color='Feature',
    orientation='h',
)

grouped_self_employed = df.groupby([' self_employed',' loan_status'])[' loan_status'].size().reset_index(name = 'count')
grouped_no_of_dependents = df.groupby([' no_of_dependents',' loan_status'])[' loan_status'].size().reset_index(name = 'count')



grouped_self_employed_fig = px.bar(
    grouped_self_employed,
    x = ' self_employed',
    y = 'count',
    color = ' loan_status',
    title='Loan Approval Status by Employment Status',
    labels={"count":"Number of Applicants",' loan_status':'Loan Status',' self_employed':'Self Employed'},
    barmode='group',

    )


grouped_no_of_dependents_fig = px.bar(
    grouped_no_of_dependents,
    x = ' no_of_dependents',
    y = 'count',
    color = ' loan_status',
    title='Loan Approval Status by Number of dependents',
    labels={"count":"Number of Dependents",' loan_status':'Loan Status',' no_of_dependents':'No of dependents'},
    barmode='group',
    )


grouped_no_of_dependents_fig.write_html('./static/grouped_no_of_dependents.html')
grouped_self_employed_fig.write_html('./static/grouped_self_employed.html')

fe.write_html('./static/feature_importances.html')

