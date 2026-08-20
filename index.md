#### [William Mann](https://wgmann.github.io), Goizueta Business School, Emory University

## Overview

This is a landing page and documentation file for the [course Github repository](https://github.com/wgmann/FIN323) that I use when I teach FIN323.
Eventually, it may become the main course page.
For now, if you're looking for information about the course, including topics, schedule, assignments, and grading, please see the [syllabus](https://wgmann.github.io/FIN323/syllabus.pdf), or contact me directly.

The purpose of this repo is just to host our course files (slides, Excel examples, homework assignments and solutions, and optional Python code).
I embed links to all these files on our Canvas page, so students are **not** required to deal with this repo directly. 
It's fine to ignore this page and download the files directly from Canvas throughout the semester.

However, if you learn how to work directly with this repo, you may actually find it to be more convenient than going through Canvas.
This is especially true if you want to run the code that you see in the notebooks (`.ipynb` files) in this folder.
The rest of this page explains how to accomplish this, if you are interested.
While not required for the course, I strongly recommend to give it a try!

You will first need to get access to the FRED and WRDS databases. Then you have two options for how to run the code itself: either on the web through GitHub Codespaces, or locally on your own computer after setting up the necessary infrastructure. 

## Database credentials

You will need to set up access to two databases, FRED and WRDS.

- [FRED](https://fred.stlouisfed.org/): 
This is a public data source maintained by the Federal Reserve Bank of St Louis.
It has a wide range of macroeconomic and survey data as well as government bond yields.
You can browse the page for free and even create interactive figures. 
(For example, here's a [figure](https://fred.stlouisfed.org/graph/?g=Jf2U) I'll show a few times in class.)
To pull data over the API, you need to create an account and sign up for a free API key.
Instructions are located [here](https://fred.stlouisfed.org/docs/api/api_key.html).
The API key is a string of letters or numbers that you can include in your data request, much like a password.
The instructions below will explain how to use it.
- [WRDS](https://wrds.wharton.upenn.edu/): 
This is technically not a database, but rather a front end for a large collection of common databases in finance, maintained by the Wharton School.
We will use it to download data on prices and returns for many different investments.
This system is not free to the public, but you can sign up for free access as long as you are enrolled at Emory.
Contact me if you do not already have your access set up, and I will put you in touch with the person who handles this on campus.

Once you have your FRED API key and WRDS username, proceed to either of the next two options.

## Option 1: Run notebooks on GitHub Codespaces (easier)

GitHub Codespaces provides a cloud-based development environment that automatically sets up everything you need to run our course notebooks. If you are new to Git and Python then I recommend you try this first.

(You will need to create a free GitHub account if you don't already have one, but this is strongly recommended anyway. If you really don't want to create a GitHub account, see next section and download the repo as a ZIP file)

1. Open this repository on GitHub in your browser.
2. Click the green "Code" button, select "Codespaces", and click "Create codespace on main" to create your own codespace for this repository.
3. The system will prompt you to enter the WRDS_USERNAME and FRED_API_KEY that you obtained above.
4. The first time you launch the codespace, you will need to wait 10-15 minutes for the environment to build.
5. Then your browser will open a web version of VSCode, and you can navigate to any of our notebooks and run the code. 

For those who already use VSCode locally, you can also connect to your codespace from there instead of the browser: open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`), type "Connect to Codespace", and select the codespace you just created. 
This is a middle ground between a completely browser-based approach (above) and a completely local approach (below).

**Note about other cloud systems:** Github Codespaces is our preferred cloud-based system, but there are many popular alternatives with similar functionality (e.g. Binder or Colab). If you use any such system, please be careful at all times with your database credentials. Only enter them into an appropriate secrets-handling system, not into the text of the notebook file itself. On some of these systems (including Binder) there is no secrets handler at all, in which case you should not use that system to run any code from this class that connects to a database.

## Option 2: Run notebooks on local computer (advanced)

Your own computer can easily run all the code that we use in class if you install a few components that it will look for. This takes a bit more work, but gives a much better experience after that.

1. Clone or download the repo to your own computer:  
    ```  
    git clone https://github.com/wgmann/FIN323  
    cd FIN323
    ```  
    If you don't have a GitHub account and don't want to create one, then download the repo as a zip folder from this site, extract it, and navigate into the directory that is created.
2. Create a virtual environment for the course and activate that environment. The recommended approach is with Conda:
    ```  
    conda create -n FIN323 python=3.12  
    conda activate FIN323  
    ```  
    If for some reason you would rather use basic Python virtual environment instead of Conda, then instead do `python3 -m venv .venv` followed by `source .venv/bin/activate` on Mac/Linux or `.venv\Scripts\activate` on Windows.  
3. Install the course tools, and register the kernel with Jupyter: With the virtual environment still activated from the previous step,  
    ```  
    pip install -e .  
    python -m ipykernel install --user --name FIN323 --display-name "FIN323"  
    ```  
3. Put your database credentials in a file called `.env`:  
    First copy the provided template file `.env.example` to a new one named `.env` (note the `.` at the start of the filename!)
    ```  
    cp .env.example .env  
    ```
    Then open the file `.env` that you just created. You will see the following lines:  
    ```  
    FRED_API_KEY=your_fred_api_key_here  
    WRDS_USERNAME=your_wrds_username_here  
    ```
    Replace everything after the = with your info, and do not use quote marks. For example,  
    ```  
    FRED_API_KEY=abc123  
    WRDS_USERNAME=johndoe  
    ```  
    The `load_dotenv()` function that appears at the start of every notebook will load this information automatically.  
4. Open and run notebooks (`.ipynb` files): If using VSCode, then just open the repo directory you created, select the FIN323 kernel (if this does not happen automatically), and navigate to any file to open and run it.  
You can also avoid using VSCode, and get a slightly better visual experience, by opening the notebooks directly in a browser window. However, the commands for this are a bit clunky:
    - Make sure your terminal window is running from inside the directory you created earlier, with the virtual environment activated.
    - Enter `jupyter notebook` to launch a browser window with a view of the course files. If it does not happen automatically, look for a URL in the output of the command, copy and paste it into a browser window.
    - Navigate to any file to open and run it. You may need to select the `FIN323` kernel if this does not happen automatically.
    - When you are done working, go back to the window where you entered `jupyter notebook`, and enter `Ctrl+C` to kill it.


## Licensing

This repository contains instructional materials and a small amount of
supporting software code.

- **Instructional materials**, including Jupyter notebooks (`.ipynb`),
  written explanations, examples, and course content, are licensed under
  the Creative Commons Attribution–NonCommercial 4.0 International License.
- **Standalone software code files** (e.g. `.py` scripts intended for reuse
  outside the instructional context) are licensed under the MIT License.

See `LICENSE` and `LICENSE-CODE` for details.

