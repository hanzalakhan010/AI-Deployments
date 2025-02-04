from joblib import load
model = load('./models/model_v1.joblib')
import numpy as np
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
    prediction = model.predict(X)[0].strip()
    reasons = rejectionReasons(X)
    return prediction
    
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
    rejection_reasons = shap_df.sort_values(by="shap_effect").head(10)
    reasons = []
    for idx, row in rejection_reasons.iterrows():
        reasons.append(f"{row['feature']}: {row['shap_effect']:.2f}")
    print(reasons)

