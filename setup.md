# Project Setup & Execution Guide

Welcome to the **House Price Prediction & Streamlit Deployment** project! Follow these step-by-step instructions to get the code running locally on your computer using VS Code, and prepare it for cloud deployment.

---

## Phase 1: Fork & Clone the Project

Before running code, you need to create your own personal copy of the project on GitHub and download it to your computer.

### Step 1: Fork the Repository
1. Open your web browser and go to: [https://github.com/rabiyakulsum/House-price-prediction](https://github.com/rabiyakulsum/House-price-prediction)


### Step 2: Clone to VS Code
1. On your new forked repository page, click the green **Code** button and copy the secure HTTPS URL provided.
2. Open **VS Code** on your computer.
3. Open the command palette (`Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on Mac) and type `Git: Clone`, then press Enter.
4. Paste the URL you copied and choose a folder on your computer to save the project.
5. When prompted by VS Code, click **Open Repository**.

---

## Phase 2: Running the Project Locally

Now, let's open the terminal inside VS Code and run the files in the correct chronological order.

### Step 1: Open the VS Code Terminal
* Press **`Ctrl + \``** (backtick) on Windows or **`Cmd + \``** on a Mac to open the built-in terminal at the bottom of your screen.

### Step 2: Install Required Libraries
We must install the exact Python tools our code relies on. Run the following command based on your computer's operating system:

  ```bash
  pip install -r requirements.txt
  ```

### Step 3: Run model.py to train the model

Run the following command to train your model and generate the pickle file:

  ```bash
  python model.py
  ```
  
### Step 4: Run the app.py to launch the Web app

Run the below command

  ```bash
  streamlit run app.py
  ```
---

## Phase 3: Deploy on Streamlit

1. Open your web browser, go to [share.streamlit.io](https://share.streamlit.io), and click **"Continue with GitHub"**.
2. Once logged in, click the **Create app** button located in the top-right corner of your workspace.
3. On the deployment configuration page, fill in the fields using the dropdown menus:
   * **Repository:** Select your personal fork (e.g., `your-username/House-price-prediction`).
   * **Branch:** Leave this set to `main` (or `master`).
   * **Main file path:** Change or verify that this points exactly to `app.py`.
4. Click the blue **Deploy!** button at the bottom of the form.







