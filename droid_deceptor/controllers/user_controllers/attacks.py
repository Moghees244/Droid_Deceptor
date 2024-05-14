import math
import random
import numpy as np

class Attacks:
    def __init__(self):
        self.apk_vector = None
        self.model = None

    
    def jsma_attack(self, max_perturbations):
        print("JSMA ATTACK")
        original_class = self.initial_data()
        # Create a copy of the APK vector for manipulation
        adversarial_example = self.apk_vector.copy()
        
        # Attack
        delta_x = 0
        while self.model(adversarial_example)[0] == original_class and delta_x < max_perturbations:
            gradients = self.forward_derivative(adversarial_example)
            # feature with largest impact
            i_max = np.argmax(gradients)
            # Adding perturbation (only add feature dont remove any so the apk remains functional)
            adversarial_example[0][i_max] = 1
            # calculating the total perturbations added
            difference = np.abs(adversarial_example - self.apk_vector)
            delta_x = np.sum(difference)
            # if perturbations limit is exceded
            if delta_x > max_perturbations:
                print("Perturbations Limit Reached. Attack Failed!")
                return None
        # Results
        self.results(adversarial_example) 
        print("Perturbations Added : ", delta_x)
        return adversarial_example
    
    def forward_derivative(self, vector):
        gradients = []
        # calculating effect of each feature and storing it 
        for i in range(len(vector[0])):
            # if we change this feature to 0, apk will not function properly
            if vector[0][i] == 1:
                gradients.append(-1)
            # adding a new feature to the apk and checking its impact on classification result
            else:
                vector[0][i] = 1
                _, gradient = self.model(vector)
                vector[0][i] = 0
                gradients.append(gradient[0][0])
        return gradients
    
    
    def initial_data(self):
        print("Initial APK Vector:")
        print(self.apk_vector)

        # initial classifier result and probabilities
        original_class, original_prob = self.model(self.apk_vector)
        print("Initial Evaluation:")
        print("Classifier Result:", original_class)
        print("Classifier Probabilities:", original_prob)

        return original_class
    
    def results(self, adversarial_vector):
        print("Manipulated Vector:")
        print(adversarial_vector)

        # final classifier result and probabilities
        test_class, test_prob = self.model(adversarial_vector)
        print("Classifier Result:", test_class)
        print("Classifier Probabilities:", test_prob)
    
    def perturbations(self, adversarial_vector):
            difference = np.abs(adversarial_vector - self.apk_vector)
            delta_x = np.sum(difference)
            print("Perturbations Added : ", delta_x)

    
    def features_names(self, adversarial_vector):
        # Paths to features lists
        manifest_features_file_path = 'droid_deceptor/public/features/manifest_features.txt'
        api_calls_file_path = 'droid_deceptor/public/features/api_calls.txt'
        # all features extracted from apk
        manifest_features = get_feature_list(manifest_features_file_path)
        api_calls = get_feature_list(api_calls_file_path)
        all_features = manifest_features + api_calls

        # getting which features are added as perturbations
        features = []
        for i in range(len(adversarial_vector[0])):
            if adversarial_vector[0][i] == 1 and adversarial_vector[0][i] != self.apk_vector[0][i]:
                features.append(all_features[i])
        # returning all added features
        return features
    

# read all permissions from file and make a list of it
def get_feature_list(file_path):
    
    with open(file_path, "r") as features_file:
        features = features_file.readlines()
    features = [word.strip() for word in features]
    return features