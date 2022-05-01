# AlphaPred
Machine learning-based classifier pipeline (AlphaPred) that differentiates between normal individuals and alpha thalassemia carriers. First model classfies between normals and alpha thalassemia carriers, and second classifies alpha carriers into alpha thalassemia traits and silent carriers, latter being the clinically milder condition.
URL of the web application built out of model 1 : https://alphaphred.herokuapp.com/

Image below depicts the structure and function of AlphaPred:
![Alphapred figure](Alphapred.png)

Following abstract of the research will provide a summmary of the work done :

**Background**
An effective screening program to detect Thalassemia carriers is a vital part of Thalassemia prevention. There are many challenges to an effective screening program, especially in low-resource settings. Considering alpha-thalassemia, genetic testing is needed for a confirmatory diagnosis of a carrier, which is expensive and not widely available. Machine learning (ML) models can act as decision-support tools that are easy to deploy and use in low-resource settings. 

**Aims**
This study attempted to apply modern machine learning algorithms to alpha-thalassemia screening data and develop a cost-effective and time-saving ML tool that can accurately predict the alpha thalassemia carrier state using simple blood tests. This tool can then be used in circumstances where there are constraints to genetic testing and can act as a complementary diagnostic tool that can identify high-risk individuals who need to undergo confirmatory genetic testing. 

**Methods**
Ethical clearance was obtained from the Ethics Review Committee of PGIM, University of Colombo. Three ML algorithms, XGBoost, random forest, and an Artificial Neural Network (ANN) were used to train two models using complete blood count and high-performance liquid chromatography data from a database of 288 cases from the Human Genetics Unit (HGU) of the Faculty of Medicine, Colombo. Each model differentiated between two diagnostic groups. Performances of the models were assessed using classification accuracy, Sensitivity, and AUC score of ROC. 

**Results**
Model 1 was trained to differentiate between alpha-thalassemia carriers and normal individuals, and the XGBoost outperformed others with an Accuracy of 83%, Sensitivity of 84% for Alpha carriers, and an AUC of 0.8. Model 2 differentiated between alpha-thalassemia silent carriers and alpha-thalassemia traits, and the XGboost algorithm again showed superior performance with an accuracy of 87%, Sensitivity of 89% for alpha thalassemia traits and an AUC of 0.84. Mean corpuscular volume (MCV) was the most helpful feature for Model 1, while mean corpuscular hemoglobin (MCH) was the most helpful feature for model 2, according to decision tree visualizations. A web application named ‘AlphaPred’ was developed, combining the two models. This could be used for further validation studies. 

**Conclusion**
AlphaPred can be used as a diagnostic tool in situations where there are constraints to genetic testing. Clinicians can then prioritize high-risk individuals that need genetic testing for confirmation. The tool needs further validation with a larger dataset, and a prospective trial, to be deployed in a real-world setting. 

