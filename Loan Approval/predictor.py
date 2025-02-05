from joblib import load
model = load('./models/model_v1.joblib')
import numpy as np
from json import loads
import shap
import pandas as pd

def prediction(data):
    X = [
            int(data.get('no_of_dependents')),
            int(data.get('income_annum'))*1000,
            int(data.get('loan_amount'))*1000,
            int(data.get('loan_term')),
            int(data.get('cibil_score')),
            int(data.get('residential_assets_value'))*1000,
            int(data.get("commercial_assets_value"))*1000,
            int(data.get('luxury_assets_value'))*1000,
            int(data.get('bank_asset_value'))*1000,
            True if data.get('self_employed') == 'self_employed_yes' else False,
            True if data.get('education') == 'ngraduated' else False
        ]
    X = np.array(X).reshape(1,-1)
    probab = model.predict_proba(X)
    prediction = model.predict(X)[0].strip()
    # print(probab)
    if prediction =='Rejected':
        explanations = rejectionReasons(X)
        probability = probab[0][1]*100
        return {"prediction":prediction,"probab":probability,"explanations":explanations}
    else:
        probability = probab[0][0]*100
        return {"prediction":prediction,"probab":probability}
    
def rejectionExplainer(reasons):
    explanations = []
    with open('explanations.json') as explanationsFile:
        explanations_dict = loads(explanationsFile.read()).get('explanations')
        for reason in reasons:
            # print(reason)
            explanations.append({"reason":reason,**explanations_dict.get(reason)})
    return explanations
def rejectionReasons(applicant_data):
    explainer = shap.TreeExplainer(model)
    shap_single = explainer.shap_values(applicant_data)
    feature_names = [' no_of_dependents', ' education', ' self_employed',
       ' income_annum', ' loan_amount', ' loan_term', ' cibil_score',
       ' residential_assets_value', ' commercial_assets_value',
       ' luxury_assets_value', ' bank_asset_value']
    shap_df = pd.DataFrame(
        {
            "feature" :feature_names,
            "shap_effect":shap_single[0]
        }
    ) 
    rejection_reasons = shap_df.sort_values(by="shap_effect").head(3)
    reasons = []
    for idx, row in rejection_reasons.iterrows():
        reasons.append(row['feature'])
    # for idx, row in rejection_reasons.iterrows():
    #     reasons.append(f"{row['feature']}: {row['shap_effect']:.2f}")
    # print(reasons)
    explaination = rejectionExplainer(reasons=list(reasons))
    return explaination

