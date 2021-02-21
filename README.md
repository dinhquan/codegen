# codegen
A minimal but powerful tool to generate code in any programming languages

## Usage
Download `codegen.py` file at https://raw.githubusercontent.com/dinhquan/codegen/main/codegen.py

Run this command to generate code:
```
python codegen.py -t <template path> <variable_name_1>=<variable_value_1> <variable_name_2>=<variable_value_2> ...
```
For example:
```
python codegen.py -t templates/ios/MVVM var1=Article
```

## Options
    -h, --help                           Print the help text.
    -t, --template                       Path to the template file or folder. It can be relative or absolute path.
    -o, --output                         Output directory. Optional. Default is the directory of codegen.py. 
                                         It can be relative or absolute path.

## Create templates
Templates are required to generate code. You must create your template or use existing templates in this repo.

Templates can be a file or folder so you can generate code for a file or a group of files/folders in a folder by one command.

A template file can contain one or many variables. A variable must be wrap with double underscore `__<var name>__`;

For example we have this file
```
// File: __var1__View.tsx

import React from 'react';
import {View} from 'react-native';

interface Props {}

function __var1__View(props: Props) {
  return (
    <View />
  )
}

export default React.memo(__var1__View);
```

To generate code for this file, you need to execute this command:
```
python codegen.py -t __var1__View.tsx var1=Article
```
Then you will have this file:
```
// File: ArticleView.tsx

import React from 'react';
import {View} from 'react-native';

interface Props {}

function ArticleView(props: Props) {
  return (
    <View />
  )
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

