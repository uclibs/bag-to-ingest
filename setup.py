from setuptools import setup

setup(
    name="BagToIngest",
    version="0.1",
    py_modules=["bagtoingest"],
    install_requires=["Click"],
    entry_points="""
       [console_scripts] 
       bagtoingest=bagtoingest:cli
    """,
)
