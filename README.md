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

## File Structure

(For an overview of the asset type structure with a UML diagram, please refer to the corresponding GitLab page)

Within admintools, there are two primary directories where the bulk of the custom code lives:

- asset_tracker/assets/
  - admin.py
  - models.py
- asset_tracker/asset_tracker/
  - settings.py



#### admin.py

This file exists primarily exists to customize the view of the admin pages UI. For example, which attributes of a asset type are searchable, which attributes to list as a filter on the right-hand side column, etc.

Within the file, most asset types contains both a resource and admin function. The resource function exists mainly to serve the import/export feature where the function explicitly assigns an asset type to a particular admin function. The admin function exists to define how a specific asset type is viewed within the admin page. For example, which attributes of an asset type are searchable, etc. 



#### models.py

This file exists to define the hierarchical structure of the asset type tree, but also to define each individual attribute of each asset type. For example, this is where we define the Clust asset type to be a subclass of the System asset type and also where each of Clust's attributes are defined. 



#### Settings.py

This file was created by the Django framework, where most of the information contained in here relates to allowed hosts, database connections, etc.


#### run_migrations.sh

A simple two-liner that runs the commands to sync the database with your current Django model structure. For example, this is useful when a change is made to models.py and the database needs to be updated to account for the change.
