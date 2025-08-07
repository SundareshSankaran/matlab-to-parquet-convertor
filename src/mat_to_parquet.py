# mat_to_parquet.py
# This script processes .mat files and converts them to Parquet format.

## Imports

import os
import glob
import shutil
import scipy.io
import pandas as pd

# Function to process .mat files and save as Parquet
def process_mat_files(mat_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    done_folder = os.path.join(mat_folder, "done")
    os.makedirs(done_folder, exist_ok=True)

    # --- New: Move existing parquet files to output_parquet/done before processing ---
    output_done_folder = os.path.join(output_folder, "done")
    os.makedirs(output_done_folder, exist_ok=True)
    existing_parquet_files = glob.glob(os.path.join(output_folder, "*.parquet"))
    for pq_file in existing_parquet_files:
        shutil.move(pq_file, os.path.join(output_done_folder, os.path.basename(pq_file)))
        print(f"Moved existing parquet file {pq_file} to {output_done_folder}")

    mat_files = glob.glob(os.path.join(mat_folder, "*.mat"))

    for mat_file in mat_files:
        base_name = os.path.splitext(os.path.basename(mat_file))[0]
        mat_data = scipy.io.loadmat(mat_file)
        mat_data_2 = {k: v for k, v in mat_data.items() if not k.startswith('__')}

        data_success = False
        summary_success = False

        # Process 'data' field
        if "data" in mat_data_2:
            df_1 = pd.DataFrame(mat_data_2["data"][0])
            df_3 = pd.DataFrame()
            for col in ['system_time', 'relative_time_min','voltage_V', 'current_A',
                        'capacity_Ah', 'power_Wh', 'temperature_C']:
                df_3[col] = df_1[col].apply(lambda arr: arr.flatten())
            df_3['counter'] = range(len(df_3))
            df_expanded = df_3.apply(pd.Series.explode)
            desc_column = []
            for row in df_1.itertuples(index=False):
                desc = [row.description] * row.system_time.shape[0]
                desc_column.append(desc)
            desc_df = pd.DataFrame({"description": desc_column})
            desc_df_expanded = desc_df.apply(pd.Series.explode)
            df_1_new = pd.concat([df_expanded, desc_df_expanded], axis=1)
            df_1_new['system_time'] = df_1_new['system_time'].astype('string')
            df_1_new['relative_time_min'] = df_1_new['relative_time_min'].astype('float')
            df_1_new['voltage_V'] = df_1_new['voltage_V'].astype('float')
            df_1_new['current_A'] = df_1_new['current_A'].astype('float')
            df_1_new['capacity_Ah'] = df_1_new['capacity_Ah'].astype('float')
            df_1_new['power_Wh'] = df_1_new['power_Wh'].astype('float')
            df_1_new['temperature_C'] = df_1_new['temperature_C'].astype('float')
            df_1_new['description'] = df_1_new['description'].astype('string')
            df_1_new['counter'] = df_1_new['counter'].astype(int)
            parquet_path = os.path.join(output_folder, f"{base_name}-data.parquet")
            df_1_new.to_parquet(parquet_path, engine="pyarrow")
            print(f"Saved {parquet_path}")
            data_success = True

        # Process 'summary' field
        if "summary" in mat_data_2:
            df_2 = pd.DataFrame(mat_data_2["summary"][0])
            df_4 = pd.DataFrame()
            for col in ['charge_capacity_Ah','discharge_capacity_Ah','charge_power_Wh','discharge_power_Wh',
                        'charge_median_voltage','discharge_median_voltage','charge_mean_voltage','discharge_mean_voltage']:
                df_4[col] = df_2[col].apply(lambda arr: arr.flatten())
            df_expanded = df_4.apply(pd.Series.explode)
            desc_column = []
            for row in df_2.itertuples(index=False):
                desc = [row.description] * row.charge_capacity_Ah.shape[0]
                desc_column.append(desc)
            desc_df = pd.DataFrame({"description": desc_column})
            desc_df_expanded = desc_df.apply(pd.Series.explode)
            df_2_new = pd.concat([df_expanded, desc_df_expanded], axis=1)
            df_2_new['counter'] = range(len(df_2_new))
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
            parquet_path = os.path.join(output_folder, f"{base_name}-summary.parquet")
            df_2_new.to_parquet(parquet_path, engine="pyarrow")
            print(f"Saved {parquet_path}")
            summary_success = True

        # Move .mat file to done folder if both parquet files were created
        if data_success and summary_success:
            shutil.move(mat_file, os.path.join(done_folder, os.path.basename(mat_file)))
            print(f"Moved {mat_file} to {done_folder}")

if __name__ == "__main__":
    mat_folder = os.path.join(os.path.dirname(__file__), "../mat_files")
    output_folder = os.path.join(os.path.dirname(__file__), "../output_parquet")
    process_mat_files(mat_folder, output_folder)