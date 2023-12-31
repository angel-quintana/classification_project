import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def prep_telco(df):
    '''
    input dataframe
    removes redundant cols (type_id's),
    fills blank spaces with 0.0 (total_charges)
    outputs clean dataframe
    '''
    df = df.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    df.internet_service_type = df.internet_service_type.fillna('None')
    
    return df

def encode_telco(df):
    '''
    input dataframe
    returns with encoded columns
    drops original string columns including customer_id
    outputs all numeric dataframe ready for models
    '''
    telco_p = df
    telco_p = telco_p.assign(sex_male = np.where(telco_p['gender'] == 'Male', 1, 0))
    telco_p = telco_p.assign(has_partner = np.where(telco_p['partner'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(has_dependents = np.where(telco_p['dependents'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(phone_serv = np.where(telco_p['phone_service'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(mult_lines = np.where(telco_p['multiple_lines'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(online_sec = np.where(telco_p['online_security'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(online_back = np.where(telco_p['online_backup'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(int_device_prot = np.where(telco_p['device_protection'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(int_tech_sup = np.where(telco_p['tech_support'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(int_tv_stream = np.where(telco_p['streaming_tv'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(int_movie_stream = np.where(telco_p['streaming_movies'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(paperless_bills = np.where(telco_p['paperless_billing'] == 'Yes', 1, 0))
    telco_p = telco_p.assign(churned = np.where(telco_p['churn'] == 'Yes', 1, 0))
    telco_p[['one_year_contract', 'two_year_contract']] = pd.get_dummies(telco_p.contract_type, drop_first=True).astype(int)
    telco_p = telco_p.assign(has_internet = np.where(telco_p['internet_service_type'] == 'None', 0, 1))
    telco_p = telco_p.assign(has_fiber = np.where(telco_p['internet_service_type'] == 'Fiber optic', 1, 0))
    telco_p = telco_p.assign(auto_bank_payment = np.where(telco_p['payment_type'] == 'Bank transfer (automatic)', 1, 0))
    telco_p = telco_p.assign(auto_credit_payment = np.where(telco_p['payment_type'] == 'Credit card (automatic)', 1, 0))
    telco_p = telco_p.assign(elec_check_payment = np.where(telco_p['payment_type'] == 'Electronic check', 1, 0))
    telco_p = telco_p.assign(mail_check_payment = np.where(telco_p['payment_type'] == 'Mailed check', 1, 0))
    
    columns=telco_p.select_dtypes('object').columns
    df_encoded = telco_p.drop(columns=columns)
    
    return df_encoded



def splitting_data(df, col):
    '''
    input dataframe and target variable to stratify on
    returns 3 dataframes serving as train, validate, and test samples
    '''

    #first split
    train, validate_test = train_test_split(df,
                     train_size=0.6,
                     random_state=123,
                     stratify=df[col]
                    )
    
    #second split
    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=123,
                                      stratify=validate_test[col]
                        
                                     )
    return train, validate, test

def compute_class_metrics(y_train, y_pred):
    '''
    input y_train and y_pred to return evaluation stats
    '''
    
    counts = pd.crosstab(y_train, y_pred)
    TP = counts.iloc[1,1]
    TN = counts.iloc[0,0]
    FP = counts.iloc[0,1]
    FN = counts.iloc[1,0]
    
    
    all_ = (TP + TN + FP + FN)

    accuracy = (TP + TN) / all_

    TPR = recall = TP / (TP + FN)
    FPR = FP / (FP + TN)

    TNR = TN / (FP + TN)
    FNR = FN / (FN + TP)

    precision =  TP / (TP + FP)
    f1 =  2 * ((precision * recall) / ( precision + recall))

    support_pos = TP + FN
    support_neg = FP + TN
    
    print(f"Accuracy: {accuracy}\n")
    print(f"True Positive Rate/Sensitivity/Recall/Power: {TPR}")
    print(f"False Positive Rate/False Alarm Ratio/Fall-out: {FPR}")
    print(f"True Negative Rate/Specificity/Selectivity: {TNR}")
    print(f"False Negative Rate/Miss Rate: {FNR}\n")
    print(f"Precision/PPV: {precision}")
    print(f"F1 Score: {f1}\n")
    print(f"Support (0): {support_pos}")
    print(f"Support (1): {support_neg}")