# codegen
A minimal but powerful tool to generate code in any programming languages

## Usage
Download `codegen.py` file at https://raw.githubusercontent.com/dinhquan/codegen/main/codegen.py

Execute this command to generate code:
```
python codegen.py -t <template path> <variable_name_1>=<variable_value_1> <variable_name_2>=<variable_value_2> ...
```
For example
```
python codegen.py -t templates/ios/MVVM var1=Article
```

## Options
    -h, --help                           Print this help text and exit
    -t, --template                       Path to the template file or folder. It can be relative or absolute path.
    -o, --output                         Output directory. Optional. Default is the directory of codegen.py. 
                                         It can be relative or absolute path.
