sudo rm -rf build/ dist/
sudo python3 setup.py sdist bdist_wheel
twine upload dist/*