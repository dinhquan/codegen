# codegen
A minimal but powerful tool to generate code in any programming languages

## Usage
Download `codegen.py` file at https://raw.githubusercontent.com/dinhquan/codegen/main/codegen.py

Run this command to generate code:
```
python codegen.py -t <template path> <variable_name_1>=<value_1> <variable_name_2>=<value_2> ...
```
For example:
```
python codegen.py -t templates/__ComponentName__View.jsx ComponentName=Article
```

In this case the template is a folder, so everything inside this template will be generated:
```
python codegen.py \
  -t templates/ios/VIPER \
  ModuleName=User \
  FileName={FILENAME} \
  ProjectName=MyProject \
  UserName=Quan \
  Date=02/01/2021 \
  Year=2021 \
  OrganizationName=MyCompany
```

Use `{FILENAME}` to get the current file name as the value.

## Options
    -h, --help                           Print the help text.
    -t, --template                       Path to the template file or folder. It can be relative or absolute path.
    -o, --output                         Output directory. Optional. Default is the directory of codegen.py. 
                                         It can be relative or absolute path.

## Create templates
Templates are required to generate code. You must create your template or use existing templates in this repo.

Templates can be a file or folder so you can generate code for a file or a group of files/folders in a folder by one command.

A template file can contain one or many variables. A variable must be wrap with double underscore `__<var name>__`;

For example we have this file:
```
// File: __ComponentName__View.jsx

import React from 'react';

function __ComponentName__View() {
  return (
    <div/>
  );
}

export default React.memo(__ComponentName__View);
```

To generate code for this file, you need to execute this command:
```
python codegen.py -t templates/__ComponentName__View.jsx ComponentName=Article
```
Then you will have this file:
```
// File: ArticleView.jsx

import React from 'react';

function ArticleView() {
  return (
    <div/>
  );
}

export default React.memo(ArticleView);
```
## Best practice
You should have `codegen.py` in the root directory of your project, and the templates inside your project.
Python is built in MacOS, Linux and Windows, you and your teammates don't have to install anything.
Just one line command `python codegen.py -t <path_to_template> ....`, files/folders with same structure as your template are generated in less than 1 second.

## Contribution
Because the purpose of this tool is able to generate code in various programming languages, it should have a large number of templates in lots of languages.
Your contributions for templates / pull request are appreciated and welcomed.

