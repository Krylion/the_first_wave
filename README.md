[logo]: https://github.com/Krylion/the_first_wave/blob/master/the_first_wave/static/logo.png
![oops][logo]
##Hello!

Here is my first project, which has been made in association with Pyramid Framework. You can find here many information about Pyramid and Jinja2 template engine.

Unfortunately all website content is in polish only.
Enjoy! :-)



#####How to run The First Wave website?

- Install the prerequisite tools (in Linux):
```
sudo apt-get update
sudo apt-get install python3-dev python3-setuptools
sudo easy_install virtualenv
```

- Configure the environment:
```
cd ~
mkdir pyramid_sites
cd pyramid_sites
```

and...

```
virtualenv --no-site-packages env
source env/bin/activate
easy_install pyramid
easy_install pyramid_jinja2
```


- After that:
```
git clone https://github.com/Krylion/the_first_wave
cd the_first_wave
python setup.py develop
```

- Finally, run the application:
```
pserve production.ini
```

Done