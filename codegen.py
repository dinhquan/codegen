import argparse
import os

def gen(template, vars):
    current_path = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_path, template)

    if os.path.isfile(template_path):
        forder_path, file_name = os.path.split(template_path)
        gen_code_for_file(file_name, forder_path, current_path, vars)
        return

    files = [f for f in os.listdir(template_path) if os.path.isfile(os.path.join(template_path, f))]
    
    for file in files:
        gen_code_for_file(file, template_path, current_path, vars)

def gen_code_for_file(file, folder_path, out_path, vars):
    file_path = os.path.join(folder_path, file)
    fr = open(file_path, 'r')
    content = fr.read()

    new_file = rename_file(file, vars)
    new_file_path = os.path.join(out_path, new_file)
    fw = open(new_file_path, 'w')

    new_content, has_replacement = replace_content(content, vars)
    if has_replacement:
        fw.write(new_content)
        print_success('Generated: ' + new_file)
    else:
        print_error('No variables matched')

    fr.close()
    fw.close()

def replace_content(content, vars):
    new_content = content
    has_replacement = False
    for var in vars:
        append_var = '__' + var[0] + '__'
        has_replacement = append_var in content
        new_content = new_content.replace(append_var, var[1])
    return new_content, has_replacement

def rename_file(file_name, vars):
    new_name = file_name
    for var in vars:
        append_var = '__' + var[0] + '__'
        new_name = new_name.replace(append_var, var[1])
    return new_name

def parse_vars(vars):
    return [x.split('=') for x in vars]      

def print_error(err):
    print('Error: ' + err)

def print_success(msg):
    print(msg)

def main():
    parser = argparse.ArgumentParser(description='Code Generator')
    parser.add_argument('-t', '--template', type=str, 
        help='Select a template for code generator', 
        required=True)
    parser.add_argument('vars', nargs='*')
    args = parser.parse_args()

    template = args.template
    vars = args.vars

    gen(template, parse_vars(vars))


if __name__ == '__main__':
    main()
