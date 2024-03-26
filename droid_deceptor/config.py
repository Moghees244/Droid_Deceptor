class Config:
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///droid_deceptor.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "verysecurekey"
    JWT_TOKEN_LOCATION = "cookies"
    JWT_COOKIE_CSRF_PROTECT = False


class Paths:
    # Paths
    manifest_features_file_path = 'droid_deceptor/public/features/manifest_features.txt'
    api_calls_file_path = 'droid_deceptor/public/features/api_calls.txt'

    jadx_apk_path = '/home/blackcat/FYP/FYP_Code/FYP_Droid_Deceptor/droid_deceptor/uploads'
    jadx_output_path = '/home/blackcat/FYP/FYP_Code/FYP_Droid_Deceptor/droid_deceptor/outputs'

    apks_path = 'droid_deceptor/uploads/'
    source_code_path = 'droid_deceptor/outputs/'

    DECISION_TREE_PATH = 'droid_deceptor/public/malware_classifiers/decision_trees.pkl'
    KNN_PATH = 'droid_deceptor/public/malware_classifiers/knn.pkl'
    LOGISTIC_REGRESSION_PATH = 'droid_deceptor/public/malware_classifiers/logistic_regression.pkl'
    RANDOM_FORESTS_PATH = 'droid_deceptor/public/malware_classifiers/random_forests.pkl'
    SVM_PATH = 'droid_deceptor/public/malware_classifiers/svm.pkl'