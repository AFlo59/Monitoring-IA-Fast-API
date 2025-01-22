import pandas as pd
from evidently.report import Report
from evidently.metrics import DataDriftMetric
from evidently.metrics import ColumnMapping

# 1) Chargement des données
reference = pd.read_csv("data/reference_data.csv")
production = pd.read_csv("data/production_data.csv")  # À adapter: test_data ou prod_data

column_mapping = ColumnMapping(
    target="target",
    numerical_features=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]
    # ou selon vos colonnes réelles ...
)

# 2) Configuration d'un report
data_drift_report = Report(metrics=[DataDriftMetric()])

# 3) Génération du report
data_drift_report.run(reference_data=reference, current_data=production, column_mapping=column_mapping)

# 4) Export
data_drift_report.save_html("reports/drift_report.html")
print("Rapport de data drift généré : reports/drift_report.html")