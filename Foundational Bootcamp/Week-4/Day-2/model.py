from __future__ import annotations

import os
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

warnings.filterwarnings("ignore")
sns.set_style("darkgrid")

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "framingham.xls"
IMAGE_FILE = BASE_DIR / "Capture.PNG"


def calculate_sigmoid(log_odds: float) -> float:
    return np.exp(log_odds) / (np.exp(log_odds) + 1)


def show_image(path: Path) -> None:
    if path.exists():
        plt.figure(figsize=(12, 10))
        plt.imshow(plt.imread(path))
        plt.axis("off")
        plt.show()


def main() -> None:
    for dirname, _, filenames in os.walk(BASE_DIR):
        for filename in filenames:
            print(os.path.join(dirname, filename))

    show_image(IMAGE_FILE)
    show_image(IMAGE_FILE)
    show_image(IMAGE_FILE)

    odds_of_rain = 0.4 / 0.6
    print("odds of rain:", odds_of_rain)

    log_odds_of_rain = np.log(0.4 / 0.6)
    print("log odds of rain:", log_odds_of_rain)

    odds_on_time = 0.9 / 0.1
    print("odds of time:", odds_on_time)

    log_odds_on_time = np.log(odds_on_time)
    print("log odds of rain:", log_odds_on_time)

    print(calculate_sigmoid(log_odds_of_rain))
    print(calculate_sigmoid(log_odds_on_time))

    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find dataset at {DATA_FILE}")

    df = pd.read_excel(DATA_FILE)
    print(df.head())
    print(df.info())
    print(df.describe(include="all").transpose())
    print(df.corr(numeric_only=True)["TenYearCHD"].sort_values(ascending=False))

    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(25, 20))
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(corr, cmap="jet", annot=True, linewidths=0, linecolor="white", cbar=True, mask=mask)
    plt.show()

    labels = ["Heart Disease", "Healthy"]
    sizes = [df.loc[df["TenYearCHD"] == 1, "TenYearCHD"].count(), df.loc[df["TenYearCHD"] == 0, "TenYearCHD"].count()]
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    ax1.pie(sizes, explode=(0, 0.1), labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    plt.title("Proportion of Heart Disease and Healthy", size=20)
    plt.show()

    plt.figure(figsize=(15, 10))
    sns.countplot(x="male", hue="TenYearCHD", data=df, palette="Set1")
    plt.title("The Counts of Heart Disease by Male")
    plt.show()

    plt.figure(figsize=(15, 10))
    sns.countplot(x="prevalentHyp", hue="TenYearCHD", data=df, palette="Set2")
    plt.title("The Counts of Heart Disease by Systolic Blood Pressure")
    plt.show()

    try:
        import plotly.graph_objects as go

        education_values = df["education"].value_counts().sort_index()
        fig = go.Figure(data=[go.Pie(labels=education_values.index.astype(str), values=education_values.values, hole=0.3)])
        fig.update_layout(title_text="<b>Education</b>")
        fig.show()
    except Exception as error:
        print(f"Plotly chart skipped: {error}")

    sns.kdeplot(x="diaBP", data=df, hue="TenYearCHD", fill=True)
    plt.ylabel("Density")
    plt.xlabel("Diastolic blood pressure")
    plt.title("Distribution of diastolic blood pressure by Heart Disease")
    plt.show()

    sns.kdeplot(x="sysBP", data=df, hue="TenYearCHD", fill=True)
    plt.ylabel("Density")
    plt.xlabel("Systolic blood pressure")
    plt.title("Distribution of systolic blood pressure by Heart Disease")
    plt.show()

    print(df.isnull().sum().sort_values(ascending=False))

    for column in ["glucose", "education", "BPMeds", "totChol", "cigsPerDay", "BMI", "heartRate"]:
        print("Column:", column)
        print(df[column].nunique())
        print("******************************")

    fill_values = {
        "glucose": df["glucose"].mean(),
        "totChol": df["totChol"].mean(),
        "cigsPerDay": df["cigsPerDay"].mean(),
        "BMI": df["BMI"].mean(),
        "heartRate": df["heartRate"].mean(),
        "education": df["education"].median(),
        "BPMeds": df["BPMeds"].median(),
    }
    for column, value in fill_values.items():
        df[column] = df[column].fillna(value)

    print(df.isnull().sum().sort_values(ascending=False))

    from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier, VotingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, log_loss
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC

    scaler = StandardScaler()
    scaled_columns = ["cigsPerDay", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose", "age"]
    df[scaled_columns] = scaler.fit_transform(df[scaled_columns])
    print(df.head(3))

    X = df.drop("TenYearCHD", axis=1)
    y = df["TenYearCHD"]
    print(X.columns)
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    print(model.coef_)
    print(model.intercept_)

    predictions = model.predict(X_test)
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))
    print(accuracy_score(y_test, predictions))

    forest = RandomForestClassifier(random_state=42)
    forest.fit(X_train, y_train)
    predictions2 = forest.predict(X_test)
    print(confusion_matrix(y_test, predictions2))
    print(classification_report(y_test, predictions2))
    print(accuracy_score(y_test, predictions2))

    random_grid = {
        "n_estimators": [int(x) for x in np.linspace(start=100, stop=1200, num=12)],
        "max_features": ["sqrt", "log2"],
        "max_depth": [int(x) for x in np.linspace(5, 30, num=6)],
        "min_samples_split": [2, 5, 10, 15, 100],
        "min_samples_leaf": [1, 2, 5, 10],
    }
    print(random_grid)

    search = RandomizedSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_distributions=random_grid,
        n_iter=10,
        cv=5,
        verbose=2,
        random_state=42,
        n_jobs=1,
    )
    search.fit(X_train, y_train)
    print(search.best_params_)
    print(search.best_score_)

    predictions3 = search.predict(X_test)
    print(confusion_matrix(y_test, predictions3))
    print(classification_report(y_test, predictions3))
    print(accuracy_score(y_test, predictions3))

    error_rate = []
    for neighbor_count in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=neighbor_count)
        knn.fit(X_train, y_train)
        prediction_i = knn.predict(X_test)
        error_rate.append(np.mean(prediction_i != y_test))

    plt.figure(figsize=(15, 10))
    plt.plot(range(1, 40), error_rate, color="blue", linestyle="--", marker="o", markerfacecolor="red", markersize=10)
    plt.title("Error Rate vs K Value")
    plt.xlabel("K Value")
    plt.ylabel("Error Rate")
    plt.show()

    knn = KNeighborsClassifier(n_neighbors=27)
    knn.fit(X_train, y_train)
    predictions4 = knn.predict(X_test)
    print(confusion_matrix(y_test, predictions4))
    print(classification_report(y_test, predictions4))
    print(accuracy_score(y_test, predictions4))

    param_grid = {"C": [1, 2, 3, 4, 5, 10, 100], "gamma": [1, 0.1, 0.2, 0.5, 0.01, 0.001, 0.0001]}
    grid = GridSearchCV(SVC(probability=True), param_grid, verbose=2)
    grid.fit(X_train, y_train)
    print(grid.best_params_)
    print(grid.best_estimator_)

    grid_predictions = grid.predict(X_test)
    print(confusion_matrix(y_test, grid_predictions))
    print(classification_report(y_test, grid_predictions))
    print(accuracy_score(y_test, grid_predictions))

    clf1 = KNeighborsClassifier(n_neighbors=27)
    clf2 = RandomForestClassifier(
        n_estimators=700,
        min_samples_split=15,
        min_samples_leaf=1,
        max_features="sqrt",
        max_depth=20,
        random_state=42,
    )
    clf3 = AdaBoostClassifier(random_state=42)
    eclf1 = VotingClassifier(estimators=[("knc", clf1), ("rfc", clf2), ("abc", clf3)], voting="soft")
    eclf1.fit(X_train, y_train)
    ensemble_predictions = eclf1.predict(X_test)
    print("Final Accuracy Score")
    print(confusion_matrix(y_test, ensemble_predictions))
    print(classification_report(y_test, ensemble_predictions))
    print(accuracy_score(y_test, ensemble_predictions))

    clf1 = GradientBoostingClassifier(random_state=42)
    clf2 = LogisticRegression(max_iter=1000)
    clf3 = AdaBoostClassifier(random_state=42)
    eclf1 = VotingClassifier(estimators=[("gbc", clf1), ("lr", clf2), ("abc", clf3)], voting="soft")
    eclf1.fit(X_train, y_train)
    ensemble_predictions = eclf1.predict(X_test)
    print("Final Accuracy Score")
    print(accuracy_score(y_test, ensemble_predictions))
    print(confusion_matrix(y_test, ensemble_predictions))
    print(classification_report(y_test, ensemble_predictions))

    try:
        import xgboost as xgb

        xgb_model = xgb.XGBClassifier(
            learning_rate=0.1,
            max_depth=20,
            min_child_weight=30,
            n_estimators=20,
            eval_metric="logloss",
        )
        xgb_model.fit(X_train, y_train)
        xgb_predictions = xgb_model.predict(X_test)
        xgb_probabilities = xgb_model.predict_proba(X_test)
        print(log_loss(y_test, xgb_probabilities))
        print(confusion_matrix(y_test, xgb_predictions))
        print(classification_report(y_test, xgb_predictions))
        print(accuracy_score(y_test, xgb_predictions))
    except Exception as error:
        print(f"XGBoost skipped: {error}")


if __name__ == "__main__":
    main()
