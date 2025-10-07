import json
fname='data.json'
with open(fname,'r') as f:
    json.load(f)
with open(fname,'r') as f:
    js=json.load(f)
js.keys()
js[:5]
import pandas as pd
df = pd.read_json(json_str)
df = pd.read_json(js)
with open(fname,'r') as f:
    js=json.loads(f)
df = pd.read_json(''.join(js))
df = pd.read_json(f"[{''.join(js)}]")
with open(fname,'r') as f:
    df=pd.read_json(json.loads(f))
with open(fname,'r') as f:
    df=pd.read_json(f)
df.head()
parks={i:j for i,j in enumerate(list(set(df.工業區名稱)))}
parks={j:f"園區{i}" for i,j in enumerate(list(set(df.工業區名稱)))}
cntys={j:f"縣市{i}" for i,j in enumerate(list(set(df.縣市別)))}
waste={j:f"廢棄物種類{i}" for i,j in enumerate(list(set(df.廢棄物名稱)))}
paths={j:f"申報途徑{i}" for i,j in enumerate(list(set(df.)))}
paths={j:f"申報途徑{i}" for i,j in enumerate(list(set(df.申報途徑)))}
years={j:f"年度{i}" for i,j in enumerate(list(set(df.year)))}
df.year=[years[i] for i in df.year]
df.head()
df.工業區名稱=[parks[i] for i in df.工業區名稱]
df.縣市別=[cntys[i] for i in  df.縣市別]
df.廢棄物名稱=[waste[i] for i in in df.廢棄物名稱]
df.廢棄物名稱=[waste[i] for i in df.廢棄物名稱]
df.申報途徑=[paths[i] for i in df.申報途徑]
df.head()
df.to_json('data.json', orient='records', lines=False, force_ascii=False, indent=2)
history

