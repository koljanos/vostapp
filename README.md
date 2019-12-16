# vostapp

## Right now i am at this part

<https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift>

To get the same code on your machine clone the repository with:

``` bash
git clone https://github.com/koljanos/vostapp.git
```

Then create venv and install requirements

``` bash
cd vostapp
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

I've made a simple zsh script to launch a dev server:

``` bash
source run.sh
```

It will declare necessary variables and run flask as dev server
