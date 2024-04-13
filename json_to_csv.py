import json
import pandas as pd

match_id_map = {}
with open('t20_json_files/t20_wc_match_results.json') as f:
    data=json.load(f)
# print(data)

df_match=pd.DataFrame(data[0]['matchSummary'])

with open('t20_json_files/t20_wc_batting_summary.json') as f:
    data=json.load(f)

    all_records=[]

    for rec in data:
        all_records.extend(rec['battingSummary'])

df_batting=pd.DataFrame(all_records)
# print(df_batting)
df_batting["out/not_out"]=df_batting.dismissal.apply(lambda x:'out' if len(x)>1 else 'not_out')
df_batting.drop(columns=['dismissal'],inplace=True) 
# df_batting['batsmanName']=df_batting['batsmanName'].apply(lambda x: x.replace(''))
# print(df_batting.head(11))
df_match=df_match.rename(columns={'scorecard':'match_id'})
for index,row in df_match.iterrows():
    key1=row['team1'] + ' Vs '+row['team2']
    key2=row['team2'] + ' Vs '+row['team1']
    match_id_map[key1]=row['match_id']
    match_id_map[key2]=row['match_id']
# print(match_id_map)
# print(df_match.head())
df_batting['match_id']=df_batting['match'].map(match_id_map)
# print(df_batting)
# df_batting.to_csv("t20_csv_files/fact_batting_summary.csv",index=False)

with open('t20_json_files/t20_wc_bowling_summary.json') as f:
    data=json.load(f)

    all_records=[]

    for rec in data:
        all_records.extend(rec['bowlingSummary'])

df_bowling=pd.DataFrame(all_records)
# print(df_bowling)
df_bowling["match_id"]=df_bowling['match'].map(match_id_map)
# print(df_bowling)
df_batting.to_csv("t20_csv_files/fact_bowling_summary.csv",index=False)

with open('t20_json_files/t20_wc_player_info.json') as f:
    data=json.load(f)

    # all_records=[]
    # for rec in data:
    #     all_records.extend(rec)

df_player=pd.DataFrame(data)
# print(df_player)
df_player.to_csv("t20_csv_files/dim_player_no_images.csv",index=False)
df_match.to_csv("t20_csv_files/dim_match_summary.csv",index=False)