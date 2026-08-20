This repository contains course materials for FIN 323 taught by William Mann at Emory University. 
See the [landing page](https://wgmann.github.io/FIN323) for detailed instructions.
To use this repo, you can either open the notebooks in GitHub Codespaces or run them locally. 
To run in Codespaces, find the green "Code" button on the [Github repo page](https://github.com/wgmann/FIN323),
click "Launch codespace on main," and wait a few minutes for initial setup.
To run locally:

    git clone https://github.com/wgmann/FIN323
    cd FIN323
    conda create -n FIN323 python=3.12
    conda activate FIN323
    pip install -e .
    python -m ipykernel install --user --name FIN323 --display-name "FIN323 (conda)"
    cp .env.example .env

...and add WRDS username and FRED API key to .env. 

Then, either enter `jupyter notebook` in the terminal (from the same folder as above, with your Conda environment activated), or else open the folder in VSCode or your favorite IDE. Navigate to any notebook file to open and run it.
