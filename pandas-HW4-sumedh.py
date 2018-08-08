#create age parameters - 4 year length
#create dataframe of unique players in each age group, find percentage against full count of players

tenyears = df[df["Age"] <10]
loteens = df[(df["Age"] >=10) & (df["Age"] <=14)]
hiteens = df[(df["Age"] >=15) & (df["Age"] <=19)]
lotwent = df[(df["Age"] >=20) & (df["Age"] <=24)]
hitwent = df[(df["Age"] >=25) & (df["Age"] <=29)]
lothirt = df[(df["Age"] >=30) & (df["Age"] <=34)]
hithirt = df[(df["Age"] >=35) & (df["Age"] <=39)]
loforty = df[(df["Age"] >=40) & (df["Age"] <=44)]
hiforty = df[(df["Age"] >=45) & (df["Age"] <=49)]

age_demo_df = pd.DataFrame({"Age": ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49"],
                       "Percentage of Players": [(tenyears["SN"].nunique()/fullcount)*100, (loteens["SN"].nunique()/fullcount)*100, (hiteens["SN"].nunique()/fullcount)*100, (lotwent["SN"].nunique()/fullcount)*100, (hitwent["SN"].nunique()/fullcount)*100, (lothirt["SN"].nunique()/fullcount)*100, (hithirt["SN"].nunique()/fullcount)*100, (loforty["SN"].nunique()/fullcount)*100, (hiforty["SN"].nunique()/fullcount)*100],
                       "Total Count": [tenyears["SN"].nunique(), loteens["SN"].nunique(), hiteens["SN"].nunique(), lotwent["SN"].nunique(), hitwent["SN"].nunique(), lothirt["SN"].nunique(), hithirt["SN"].nunique(), loforty["SN"].nunique(), hiforty["SN"].nunique()]
                      })

age_demo_final = age_demo_df.set_index("Age")
age_demo_final.style.format({"Percentage of Players": "{:.2f}%"})
In [64]:
age_purchasing_df = pd.DataFrame({"Age": ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49"],
                             "Purchase Count": [tenyears["Price"].count(), loteens["Price"].count(), hiteens["Price"].count(), lotwent["Price"].count(), hitwent["Price"].count(), lothirt["Price"].count(), hithirt["Price"].count(), loforty["Price"].count(), hiforty["Price"].count()],
                             "Average Purchase Price": [tenyears["Price"].mean(), loteens["Price"].mean(), hiteens["Price"].mean(), lotwent["Price"].mean(), hitwent["Price"].mean(), lothirt["Price"].mean(), hithirt["Price"].mean(), loforty["Price"].mean(), hiforty["Price"].mean()],
                             "Total Purchase Value": [tenyears["Price"].sum(), loteens["Price"].sum(), hiteens["Price"].sum(), lotwent["Price"].sum(), hitwent["Price"].sum(), lothirt["Price"].sum(), hithirt["Price"].sum(), loforty["Price"].sum(), hiforty["Price"].sum()],
                             "Normalized Totals": [tenyears["Price"].sum()/tenyears['SN'].nunique(), loteens["Price"].sum()/loteens['SN'].nunique(), hiteens["Price"].sum()/hiteens['SN'].nunique(),
                                                   lotwent["Price"].sum()/lotwent['SN'].nunique(), hitwent["Price"].sum()/hitwent['SN'].nunique(),
                                                   lothirt["Price"].sum()/lothirt['SN'].nunique(), hithirt["Price"].sum()/hithirt['SN'].nunique(),
                                                   loforty["Price"].sum()/loforty['SN'].nunique(), hiforty["Price"].sum()/hiforty['SN'].nunique()]},
                            columns =
                           ["Age", "Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"])

age_purchasing_final = age_purchasing_df.set_index("Age")

age_purchasing_final.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}", "Normalized Totals": "${:.2f}"})
Top Spenders
In [63]:
sn_total_purchase = df.groupby('SN')['Price'].sum().to_frame()
sn_purchase_count = df.groupby('SN')['Price'].count().to_frame()
sn_purchase_avg = df.groupby('SN')['Price'].mean().to_frame()

sn_total_purchase.columns=["Total Purchase Value"]
join_one = sn_total_purchase.join(sn_purchase_count, how="left")
join_one.columns=["Total Purchase Value", "Purchase Count"]

join_two = join_one.join(sn_purchase_avg, how="inner")
join_two.columns=["Total Purchase Value", "Purchase Count", "Average Purchase Price"]

top_spenders_df = join_two[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]
top_spenders_final = top_spenders_df.sort_values('Total Purchase Value', ascending=False).head()
top_spenders_final.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})