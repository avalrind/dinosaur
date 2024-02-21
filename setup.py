import setuptools

setuptools.setup(
    name = 'dinasour' , 
    version =  '0.0.1' , 
    author = 'Ayush Singhal' , 
    description = 'Animated Data Visualization' , 
    long_description = open('readme.md').read() , 
    long_description_content_type = 'text/markdown' , 
    packages = setuptools.find_packages() , 
    classifiers = [
        'Programming Language :: Python :: 3' , 
        'License :: OSI Approved :: MIT License' , 
        'Operating System :: OS Independent'
    ] ,
    python_requires = '>=3.6' , 
    py_modules = ['dinasour'] ,
    package_dir = {'':'dinasour/src'} ,
    install_requires = ['numpy' , 'matplotlib' , 'pillow' , 'moviepy']
)