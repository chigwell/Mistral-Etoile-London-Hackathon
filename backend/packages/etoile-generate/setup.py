from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='etoile_generate',
    version='0.0.2',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    install_requires=[
        "transformers==4.44.2",
        "tokenizers==0.19.1",
        "langchain==0.1.20",
        "langchain-core==0.1.52",
        "langchain-community==0.0.38",
        "langchain-huggingface==0.0.3",
        "faiss-cpu==1.8.0",
        "sentence-transformers==2.7.0"
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
    tests_require=['unittest'],
    test_suite='test',
)