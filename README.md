# Asset Tracker

## Install

### Environment
Conda should be used, due to the uwsgi dependency on Python version 3, and the fact that CentOS is Python 2 centric.

Create `~/.condarc` with the following contents:

```
channels:
  - defaults
  - anaconda
  - conda-forge
auto_activate_base: false
```

Install conda under `/opt/`, installation should add conda to PATH.
If not, then do it manually by adding `/opt/path-to-conda-install/bin` to your PATH and then running the following:
```bash
conda init bash
```

Build conda virtual environment:

```bash
conda create -n python3
conda activate python3
conda install -n python3 --file requirements.txt
which pip #Should be under env, if not find path manually for next command
/opt/miniconda2/envs/python3/bin/pip install django-admin-import=0.3.0
```

### Configuration

#### Basics
https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

#### Systemd
https://uwsgi-docs.readthedocs.io/en/latest/Systemd.html

#### Tyrant
https://uwsgi-docs.readthedocs.io/en/latest/Emperor.html#tyrant-mode-secure-multi-user-hosting
