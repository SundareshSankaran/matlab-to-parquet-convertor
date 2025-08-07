## Prompt

Given the jupyter notebook, I want to extract the code which creates two parquet files, and generalise it to run against all .mat files located in the mat_files folder. The parquet files should have the name of the original mat file and should have suffixes for data and summary fields (gleaned from the mat files)

Save this prompt and results in a markdown file under /Users/sinsrn/current_projects/matlab-convertor/build/prompts with a name pattern prefixed with sequence at which this prompt has been generated.

---

## Result

Below is a Python script that iterates over all `.mat` files in the `mat_files` folder, extracts the `data` and `summary` fields, processes them as in the notebook, and saves each as a parquet file with the original `.mat` filename and appropriate suffixes.

```python
import os
import glob
import scipy.io
import pandas as pd

mat_folder = "/Users/sinsrn/current_projects/matlab-convertor/mat_files"
output_folder = "/Users/sinsrn/current_projects/matlab-convertor/output_parquet"
os.makedirs(output_folder, exist_ok=True)

mat_files = glob.glob(os.path.join(mat_folder, "*.mat"))

for mat_file in mat_files:
    base_name = os.path.splitext(os.path.basename(mat_file))[0]
    mat_data = scipy.io.loadmat(mat_file)
    mat_data_2 = {k: v for k, v in mat_data.items() if not k.startswith('__')}

    # Process 'data' field
    if "data" in mat_data_2:
        df_1 = pd.DataFrame(mat_data_2["data"][0])
        # Flatten and expand columns as in notebook
        df_3 = pd.DataFrame()
        for col in ['system_time', 'relative_time_min','voltage_V', 'current_A',
                    'capacity_Ah', 'power_Wh', 'temperature_C']:
            df_3[col] = df_1[col].apply(lambda arr: arr.flatten())
        df_3['counter'] = range(len(df_3))
        df_expanded = df_3.apply(pd.Series.explode)
        # Description column
        desc_column = []
        for row in df_1.itertuples(index=False):
            desc = [row.description] * row.system_time.shape[0]
            desc_column.append(desc)
        desc_df = pd.DataFrame({"description": desc_column})
        desc_df_expanded = desc_df.apply(pd.Series.explode)
        df_1_new = pd.concat([df_expanded, desc_df_expanded], axis=1)
        # Set dtypes as in notebook
        df_1_new['system_time'] = df_1_new['system_time'].astype('string')
        df_1_new['relative_time_min'] = df_1_new['relative_time_min'].astype('float')
        df_1_new['voltage_V'] = df_1_new['voltage_V'].astype('float')
        df_1_new['current_A'] = df_1_new['current_A'].astype('float')
        df_1_new['capacity_Ah'] = df_1_new['capacity_Ah'].astype('float')
        df_1_new['power_Wh'] = df_1_new['power_Wh'].astype('float')
        df_1_new['temperature_C'] = df_1_new['temperature_C'].astype('float')
        df_1_new['description'] = df_1_new['description'].astype('string')
        df_1_new['counter'] = df_1_new['counter'].astype(int)
        # Save to parquet
        parquet_path = os.path.join(output_folder, f"{base_name}-data.parquet")
        df_1_new.to_parquet(parquet_path, engine="pyarrow")
        print(f"Saved {parquet_path}")

    # Process 'summary' field
    if "summary" in mat_data_2:
        df_2 = pd.DataFrame(mat_data_2["summary"][0])
        df_4 = pd.DataFrame()
        for col in ['charge_capacity_Ah','discharge_capacity_Ah','charge_power_Wh','discharge_power_Wh',
                    'charge_median_voltage','discharge_median_voltage','charge_mean_voltage','discharge_mean_voltage']:
            df_4[col] = df_2[col].apply(lambda arr: arr.flatten())
        df_expanded = df_4.apply(pd.Series.explode)
        # Description column
        desc_column = []
        for row in df_2.itertuples(index=False):
            desc = [row.description] * row.charge_capacity_Ah.shape[0]
            desc_column.append(desc)
        desc_df = pd.DataFrame({"description": desc_column})
        desc_df_expanded = desc_df.apply(pd.Series.explode)
        df_2_new = pd.concat([df_expanded, desc_df_expanded], axis=1)
        df_2_new['counter'] = range(len(df_2_new))
        # Set dtypes as in notebook
        df_2_new['charge_capacity_Ah'] = df_2_new['charge_capacity_Ah'].astype('float')
        df_2_new['discharge_capacity_Ah'] = df_2_new['discharge_capacity_Ah'].astype('float')
        df_2_new['charge_power_Wh'] = df_2_new['charge_power_Wh'].astype('float')
        df_2_new['discharge_power_Wh'] = df_2_new['discharge_power_Wh'].astype('float')
        df_2_new['charge_median_voltage'] = df_2_new['charge_median_voltage'].astype('float')
        df_2_new['discharge_median_voltage'] = df_2_new['discharge_median_voltage'].astype('float')
        df_2_new['charge_mean_voltage'] = df_2_new['charge_mean_voltage'].astype('float')
        df_2_new['discharge_mean_voltage'] = df_2_new['discharge_mean_voltage'].astype('float')
        df_2_new['description'] = df_2_new['description'].astype('string')
        df_2_new['counter'] = df_2_new['counter'].astype(int)
        # Save to parquet
        parquet_path = os.path.join(output_folder, f"{base_name}-summary.parquet")
        df_2_new.to_parquet(parquet_path, engine="pyarrow")
        print(f"Saved {parquet_path}")
```

This script will process all `.mat` files in the folder and create corresponding parquet files for both `data` and `summary` fields, named as `<matfilename>-data.parquet` and `<matfilename>