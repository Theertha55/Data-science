import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("Iris.csv")
print(data.head())
print()

X = data.iloc[:, :-1]
print(X.head())
print()

y = data.iloc[:, -1]
print(y.head())
print()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)
print(X_train.head())
print()
print(X_test.head())
print()


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print("array", y_pred)
print()
print(y_test.to_numpy())
print()

cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)

print(f"\nConfusion Matrix:\n{cm}")
print(f"\nAccuracy Score: {ac}")