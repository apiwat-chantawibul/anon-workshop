# Data Anonymization Workshop

This repository houses the materials for "Introduction to Data Anonymization" workshop.
It includes both reading materials and hands-on exercises in Jupyter notebooks **If you just want to read, you can start from [the intro notebook](notebooks/intro/intro_to_data_anonymization.ipynb)**.

## Running the notebooks

### on Google Colab

Some notebooks contain codes that reader can run and experiment with.
The easiest way to run a notebook is to **click on**

<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>

**badge at the top of the notebook** to open it in Google Colab. However,

- You might need to follow a few more steps to download files into Colab environment depending on the task.
- Runtime resources on Colab is [limited](https://research.google.com/colaboratory/faq.html#limitations-and-restrictions). Runtime environment might be deleted automatically after a period of inactivity.
- Colab environment might get updated out of sync with codes in the notebooks.

### on local machine

Alternatively, the notebooks can also be served from JupyterLab running on local machine using Docker.
To start the JupyterLab server, just enter into `docker` directory and run:

```shell
docker compose up
```

This repository will be automatically mounted inside the container.
You should then

- Follow the link `http://localhost:8888/lab?token=...` printed out by JupyterLab to get into its environment.
- Inside JupyterLab, browse to [the intro notebook at `notebooks/intro/intro_to_data_anonymization.ipynb`](notebooks/intro/intro_to_data_anonymization.ipynb) and follow the workshop material from there.

Running locally allows you to:

- work with all notebooks and files in same environment.
- make sure the environment version matches the code.
- use the runtime however you like

## References

Here are some really [important references](notebooks/references.md) that is used in building this workshop material.
These includes primary source for privcay laws.

## Your Feedback Matters

If this repository has been helpful, please star it and consider opening a
GitHub issue with your feedback or suggestions. Your input is essential for
showcasing the project's impact and informing future development.
