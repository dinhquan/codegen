import argparse
import os
import shutil

_k_Param_FILENAME = 'FILENAME'

def gen(template, vars, output):
    current_path = os.path.dirname(os.path.abspath(__file__))
    if output:
        output_path = output if os.path.isabs(output) else os.path.join(current_path, output)
    else:
        output_path = current_path

    template_path = template if os.path.isabs(template) else os.path.join(current_path, template)

    if os.path.isfile(template_path):
        forder_path, file_name = os.path.split(template_path)
        gen_code_for_file(file_name, forder_path, output_path, vars)
        return

    template_folder = os.path.basename(template_path)
    new_folder = template_folder
    if has_var(template_folder, vars):
        new_folder = rename_file(template_folder, vars)

    new_folder_path = os.path.join(output_path, new_folder)

    if os.path.exists(new_folder_path):
        shutil.rmtree(new_folder_path)

    shutil.copytree(template_path, new_folder_path)

    for root, _, files in os.walk(new_folder_path):
        for file in files:
            new_file = rename_file(file, vars)
            file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_file)
            os.rename(file_path, new_file_path)
            gen_code_in_file(new_file_path, vars)

    for root, directories, _ in os.walk(new_folder_path):
        for directory in directories:
            new_directory = rename_file(directory, vars)
            os.rename(os.path.join(root, directory), os.path.join(root, new_directory))

def gen_code_in_file(file_path, vars):
    fw = open(file_path, 'r+')
    content = fw.read()

    _, file_name = os.path.split(file_path)
    extra = {_k_Param_FILENAME: file_name}

    new_content, has_replacement = replace_content(content, vars, extra)
    if has_replacement:
        fw.seek(0)
        fw.truncate()
        fw.write(new_content)
        print_success('Generated: ' + file_name)
    else:
        print_error('No variables matched')
    fw.close()

def gen_code_for_file(file, folder_path, out_path, vars):
    file_path = os.path.join(folder_path, file)
    fr = open(file_path, 'r')
    content = fr.read()

    new_file = rename_file(file, vars)
    new_file_path = os.path.join(out_path, new_file)
    fw = open(new_file_path, 'w')

    extra = {_k_Param_FILENAME: new_file}

    new_content, has_replacement = replace_content(content, vars, extra)
    if has_replacement:
        fw.write(new_content)
        print_success('Generated: ' + new_file)
    else:
        print_error('No variables matched')

    fr.close()
    fw.close()

def replace_content(content, vars, extra=None):
    new_content = content
    has_replacement = False
    for var in vars:
        append_var = slash_var(var[0])
        has_replacement = append_var in content
        new_content = replace_var(new_content, append_var, var[1], extra)
    return new_content, has_replacement

def rename_file(file_name, vars):
    new_name = file_name
    for var in vars:
        append_var = slash_var(var[0])
        new_name = replace_var(new_name, append_var, var[1])
    return new_name

def has_var(file_name, vars):
    for var in vars:
        append_var = slash_var(var[0])
        if append_var in file_name:
            return True
    return False

def parse_vars(vars):
    return [x.split('=') for x in vars]

def slash_var(var):
    if len(var) > 3 and var[:2] == '__' and var[-2:] == '__':
        return var
    return '__' + var + '__'

def replace_var(content, var, value, extra=None):
    if len(value) > 2 and value[:1] == '{' and value[-1:] == '}':
        return replace_special_var(content, var, value[1:-1], extra)
    return content.replace(var, value)

def replace_special_var(content, var, value, extra=None):
    if value == _k_Param_FILENAME and extra:
        fileName = extra[_k_Param_FILENAME]
        if fileName:
            return content.replace(var, fileName)
    return content

def print_error(err):
    print('Error: ' + err)

def print_success(msg):
    print(msg)

def main():
    parser = argparse.ArgumentParser(description='Code Generator')
    parser.add_argument('-t', '--template', type=str, 
        help='Template for code generator. It can be a file or folder; relative or absolute path.', 
        required=True)
    parser.add_argument('-o', '--output', type=str, 
        help='Output directory. Default is the current directory.', 
        required=False)
    parser.add_argument('vars', nargs='*')
    args = parser.parse_args()

    template = args.template
    output = args.output
    vars = args.vars

    gen(template, parse_vars(vars), output)

if __name__ == '__main__':
    main()
