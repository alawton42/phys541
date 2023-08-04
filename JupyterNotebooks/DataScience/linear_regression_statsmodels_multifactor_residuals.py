import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# Get the data
advert = pd.read_csv('advertising.csv')
print(advert.head())

fig, ax = plt.subplots(1, figsize=(8,8))
fig.suptitle("Effects of Advertising on Sales - Residual Plot")

# Fit a linear regression models to different combinations of parameters
model1 = smf.ols('Sales ~ TV', data=advert)
model1 = model1.fit()
model2 = smf.ols('Sales ~ TV + Radio', data=advert)
model2 = model2.fit()
model3 = smf.ols('Sales ~ TV + Radio + Newspaper', data=advert)
model3 = model3.fit()

# View model summary
print(model3.summary())

# Predict values
sales_pred1 = model1.predict()
resid1 = advert['Sales'] - sales_pred1
sales_pred2 = model2.predict()
resid2 = advert['Sales'] - sales_pred2
sales_pred3 = model3.predict()
resid3 = advert['Sales'] - sales_pred3

# Plot regression against actual data
ax.hist(resid1, color = "blue", ec="white", bins=50, label='Sales ~ TV')           # histogram of residuals
ax.hist(resid2, color = "yellow", ec="blue", bins=50, label='Sales ~ TV + Radio')           # histogram of residuals
ax.hist(resid3, color = "lightblue", ec="yellow", bins=50, label='Sales ~ TV + Radio + Newspaper')           # histogram of residuals

plt.legend()
plt.show()