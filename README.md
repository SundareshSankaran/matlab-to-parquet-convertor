# MATLAB to Parquet Converter

## Objective

This project provides a script (along with variants) to convert MATLAB `.mat` data files into Parquet format using Python. The conversion process is automated to handle multiple `.mat` files, extract relevant fields for preprocessing (in this case, a `data` and `summary` field unique to this example), and output them as efficient, analysis-ready Parquet files. The project is designed to facilitate data processing, analysis, and integration with modern data science tools.

## Directory Structure

- **/src**  
  Contains the main Python scripts, including `mat_to_parquet.py`, which performs the conversion from `.mat` files to Parquet files.
  
  Also contains some variations on above which were earlier attempts to automatically generate processing code for `.mat` files.

- **/build**  
  Contains build scripts (e.g., `build.sh`), requirements files, and a `/prompts` subdirectory for prompt/result documentation.


- **/build/prompts**  
  Stores markdown files documenting the prompts and results generated during the development process.   The `/build/prompts` subdirectory is relevant since a major portion of this repo was constructed with code generation utilities (GPT 4.1 through GitHub Copilot) and prompts employed for thus are saved for future reference.

- **/mat_files**  
  Directory where input MATLAB `.mat` files should be placed. After successful processing, files are moved to a `done` subfolder.

- **/output_parquet**  
  Directory where the resulting Parquet files are saved. Existing Parquet files are moved to a `done` subfolder at the start of each run.

## Installation

1. Clone this repository.
```bash
git clone https://github.com/SundareshSankaran/matlab-to-parquet-convertor.git
```
2. Ensure you have Python 3.8+ installed.
3. Install dependencies using the provided requirements file:
   ```bash
   cd build
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   Or use the provided `build.sh` script for a fully automated setup.

## Data

- Place your `.mat` files in the `/mat_files` directory.
- After running the conversion script, Parquet files will be available in `/output_parquet`.
- Processed `.mat` files are moved to `/mat_files/done`.
- Previous Parquet files are archived in `/output_parquet/done`.

### Data (used for example purposes only)

To illustrate the use of this repo through an example, we converted data from the [XJTU Battery Experiment](https://wang-fujin.github.io), which is in Matlab format, into parquet files.  The parquet and original Matlab files (which are available on the site) are **not** provided with this repo.  Original Matlab files are under the terms of use specified on their source website (link provided above).  The data was not analysed but merely used as an item for conversion.

*Attribution for the data: Wang, F., Zhai, Z., Zhao, Z. et al. Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis. Nat Commun 15, 4332 (2024). https://doi.org/10.1038/s41467-024-48779-z*

Citations from the paper:
[1]. Wang, F., Zhai, Z., Zhao, Z. et al. Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis. Nature Communications 15, 4332 (2024). （Source Code Available）
[2]. Wang, F., Zhi, Q., Zhao, Z. et al. "Inherently Interpretable Physics-Informed Neural Network for Battery Modeling and Prognosis." IEEE Transactions on Neural Networks and Learning Systems (2023). （Source Code Available）
[3]. Wang F, Zhai Z, Liu B, et al. Open access dataset, code library and benchmarking deep learning approaches for state-of-health estimation of lithium-ion batteries. Journal of Energy Storage, 2024, 77: 109884. （Source Code Available）

## License

This repo is shared under an Apache-2.0 license.

## Contact

For questions, suggestions, or contributions, please contact:

- Name: Sundaresh Sankaran
- Email: [sundaresh.sankaran@gmail.com]
