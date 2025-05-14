FROM quay.io/jupyter/scipy-notebook:2025-05-05

RUN mamba install --yes \
    'jupyterlab_rise' \
    'Faker~=37.1' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

