This app is built for testing image generation and editing using AI. Currently it runs on Jupyter Notebook. An UI powered by __streamlit__ is under development.

## Running

Create a new virtualenv and run,

```bash
pip install -r requirements.txt
```

### Jupyter Notebook File

- Once requirements are installed open the folder on VSCode.
- Here create two folders `samples` and `output`.
- Put your sample images on the `samples` directory. They should be named as `sample_1.jpg`, `sample_2.jpg` and so on.
- In the `notebook.ipynb` file, change the value of the `sample_no` variable if you want. It has the value `1` by default.
- Run the notebook piece by piece. The resulting image will be stored inside the `output` directory with the same name.
