import pandas as pd
#dtype={'YearsCoding': numpy.integer}
data = pd.read_csv('../database/survey_results_public.csv')
print(data['YearsCodingProf'].value_counts())


#print(data['YearsCodingProf'].value_counts())

summary = data['YearsCodingProf'].value_counts()
#print(summary["3-5 years"])