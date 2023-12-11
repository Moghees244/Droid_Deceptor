class Config:
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///droid_deceptor.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "verysecurekey"
    JWT_TOKEN_LOCATION = "cookies"

class Paths:
    # Paths
    manifest_features_file_path = 'droid_deceptor/public/features/manifest_features.txt'
    api_calls_file_path = 'droid_deceptor/public/features/api_calls.txt'

    apks_path = 'droid_deceptor/uploads/'
    source_code_path = 'droid_deceptor/outputs/'